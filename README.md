# Health-RI Metadata Schema

This project aims to define the HealthRI core metadata schema using DCAT, DCAT-AP and other standards. This is part of the Health RI portal project, an extension of [Health RI COVID portal](https://covid19initiatives.health-ri.nl/). 

## Core Metadata Schema
The core metadata schema can also be used as a guideline for other portals. The schema can be extended to COVID metadata, Cohort Metadata, Dementia Metadata, governance aspects (Accessibility) etc. The extensions are defined by working groups (e.g. Omics) and are hereby considered [modules](https://github.com/Health-RI/health-ri-metadata/tree/master/Modules).

<!-- - [HRI core metadata mapping spreadsheet](https://docs.google.com/spreadsheets/d/1KKfAxn4ftoOAM2v3WsqT2XcPhdmTjnf1BZkvFf9FqF8/edit#gid=0) -->
- [Core metadata schema specification](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/121110529/Core+Metadata+Schema+Specification) (Health-RI wiki/Confluence).
- HRI core metadata schema diagram (under review):
<img src="https://github.com/Health-RI/health-ri-metadata/blob/master/Images/1.0_plateau1/hricoreschemaplateau1releasecardinality.jpg" alt="diagram" width=1080 height=640 title="diagram">


## [Modules (Leaves/Petals)](https://github.com/Health-RI/health-ri-metadata/tree/master/Modules)
- [Omics](https://github.com/Health-RI/health-ri-metadata/tree/master/Modules/Omics)
- [Imaging](https://github.com/Health-RI/health-ri-metadata/tree/master/Modules/Imaging)
- [Biobanks&Collections](https://github.com/Health-RI/health-ri-metadata/tree/master/Modules/Biobanks%20%26%20Collections)
- Oncology
- Rare Diseases
- ...

## Implementation
The model is part of the requirements to onboard to the Health-RI catalog, and documentation for users is not yet released. However, users can start the onboarding process by publishing their metadata according to this schema in a FAIR Data Point. To start:
- read the explanation of all classes and properties in the [Core Metadata Schema Specification wiki](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/121110529/Core+Metadata+Schema+Specification) 
- collect and map your metadata instances to the model using this [example metadata collection sheet](https://github.com/Health-RI/health-ri-metadata/blob/master/Implementation/metadata%20collection%20sheet%20template.xlsx)
- import the provided [shacl](https://github.com/Health-RI/health-ri-metadata/tree/master/Shapes_rdf_skos) to your FDP (note: tutorial on how to configure your FDP for Health-RI's requirements is being developed)

<!-- ## Sunflower Diagram
To illustrate that after the core, other layers of metadata can be added per domain (e.g. certain funder could require certain metadata information that other funder would not; cancer domain resources need to be described with certain metadata that is not applicable to omics domain resources).

<img src="https://github.com/Health-RI/health-ri-metadata/assets/54810046/c14e2908-6be3-4750-8dae-b625367edc5a" width=360 height=300 > -->


## References
- [Cedar Forms/Templates](https://cedar.metadatacenter.org/dashboard?folderId=https:%2F%2Frepo.metadatacenter.org%2Ffolders%2Fe07ef045-bc38-4e9c-a03f-b53a960b3acc)
- [M4M Guidelines](https://osf.io/2y6ba)
- [DCAT](https://www.w3.org/TR/vocab-dcat/)
- [DCAT AP](https://tehdas.eu/app/uploads/2022/12/tehdas-recommendations-to-enhance-interoperability-within-healthdata-at-eu.pdf)
- [DCAT AP training](https://data.europa.eu/en/dcat-and-dcat-ap-achieving-interoperability-through-data-modelling-and-standardisation)
- [EJP RD Metadata Schema](https://github.com/ejp-rd-vp/resource-metadata-schema)
- Schemas provided by the Health-RI nodes
- Resource for Access metadata: https://www.sciencedirect.com/science/article/pii/S2666979X21000355
- [FAIR Data Point](https://fairdatapoint.readthedocs.io/en/latest/)

## Related projects
- NWO oncology portal
- Cohort NCC
- KWF ICRP Database
- X-Omics
- EJP-RD
- TWOC
- [Health-RI Demonstrator projects](https://www.health-ri.nl/demonstrator-portfolio) 
