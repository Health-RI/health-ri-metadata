# Changelog

## [v2] - YYYY-MM-DD  

### Overview

The new version (v2) of the Health-RI model is somewhat more extensive than v1. While it introduces only a limited number of new mandatory properties, there are many new recommended properties a data holder can use to describe their data.

In [this sheet](Documents/Pre-release_metadata_CoreGenericHealth_p2.xlsx) we state for each property whether it is identical to v1, adapted compared to v1, or completely new (column I). In below table you find an overview of the number of mandatory and recommended properties in both versions.

---

### Summary of Changes

#### Property Counts

In the tables below, you can find an overview of the number of mandatory and recommended properties in both versions.


#### Mandatory Classes

| Class   | v1 Mandatory | v2 Mandatory | v1 Recommended | v2 Recommended |
|---------|--------------|--------------|----------------|----------------|
| Dataset | 10           | 10           | 5              | 37             |
| Catalog | 3            | 5            | 2              | 15             |
| Agent   | 2            | 4            | 0              | 4              |
| Kind    | 2            | 2            | 1              | 1              |

**Total**  
- **Mandatory properties**: increased from **17** to **21**  
- **Recommended properties**: increased from **8** to **57**

#### Remaining Classes

| Class           | v1 Mandatory | v2 Mandatory | v1 Recommended | v2 Recommended |
|----------------|--------------|--------------|----------------|----------------|
| Distribution   | 4            | 5            | 2              | 17             |
| Dataset Series | 10           | 2            | 3              | 10             |
| Data Service   | 2            | 10           | 2              | 12             |

---

### Notable Changes

#### New Mandatory Properties

**Dataset**  
- [access rights](https://healthdcat-ap.github.io/#Dataset.accessrights)
- `keyword`  
- [applicable legislation](https://healthdcat-ap.github.io/#Dataset.applicablelegislation) (uses ELI from EHDS for health datasets)

**Catalog**  
- [contact point](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#catalog-contact-point)
- `dataset`

**Agent**  
- [email](https://healthdcat-ap.github.io/#Agent.email) 
- [homepage](https://healthdcat-ap.github.io/#Agent)

**Data Service**  
- Now includes 10 mandatory properties (up from 2), aligning with **DCAT-AP NL** standards

#### ➖ Deprecated Mandatory Properties (now optional or moved)

**Dataset**  
- `release date`  
- `modification date`  
- `licence` (now belongs to the Distribution class)

---

