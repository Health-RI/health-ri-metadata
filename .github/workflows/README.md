# Workflows for the model release

The data team edits the source Excel (`Documents/Health-RI_v2.1.0.xlsx`) and nothing else. The technical columns
(`prefixes`, `classes` and the `SHACL_*` columns) are computed by [metadata-automation](https://github.com/Health-RI/metadata-automation)
and kept correct by the workflows below. The code lives in that repository; the workflows here only call it, pinned to a
version, and read their file names from the `env` block at the top.

| Workflow | Trigger | Writes | Purpose |
|---|---|---|---|
| `validate.yml` | pull request touching the Excel or the generated SHACLs | nothing | Job 1 checks that the technical columns are correct and complete. Job 2, only when job 1 passes, checks that the committed SHACLs match what the Excel generates. |
| `excel-plan.yml` | manual, input: branch | the plan file `{name}-plan.xlsx`, committed to the branch | Computes what has to change in the technical columns. |
| `shacl-regenerate.yml` | manual, input: branch | the SHACLs, committed to the branch | Regenerates `PiecesShape`, `FairDataPointShape` and `ValidationShape`. Refuses when the Excel check fails. |
| `ci.yml` | pull request touching the SHACLs or the tests | nothing | Runs the SHACL tests with pyshacl. |

## When the Excel check fails

1. Run **Plan Excel columns** with the branch of your pull request. It commits `{name}-plan.xlsx` next to the Excel; nothing in the Excel changes.
2. Pull the branch and inspect the plan. On the `Edits` sheet, set `Apply` to `no` to skip a change or change a proposed value. On the `Gaps` sheet, fill in `Value to apply` for cells that cannot be computed.
3. Apply it and commit the updated Excel (the plan is deleted when it is applied):

   ```bash
   uv tool install git+https://github.com/Health-RI/metadata-automation
   metadata-automation apply-plan -p Documents/Health-RI_v2.1.0-plan.xlsx
   ```

   If the Excel changed since the plan was made, add `--ignore-source-hash`; every edit is still matched on its property URI and checked against the value it expected.

The `SeMPyRO_*` columns are not required yet (`IGNORE_GAPS`), as SeMPyRO classes are not generated from the Excel.

## When the SHACL check fails

Run **Regenerate SHACLs** with the branch of your pull request and pull the commit it makes. The check compares the SHACLs as RDF graphs, so formatting and blank node labels do not count as differences.

Pushes made by a workflow use `GITHUB_TOKEN` and do not start the pull request checks; they run again on your next push.
