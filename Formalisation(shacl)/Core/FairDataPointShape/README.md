# FAIR Data Point Shapes

SHACL bundles prepared for FDP use. Each file combines one schema configured in [Properties.yaml](../Properties.yaml) with the supporting class shapes assigned to it. For v2.1.0, the configured schemas are Resource, Dataset, Catalog, Distribution, Dataset Series, Data Service, and Table Group.

The bundles are assembled from [PiecesShape](../PiecesShape/) and retain the for-FDP specification. The individual pieces are also the input to `FAIRDataPointSchemaTool` for FDP publication; see the [core overview](../README.md) for the packaging and publication relationships and validation considerations.

The existing preprocessing target documented for these files is FDP Reference Implementation 1.16. Compatibility with the FDP version being used requires separate verification.

## Automated tests

[test_shacl.py](../../../tests/test_shacl.py) uses pytest and pySHACL to validate example RDF data against the Catalog, Dataset, Distribution, and Data Service bundles. Additional test cases focus on Dataset. These tests do not cover every bundle or exercise a running FDP installation.
