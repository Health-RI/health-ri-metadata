"""Compare the SHACL Turtle files in a folder with their committed version (HEAD), as RDF graphs.

The generator writes RDF lists with random blank node labels, so regenerating can change the bytes of a file
without changing its content. This script only reports files whose graph actually differs.

Usage: shacl_graph_diff.py PATH [--restore-equivalent]

  --restore-equivalent  put back the committed bytes of files that only differ in blank node labels or formatting,
                        so that git sees no change for them.

Exit code 1 if any file differs as a graph (added, removed or changed), 0 otherwise.
"""

import argparse
import subprocess
import sys
from pathlib import Path

from rdflib import Graph
from rdflib.compare import graph_diff, to_isomorphic


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def committed_files(folder: str) -> set[str]:
    out = git("ls-tree", "-r", "--name-only", "-z", "HEAD", "--", folder)
    return {f for f in out.split("\0") if f.endswith(".ttl")}


def graph_of(turtle: str) -> Graph:
    return Graph().parse(data=turtle, format="turtle")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path")
    parser.add_argument("--restore-equivalent", action="store_true")
    args = parser.parse_args()

    committed = committed_files(args.path)
    current = {p.as_posix() for p in Path(args.path).glob("*.ttl")}
    differing = []

    for name in sorted(committed | current):
        if name not in current:
            differing.append((name, "no longer generated", []))
            continue
        new_text = Path(name).read_text(encoding="utf-8")
        if name not in committed:
            differing.append((name, "newly generated", []))
            continue
        old_text = git("show", f"HEAD:{name}")
        if new_text == old_text:
            continue
        old, new = to_isomorphic(graph_of(old_text)), to_isomorphic(graph_of(new_text))
        if old == new:
            if args.restore_equivalent:
                git("checkout", "HEAD", "--", name)
            continue
        _, only_old, only_new = graph_diff(old, new)
        reason = f"{len(only_old)} triple(s) only in the committed file, {len(only_new)} only in the generated file"
        details = [f"- {s.n3()} {p.n3()} {o.n3()}" for s, p, o in sorted(only_old, key=str)[:5]]
        details += [f"+ {s.n3()} {p.n3()} {o.n3()}" for s, p, o in sorted(only_new, key=str)[:5]]
        differing.append((name, reason, details))

    for name, reason, *details in differing:
        print(f"{name}: {reason}")
        for line in details[0] if details else []:
            print(f"    {line}")
    if not differing:
        print("All SHACL files are equivalent to the committed ones.")
    return 1 if differing else 0


if __name__ == "__main__":
    sys.exit(main())
