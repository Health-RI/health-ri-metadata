# Health-RI Metadata Schemas

This project aims to define the HealthRI core metadata schema using DCAT and other standards. This is part of the Health RI portal project, an extension of [Health RI COVID portal](https://covid19initiatives.health-ri.nl/). 

## Core Metadata Schema
The core metadata schema can also be used as a guideline for other portals. The schema can be extended to COVID metadata, Cohort Metadata, Dementia Metadata, governance aspects (Accessibility) etc. The extensions are defined by working groups (e.g. Omics group) and are hereby called "leaves" or "petals" in reference to the sunflower diagram (see [Leaves Metadata Schema session](https://github.com/Health-RI/health-ri-metadata/edit/master/README.md#leaves-metadata-schema)).

- [HRI core metadata mapping spreadsheet](https://docs.google.com/spreadsheets/d/1KKfAxn4ftoOAM2v3WsqT2XcPhdmTjnf1BZkvFf9FqF8/edit#gid=0)
- HRI core metadata schema (under development)


## [Leaves Metadata Schema](https://github.com/Health-RI/health-ri-metadata/tree/master/Leaves_Petals)
- [Omics](https://github.com/Health-RI/health-ri-metadata/tree/master/Leaves_Petals/Omics)
- Cohorts
- Biobanks
- Oncology
- Rare Diseases
- ...

## Implementation
The official implementation specifications are not yet released, however, one option is for resources to publish their metadata according to this schema in a FAIR Data Point. For that, [shacl](https://github.com/Health-RI/health-ri-metadata/tree/master/shacl) will be provided.

## Sunflower Diagram
For illustrative purposes

<img src="https://github.com/Health-RI/health-ri-metadata/assets/54810046/c14e2908-6be3-4750-8dae-b625367edc5a" alt="sunflower" width=350 height=300 title="sunflower">


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
