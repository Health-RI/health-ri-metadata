from rdflib import Graph, URIRef, Namespace, RDF
from rdflib.term import Node
from typing import Union
from hashlib import sha1
from collections import defaultdict

SHACL = Namespace("http://www.w3.org/ns/shacl#")
PURL_EU_SHACL = Namespace("https://purl.eu/ns/shacl#")


def hash(nodeshape: Union[URIRef, Node], path: Union[URIRef, Node]) -> URIRef:
    base = str(nodeshape)

    hashed = sha1((nodeshape+path).encode("UTF-8"))
    return URIRef(f"{base}/{hashed.hexdigest()}")


def preprocess(source: str) -> None:
    g = Graph().parse(location=source, format="n3")
    output = Graph()

    for nodeshape in g.subjects(RDF.type, SHACL.NodeShape):
        print(f"Found nodeshape {nodeshape}")

        merged = defaultdict(Graph)

        for propertyshape in g.objects(nodeshape, SHACL.property):
            # print(f" Found propertyshape {propertyshape}")

            path = g.value(subject=propertyshape, predicate=SHACL.path)
            # print(f"  concerning path {path}")

            subj = hash(nodeshape, path) #URIRef(f"foo:{sha1((nodeshape+path).encode('utf-8')).hexdigest()}")
            mg = merged[path]

            for p, o in g.predicate_objects(propertyshape):
                if p == PURL_EU_SHACL.message:
                    continue

                if (subj, p, o) not in mg:
                    mg.add((subj, p, o))

        # output nodeshape
        for s, p, o in g.triples((nodeshape, None, None)):
            if p == SHACL.property:
                continue

            output.add((s, p, o))

        for value in merged.values():
            graph = value

            for s in graph.subjects():
                output.add((nodeshape, SHACL.property, s))

            # print(f"merged looks like:\n{merged[path]['graph'].serialize()}")
            output += graph

    print(f"total merged looks like:\n{output.serialize()}")


if __name__ == "__main__":
    release = "https://github.com/SEMICeu/DCAT-AP/raw/master/releases/3.0.0/shacl/dcat-ap-SHACL.ttl"

    preprocess(release)

    print("done")
