# Schema documents

Contains the v2.1.0 schema workbooks, controlled vocabulary instructions, and the v2 modeling decision log.

- `Health-RI_v2.1.0.xlsx`: the schema workbook.
- `Health-RI_v2.1.0-for-FDP.xlsx`: the FDP-specific workbook variant.
- `Controlled_Vocabularies_Instructions.xlsx`: controlled vocabulary guidance.
- `V2_decisionLog.md`: modeling decisions and their rationale.

## Model and FDP specifications

`Health-RI_v2.1.0.xlsx` describes the metadata model. `Health-RI_v2.1.0-for-FDP.xlsx` is the FDP-oriented specification used for the current SHACL outputs. The individual class shapes, grouped FDP bundles, and combined validation graph all follow that FDP-oriented basis.

Exact spreadsheet editing and conversion steps require confirmation from the generation maintainers before they can be documented as reproducible instructions.

### FDP-specific validation rules

The reference metadata specification and its FDP-oriented implementation have different cardinality requirements for two properties:

| Property | Reference specification | FDP-oriented rule | Rationale |
|---|---|---|---|
| `dcat:dataset` on `dcat:Catalog` | `1..n` (mandatory) | `0..n` | The FDP must allow a catalogue to be created before its datasets are added. Requiring a dataset immediately would create a dependency that prevents the initial creation of the catalogue. |
| `dct:title` on `dcat:Distribution` | `0..n` (recommended) | `1..n` (mandatory) | The FDP requires a title to create and manage a distribution as an independently identifiable resource. |

The FDP-oriented workbook specifies a cardinality of `0..n` for `dcat:dataset`, and the corresponding SHACL shape does not enforce a minimum count.

Conversely, the FDP-oriented specification makes `dct:title` mandatory for distributions, and the corresponding SHACL shapes enforce this requirement through `sh:minCount 1`.

These adaptations accommodate the FDP reference implementation without changing the requirements of the reference metadata specification.

The FDP-oriented workbook also contains technical adaptations concerning IRI references, nested SHACL shapes, and DASH viewers and editors. These should be distinguished from the two cardinality changes described above.

The individual class shapes, FDP-specific bundles, and combined validation shapes are all based on the FDP-oriented workbook. Consequently, the combined validation shapes also retain FDP-specific adaptations and should not be treated as an independent SHACL implementation of the reference specification.

See the [core SHACL overview](../Formalisation%28shacl%29/Core/README.md) for the relationships between these SHACL outputs.
