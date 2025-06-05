# Core Metadata Schema Specification

[![Project DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15395604.svg)](https://doi.org/10.5281/zenodo.15395604)
[![Project Status - Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![GitHub last commit](https://img.shields.io/github/last-commit/Health-RI/health-ri-metadata)
![GitHub Created At](https://img.shields.io/github/created-at/Health-RI/health-ri-metadata)
![GitHub Release](https://img.shields.io/github/v/release/Health-RI/health-ri-metadata)
![GitHub Release Date](https://img.shields.io/github/release-date/Health-RI/health-ri-metadata)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/Health-RI/health-ri-metadata/latest)
![GitHub contributors](https://img.shields.io/github/contributors/Health-RI/health-ri-metadata)

This is version 2.0 of Health-RI core metadata schema.

- [Previous published version](#previous-published-version)
- [Purpose and audience](#purpose-and-audience)
- [Introduction](#introduction)
  - [Scope and current state of the Health-RI core metadata schema](#scope-and-current-state-of-the-health-ri-core-metadata-schema)
  - [Used Prefixes](#used-prefixes)
  - [Overview and Diagram](#overview-and-diagram)
- [Permanent URLs for Health-RI Metadata Resources](#permanent-urls-for-health-ri-metadata-resources)
  - [Health-RI Metadata](#health-ri-metadata)
  - [Project Homepage](#project-homepage)
- [Main Classes](#main-classes)
  - [Mandatory Classes](#mandatory-classes)
  - [Recommended Classes](#recommended-classes)
- [Supporting Classes](#supporting-classes)
  - [Mandatory Classes](#mandatory-classes-1)
  - [Recommended Classes](#recommended-classes-1)
- [Main Properties per Class](#main-properties-per-class)
  - [Catalog](#catalog)
  - [Dataset](#dataset)
  - [Data Service](#data-service)
  - [Dataset Series](#dataset-series)
  - [Distribution](#distribution)
  - [Agent](#agent)
  - [Kind](#kind)
  - [Attribution](#attribution)
  - [Checksum](#checksum)
  - [Identifier](#identifier)
  - [Period of time](#period-of-time)
  - [Relationship](#relationship)
  - [Quality certificate](#quality-certificate)
- [Further Information](#further-information)
  - [Model extension](#model-extension)

## Previous published version

The previous published version (version 1.0.2) of the Health-RI core metadata schema is [available here](https://github.com/Health-RI/health-ri-metadata/releases/tag/v1.0.2).

## Purpose and audience

This branch contains the 2nd version of the Health-RI core and generic health metadata schema for the National Health Data Catalogue, detailing the classes and entities involved and offering usage notes for developers. It addresses the schema's design and application but excludes discussion on the National Health Data Catalogue and its onboarding process (these are described [here](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/279150593/Metadata+onboarding+on+the+National+Catalogue)). Please also visit Confluence for general information about the [metadata schema](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/279281676/4A+Metadata+mapping) and [metadata mapping](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/290291734/Mapping+tutorial). **Please note that we are currently still working on the implementation of the new schema into the frontend of the National Health Data Catalogue.**

This documentation aims at a **technical audience** tasked with implementing the metadata schema and stakeholders interested in a detailed understanding of the core metadata schema. With any further questions or comments please contact Health-RI via the [Health-RI ServiceDesk](https://www.health-ri.nl/health-ri-servicedesk) or via [servicedesk@health-ri.nl](mailto:servicedesk@health-ri.nl).

## Introduction

### Scope and current state of the Health-RI core metadata schema

Building on the [1st version of the metadata schema](https://github.com/Health-RI/health-ri-metadata/tree/master), the scope of the version 2 is to incorporate both [DCAT-AP NL](https://geonovum.github.io/DCAT-AP-NL30/) and the (yet to be finalized) [HealthDCAT-AP](https://healthdcat-ap.github.io/), as well as Health-RI specific requirements / needs for the [National Health Data Catalogue](https://catalogus.healthdata.nl/). It introduces several health-related properties (indicated in blue in the UML diagram below), with (where applicable) suggested or required controlled vocabularies.

Please note that HealthDCAT-AP has currently not officially been finalized and is subject to change and further specification. Once the official release is published, we will reevaluate and make the Health-RI schema compatible with HealthDCAT-AP. The current version of the model is based on the HealthDCAT-AP draft, version of 16-12-2024. In that version, cardinalities of HealthDCAT-AP are dependent on different access rights (public, restricted, non-public). It was decided to be compliant with the [open](https://healthdcat-ap.github.io/OPEN%20DATA%20HealthDCAT-AP%203.0.0.drawio.png) version for now, and cardinalities from that UML diagram of the HealthDCAT-AP specification were used as a reference for compliance checking.

In addition, several **ELSI**-related metadata fields, as [gathered](https://health-ri.atlassian.net/wiki/spaces/HA/pages/469893133/Metadata+rondom+gebruiksvoorwaarden+en+authenticatie+autorisatie+en+ELSI+aspecten#Catalogus) by the Health-RI ELSI team, are included in this version 2 of the Health-RI core metadata schema, although not mandatory. The use of these properties will be explored and evaluated once the new version is implemented in the catalogue.

We propose to indicate the **nature of the data** (e.g. whole genome sequencing data, or questionnaire data) with `healthdcatap:healthTheme`. In case you are describing **synthetic data**, you can use the `dct:type` property with the required controlled vocabulary (including a value for synthetic data) in the `dcat:Dataset` class.

Several classes have been included from [DCAT-AP NL](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/) and draft [HealthDCAT-AP](https://healthdcat-ap.github.io/) without further specification so far at Health-RI. This includes the [DataService class](#data-service). Therefore, these classes can be used, but are not yet further modelled to reflect specific needs of dataholders for the National Health Data Catalogue.

### Used Prefixes

| **Prefix**     | **Namespace IRI**                             |
| -------------- | --------------------------------------------- |
| `adms`         | `http://www.w3.org/ns/adms#`                  |
| `dcat`         | `http://www.w3.org/ns/dcat#`                  |
| `dcatap`       | `http://data.europa.eu/r5r/`                  |
| `dct`          | `http://purl.org/dc/terms/`                   |
| `dpv`          | `https://w3id.org/dpv#`                       |
| `dqv`          | `https://www.w3.org/TR/vocab-dqv/`            |
| `eli`          | `http://data.europa.eu/eli/ontology#`         |
| `foaf`         | `http://xmlns.com/foaf/0.1/`                  |
| `owl`          | `http://www.w3.org/2002/07/owl#`              |
| `rdf`          | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs`         | `http://www.w3.org/2000/01/rdf-schema#`       |
| `skos`         | `http://www.w3.org/2004/02/skos/core#`        |
| `spdx`         | `http://spdx.org/rdf/terms#`                  |
| `time`         | `http://www.w3.org/2006/time#`                |
| `vcard`        | `http://www.w3.org/2006/vcard/ns#`            |
| `xsd`          | `http://www.w3.org/2001/XMLSchema#`           |
| `healthdcatap` | TBD                                           |

### Overview and Diagram

An overview of the Metadata schema core is presented in the UML diagram depicted below. The UML showcases the primary classes (entities), excluding the detailed definitions such as `rdfs:label` and `rdfs:comment`. Each block denotes a class and comprises a list of its attributes (properties). Where properties connect to another class (the range of the property is another class), this range is stated in pink font.
If a class is connected to another class by a closed arrow, this indicates that it inherits all properties from the other class. For example, `dcat:Dataset` inherits from `dcat:Resource`. The other arrows represent relations and contain the type of relation, such as `dcat:Dataset` connects to a `dcat:DatasetSeries` via the predicate `dcat:inSeries`, and include the cardinality, such as `dcat:Dataset` can be connected via `dcat:inSeries` to zero or more `dcat:DatasetSeries`. Mandatory relationships are marked with dark labels, recommended relationships with a lighter colour.
In the UML, we have separated the main classes from supporting classes. Relationships between main classes are indicated with arrows as described above. Relationships with supporting classes are not shown with arrows to keep a better overview in the drawing, but can still be deduced from the pink coloured ranges of the listed properties per class.

Properties that are derived from draft [HealthDCAT-AP](https://healthdcat-ap.github.io/) (mostly in the `dcat:Dataset` class) are marked blue.

Next to the UML, a tabular overview of all classes and properties, including their range, cardinality, controlled vocabulary (if applicable), and usage note, can be found below. The same information can be referred to in [this sheet](Documents/Metadata_CoreGenericHealth_v2.xlsx). In this sheet, we also state the history of each property (compared to v1 of the Health-RI core metadata schema) and the origin of the (new) constraint (whether it is taken from DCAT-AP v3, DCAT-AP NL or HealthDCAT-AP).

  UML of the Health-RI core metadata schema diagram (version 2):
<img src="Images/2.0_plateau2/HRI_metadata_p2.png" alt="diagram" width=800 height=1100 title="diagram">

**Some notes on using the metadata schema / mapping**:

- We discriminate between main and supporting classes, and within each group between mandatory and recommended classes.

- The main classes are [Catalog](#catalog), [Dataset](#dataset), [Data Service](#data-service), [Dataset Series](#dataset-series), [Distribution](#distribution)
- The supporting classes are [Agent](#agent), [Kind](#kind), [Attribution](#attribution), [Checksum](#checksum), [Identifier](#identifier), [Period of time](#period-of-time), [Relationship](#relationship), [Quality certificate](#quality-certificate)

- Certain properties (e.g. `dct:publisher`, `dct:creator`, `dct:contactPoint`) in several of the main classes refer to the supporting classes (e.g. [`foaf:Agent`](#agent), [`vcard:Kind`](#kind)). When used, these properties will instantiate new instances of the specific supporting classes for each usage.
This means that, for example, the `dct:publisher` and `dct:creator` can instantiate [`foaf:Agent`](#agent) at two separate times with different content (organisation vs. person).

- It is possible that not all main classes of the metadata schema are necessary to describe your data or the structure of your data. For example, [DataService](#data-service) or [DatasetSeries](#dataset-series) might not apply to all datasets described/onboarded in the National Health Data Catalogue.

- The power of [DCAT](https://www.w3.org/TR/vocab-dcat-3/) is that it is flexible in use, giving a data holder the ability to reflect the structure of their data by using the different classes.

- We aim to collect mapping examples from different data sources [here](https://health-ri.atlassian.net/wiki/spaces/FSD/folder/736985095). Currently, this collection only holds mapping examples to v1 though.

- Please visit Confluence for general information about the [metadata schema](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/279281676/4A+Metadata+mapping) and [metadata mapping](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/290291734/Mapping+tutorial).

## Permanent URLs for Health-RI Metadata Resources

To support long-term FAIR (Findable, Accessible, Interoperable, and Reusable) access to Health-RI Metadata Schema resources, we provide persistent URLs using the [W3ID](https://w3id.org/) system. These permanent identifiers improve the **findability** and **accessibility** of the related artifacts.

The following **W3ID redirects** are available for Health-RI metadata:

### Health-RI Metadata

- **Git repository:** [w3id.org/health-ri/metadata/git](https://w3id.org/health-ri/metadata/git)

#### Versioning & Releases

- **Latest release:** [w3id.org/health-ri/metadata/releases/latest](https://w3id.org/health-ri/metadata/releases/latest)
- **All releases:** [w3id.org/health-ri/metadata/releases](https://w3id.org/health-ri/metadata/releases)
- **Specific release:**
  - Use the following pattern to reference a specific versioned release: `https://w3id.org/health-ri/metadata/releases/{version}`.
  - For example: [w3id.org/health-ri/metadata/releases/v1.0.1](https://w3id.org/health-ri/metadata/releases/v1.0.1)

### Project Homepage

- **Main page:** [w3id.org/health-ri/metadata](https://w3id.org/health-ri/metadata)

## Main Classes

### Mandatory Classes

| **Class name** | **HealthDCAT-AP Definition** | **Usage Note** | **URI** |
| --- | --- | --- | --- |
| [Catalog](#catalog) | A catalogue or repository that hosts the Datasets or Data Services being described. | A catalog that is listed in the National Health Data catalog and contains one or several datasets and/or data services. Used to describe a bundle of datasets (and other resources) under a single title, for example, a collection. | `dcat:Catalog` |
| [Dataset](#dataset) | A conceptual entity that represents the information published. | When focusing on health data, a dataset typically contains structured information gathered from a study or research project related to health topics. This might include clinical trial results, public health statistics, patient records, survey data, etc. <br> How the data in a dataset can be accessed is defined in the Distribution, which usually points to the actual data files available for access or download. Datasets are often included in a catalog, which organizes and provides metadata about multiple datasets, making them easier to find and use. The term 'agent' refers to any entity responsible for creating, maintaining, or distributing the dataset. | `dcat:Dataset` |

### Recommended Classes

| **Class name** | **HealthDCAT-AP Definition** | **Usage Note** | **URI** |
| --- | --- | --- | --- |
| [Data Service](#data-service) | A collection of operations that provides access to one or more datasets or data processing functions. | A Data service offers the possibility to access and query the data of one (or several datasets) through operations. It offers more extensive possibilities to access the data than the Distribution through a variety of potential actions. An example of a Data Service is a [Beacon API](https://docs.genomebeacons.org/) to query genomics data. | `dcat:DataService` |
| [Dataset Series](#dataset-series) | A collection of datasets that are published separately, but share some characteristics that group them. | A Dataset Series is a collection of similar datasets that are somehow interrelated but published separately. An example is consecutive datasets split by year and/or datasets separated by location. Instead of being made available in a single dataset, the individual (e.g. yearly) datasets are linked together with the Dataset Series class. | `dcat:DatasetSeries` |
| [Distribution](#distribution) | A physical embodiment of the Dataset in a particular format. | Used to describe the different ways that a single dataset can be made available in. I.e., it can be downloaded or it can be accessed online in one or more distributions (e.g. one in a downloadable .csv file, another file with an access or query webpage) | `dcat:Distribution` |

## Supporting Classes

### Mandatory Classes

| **Class name** | **HealthDCAT-AP Definition** | **Usage Note** | **URI** |
| --- | --- | --- | --- |
| [Agent](#agent) | Any entity carrying out actions with respect to the (Core) entities Catalogue, Datasets, Data Services and Distributions. | A person or organisation that is associated with the catalogue or dataset. This class is instantiated in these classes whenever the range is `foaf:Agent`. | `foaf:Agent` |
| [Kind](#kind) | A description following the vCard specification. | Used to describe contact information for Dataset and DatasetSeries. This class is instantiated in these classes whenever the range is `vcard:Kind`. | `vcard:Kind` |

### Recommended Classes

| **Class name** | **HealthDCAT-AP Definition** | **Usage Note** | **URI** |
| --- | --- | --- | --- |
| [Attribution](#attribution) | Attribution is the ascribing of an entity to an agent. | This class is instantiated by the property "qualified attribution" (`prov:qualifiedAttribution`) in other classes. Use this class to describe any Agent (other than publisher or creator) that has some form of responsibility for the resource. Within the class, this Agent is described with an instance of `foaf:Agent`, and the role is chosen from a controlled vocabulary. This class can be used to indicate the funding agent that provided funding for the dataset. | `prov:Attribution` |
| [Checksum](#checksum) | A value that allows the contents of a file to be authenticated. | This class is instantiated by properties in other classes that have the range `spdx:Checksum`. | `spdx:Checksum` |
| [Identifier](#identifier) | An identifier in a particular context, consisting of the string that is the identifier; an optional identifier for the identifier scheme; an optional identifier for the version of the identifier scheme; an optional identifier for the agency that manages the identifier scheme. | This class is instantiated by the property "other identifier" (`adms:identifier`) in other classes. Use this class to provide any additional identifier to the resource or dataset that is not the primary identifier provided in `dct:identifier`. | `adms:Identifier` |
| [Period of Time](#period-of-time) | An interval of time that is named or defined by its start and end dates. | This class is instantiated by properties in other classes that have the range `dct:PeriodOfTime`. | `dct:PeriodOfTime` |
| [Relationship](#relationship) | An association class for attaching additional information to a relationship between DCAT Resources. | This class is instantiated by the property "qualified relation" (`dcat:qualifiedRelation`) in other classes. Use this class to describe a relationship with another resource or dataset. Within the class, that resource is indicated, as well as the role this resource has in relation to the described one. The role is indicated based on a controlled vocabulary. | `dcat:Relationship` |
| [Quality Certificate](#quality-certificate) | An annotation that associates a resource (especially, a dataset or a distribution) to another resource (for example, a document) that certifies the resource's quality according to a set of quality assessment rules. | This class is instantiated by the property "quality annotation" (`dqv:hasQualityAnnotation`) in other classes. Use this class to provide a link between the resource or dataset and an associated quality annotation.  | `dqv:QualityCertificate` |

## Main Properties per Class

### [Catalog](https://www.w3.org/TR/vocab-dcat-3/#Class:Catalog)

A catalogue or repository that hosts the Datasets or Data Services being described. <br><br>
`Usage note`: A catalog that is listed in the [National Health Data catalog](https://catalogus.healthdata.nl/) and contains one or several datasets and/or data services. Used to describe a bundle of datasets (and other resources) under a single title, for example, a collection.

#### Mandatory Properties

| **Property label** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [contact point](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) | Relevant contact information for the cataloged resource. | `dcat:contactPoint` | NA | `vcard:Kind` | This property points to a contact point (department or person) that can answer questions about the catalogue. Details on how to describe these are provided under class `vcard:Kind`. <br> Whenever possible, use **general contact information** (for example from a department) instead of contact information of an individual. | 1 | TBD |
| [dataset](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset) | A dataset that is listed in the catalog. | `dcat:dataset` | NA | `dcat:Dataset` | Each catalog contains one or more datasets. This property serves to link datasets to a catalogue. Therefore, a dataset is always contained inside a catalogue. | 1..\* | TBD |
| [description](http://purl.org/dc/terms/description) | An account of the resource. | `dct:description` | NA |`rdfs:Literal` | Briefly describe the catalog and what it contains. You can repeat this in multiple languages. | 1..\* | This catalogue describes the core metadata of AUMC Inflammatory Bowel Disease datasets. <br> This catalogue describes breast cancer imaging, clinical and omics datasets. |
| [publisher](http://purl.org/dc/terms/publisher) | An entity responsible for making the resource available. | `dct:publisher` | NA | `foaf:Agent` | The organisation or individual that is the holder of the intellectual property rights of a dataset. For more details about the publisher, see the class [Agent](#agent). | 1 | name: Radboud University Medical Center <br> identifier: `https://ror.org/05wg1m734` <br> (see class foaf: Agent) |
| [title](http://purl.org/dc/terms/title) | A name given to the resource. | `dct:title` | NA | `rdfs:Literal` | Provide a unique title for your catalog, which can be repeated in multiple languages. | 1..\* | Healthy Brain Study |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [applicable legislation](https://semiceu.github.io/DCAT-AP/r5r/releases/3.0.0/#applicableLegislation) | The legislation that is applicable to this resource. | `dcatap:applicableLegislation` | NA | `eli:LegalResource` | NA | 0..\* |
| [catalog](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_catalog) | A catalog that is listed in the catalog. | `dcat:catalog` | NA | `dcat:Catalog` | For certain research projects, multiple catalogs may need to be organized in a nested manner. This property serves to connect the different catalogs with each other. | 0..\* |
| [creator](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#creator) | An entity responsible for making the resource. | `dct:creator` | NA | `foaf:Agent` | Note that the Health-RI model diverges from DCAT-AP NL here, which reduces the maximum number of creators to 1. The Health-RI model allows the specification of multiple creators of a catalogue. | 0..\* |
| [geographical coverage](http://purl.org/dc/terms/spatial) | Spatial characteristics of the resource. | `dct:spatial` | EU Vocabularies Lists: <br> [Continents](http://publications.europa.eu/resource/authority/continent/) <br> [Countries](http://publications.europa.eu/resource/authority/country) <br> [Places](http://publications.europa.eu/resource/authority/place/) <br> OR <br>[Geonames](http://sws.geonames.org/) OR <br>[CBS Classificaties en begrippen](https://vocabs.cbs.nl/nl/) | `dct:Location` | The EU Vocabularies Name Authority Lists must be used for continents, countries and places that are in those lists; if a particular location is not in one of the mentioned Named Authority Lists, Geonames URIs must be used. For districts or neighbourhoods in NL, the Dutch vocab can be used. | 0..\* |
| [has part](http://purl.org/dc/terms/hasPart) | A related resource that is included either physically or logically in the described resource. | `dct:hasPart` | NA | `dcat:Catalog` | Use this property to establish another catalogue in this catalogue. <br> Note that deeply nested structures should be avoided, and can currently not be displayed in the National Health Data Catalogue. | 0..\* |
| [home page](http://xmlns.com/foaf/spec/#term_homepage) | A homepage for some thing. | `foaf:homepage` | NA | `foaf:Document` | The home page of the catalogue, if available. | 0..1 |
| [language](http://purl.org/dc/terms/language) | A language of the resource. | `dct:language` | [EU Vocabularies Language Authority List](http://publications.europa.eu/resource/authority/language) | `dct:LinguisticSystem` | The value of this property must be an IRI from the provided controlled vocabulary. <br> For example: `http://publications.europa.eu/resource/authority/language/NLD` | 0..\* |
| [licence](http://purl.org/dc/terms/license) | A legal document giving official permission to do something with the resource. | `dct:license` | [Geonovum licence list](https://definities.geostandaarden.nl/dcat-ap-nl/nl/) | `dct:LicenseDocument` | The licence under which the catalogue (with resource description) is made available. In the description of distributions and data services, the licences of that resources are taken up. | 0..1 |
| [modification date](http://purl.org/dc/terms/modified) | Date on which the resource was changed. | `dct:modified` | NA | `xsd:dateTime` | NA | 0..1 |
| [release date](http://purl.org/dc/terms/issued) | Date of formal issuance of the resource. | `dct:issued` | NA | `xsd:dateTime` | NA | 0..1 |
| [rights](http://purl.org/dc/terms/rights) | Information about rights held in and over the resource. | `dct:rights` | NA | `dct:RightsStatement` | The rights statement should be a free-text statement placed at a web-accessible location such that the value of this property is the IRI pointing to that statement. | 0..1 |
| [service](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_service) | A service that is listed in the catalog. | `dcat:service` | NA | `dcat:DataService` | Some datasets may have real-time Data Services (e.g., Beacon API counting individuals). IT teams should define the relationship between the catalog and the Data Service via this property. While crucial for interoperability, this property is not relevant for end-users to collect. | 0..\* |
| [temporal coverage](http://purl.org/dc/terms/temporal) | Temporal characteristics of the resource. | `dct:temporal` |NA | `dct:PeriodOfTime` | Use this property, if applicable to the catalogue, to indicate a time period the catalogue spans. | 0..\* |
| [themes](https://www.w3.org/ns/dcat#themeTaxonomy) | A main category of the resource. A resource can have multiple themes. | `dcat:themeTaxonomy` | NA | `skos:ConceptScheme` | This property refers to a knowledge organisation system used to classify the Catalogue's Datasets. It must have at least the value `NAL:data-theme` as this is the mandatory controlled vocabulary for `dcat:theme`. | 0..\* |

### [Dataset](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset)

A conceptual entity that represents the information published. <br><br>
`Usage note`: When focusing on health data, a dataset typically contains structured information gathered from a study or research project related to health topics. This might include clinical trial results, public health statistics, patient records, survey data, etc. <br> How the data in a dataset can be accessed is defined in the [Distribution](#distribution), which usually points to the actual data files available for access or download. Datasets are often included in a catalog, which organizes and provides metadata about multiple datasets, making them easier to find and use. The term 'agent' refers to any entity responsible for creating, maintaining, or distributing the dataset.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [access rights](http://purl.org/dc/terms/accessRights) | Information about who accesses the resource or an indication of its security status. | `dct:accessRights` | [EU Vocabularies Access Rights Authority List](http://publications.europa.eu/resource/authority/access-right) | [Rights Statement (IRI)](http://publications.europa.eu/resource/authority/access-right) | Information that indicates whether the Dataset is publicly accessible, has access restrictions, or is not public. It is foreseen that one of the three options has to be used: `public`, `restricted`, `non-public`. <br> - Open Data (Public): The dataset is available under general open data rules, such as those covered by the High Value Datasets Implementing Regulation. <br> - Protected Data (Restricted): The dataset contains protected data and is accessible only under specific conditions, as outlined in regulations like the Data Governance Act. <br> - Sensitive Data (Non public): The dataset includes resources that may contain sensitive or personal information, falling under regulations such as the EHDS Regulation. <br><br> Since most data contain personal information, these datasets will need to take the value 'non-public' for the access rights property. | 1 | `http://publications.europa.eu/resource/authority/access-right/RESTRICTED` |
| [applicable legislation](http://data.europa.eu/r5r/applicableLegislation) | The legislation that is applicable to this resource. | `dcatap:applicableLegislation` | NA | `eli:LegalResource` | The ELI of the EHDS was published in March 2025 and can now be included as the applicable legislation mandating that the dataset has to be made public. <br> For health datasets, the value must include the ELI of the [EHDS Regulation](http://data.europa.eu/eli/reg/2025/327/oj). <br> As multiple legislations may apply to the resource, the maximum cardinality is not limited. <br><br> While the applicable legislation indicates which legislation mandates the publication of the dataset, the legal basis property (also in Datasets) described the legal basis for initial collection and processing of (personal) data. | 1..\* | NA |
| [contact point](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) | Relevant contact information for the cataloged resource. | `dcat:contactPoint` | NA | `vcard:Kind` | This property points to a contact point (department or person) that can answer questions about the dataset. Details on how to describe these are provided under class `vcard:Kind`. <br>Whenever possible, use **general contact information** (for example from a department) instead of contact information of an individual. | 1 | mailto: `data-access-committee@xumc.nl` <br> with the name Data Access Committee of the x UMC (see [vcard:Kind](#kind)) |
| [creator](http://purl.org/dc/terms/creator) | An entity responsible for making the resource. | `dct:creator` | NA | `foaf:Agent` | This property points to a person (known as `Agent`) responsible for generating the dataset. In most cases, this should be the project’s Principal Investigator, provided they consent to being listed in the catalogue. If not, the associated department or institute may be specified instead. | 1..\* | Jip Fictief, Inez Maginary, Fabio Abricated for name of `foaf:Agent` |
| [description](http://purl.org/dc/terms/description) | An account of the resource. | `dct:description` | NA | `rdfs:Literal` | Brief description of the dataset. You can repeat this property in multiple languages. | 1..\* | Collection of physiological data of Healthy Brain Study participants. This collection includes measurements via biowearables for heart rate, oxygenation, systolic and diastolic measures and stress levels. |
| [identifier](http://purl.org/dc/terms/identifier) | An unambiguous reference to the resource within a given context. | `dct:identifier` | NA | `rdfs:Literal` | Please see the latest usage recommendations on [this page](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/1084751895/Recommendations+for+filling+in+the+dct+identifier+field+for+Dataset).  | 1 | `https://doi.org/10.34894/ZLOYOJ` |
| [keyword](https://www.w3.org/ns/dcat#keyword) | A keyword or tag describing the resource. | `dcat:keyword` | NA | `rdfs:Literal` | Add keywords to increase dataset discoverability. You can include keywords in different languages, submitting each keyword as a separate entry. | 1..\* | Physiological measures, Heart Rate, Stress Measures |
| [publisher](http://purl.org/dc/terms/publisher) | An entity responsible for making the resource available. | `dct:publisher` | NA | `foaf:Agent` | This property identifies the organisation or individual responsible for making the dataset available. For datasets, this is typically the employer of the data creators. In simple cases, the dataset publisher may be the same as the catalog publisher. In more complex settings, such as when datasets come from multiple institutions within a consortium, the consortium should be listed as the publisher where possible. If no formal consortium can be specified, provide the information of the contributing organizations or individuals under `dct:creator` instead. For more details, refer to the [Agent](#agent) class. | 1 | Radboud University Medical Center; identifier `https://ror.org/05wg1m734` (see foaf: Agent) |
| [theme](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme) | A main category of the resource. A resource can have multiple themes. | `dcat:theme` | [Dataset Theme Vocabulary](http://publications.europa.eu/resource/authority/data-theme) | `skos:Concept` | This property should use a controlled vocabulary. In the Health Data Catalogue, all datasets will use the theme [HEAL](http://publications.europa.eu/resource/authority/data-theme/HEAL), but additional values from the same vocabulary are allowed. | 1..\* | `http://publications.europa.eu/resource/authority/data-theme/HEAL` |
| [title](http://purl.org/dc/terms/title) | A name given to the resource. | `dct:title` | NA | `rdfs:Literal` | Provide a unique title for your Dataset, which can be repeated in multiple languages. | 1..\* | Healthy Brain Study - Physiological Data |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [analytics](https://healthdcat-ap.github.io/#Dataset.analytics) | An analytics distribution of the dataset. | `healthdcatap:analytics` | NA | `dcat:Distribution` | Publishers are encouraged to provide URLs pointing to document repositories where users can access or request associated resources such as technical reports of the dataset, quality measurements, usability indicators,... Note that HealthDCAT-AP mentions also API endpoints or analytics services, but these would not be Distributions but rather DatasetServices. | 0..\* | NA |
| [code values](https://healthdcat-ap.github.io/#Dataset.hascodevalues) | Health classifications and their codes associated with the dataset. | `healthdcatap:hasCodeValues` | NA | `skos:Concept` | Inside this property, you can provide the coding system of the dataset in the form of [wikidata](https://www.wikidata.org/) URI (example: `https://www.wikidata.org/entity/P494` for ICD-10 ID) and the URI of the value that describes the dataset (example: `https://icd.who.int/browse10/2019/en#/Y59.0` for viral vaccines) | 0..\* | `https://www.wikidata.org/entity/P494` for ICD-10 ID and `https://icd.who.int/browse10/2019/en#/Y59.0` for viral vaccines|
| [coding system](https://healthdcat-ap.github.io/#Dataset.hascodingsystem) | Coding systems in use (ex: ICD-10-CM, DGRs, SNOMED-CT, ...). | `healthdcatap:hasCodingSystem` | NA | `dct:Standard (IRI)` | This property provides information on which coding systems are in use inside your dataset. For this, [wikidata](https://www.wikidata.org/) URIs must be used. | 0..\* | `https://www.wikidata.org/entity/P494` (ICD-10 ID) |
| [conforms to](http://purl.org/dc/terms/conformsTo) | An established standard to which the described resource conforms. | `dct:conformsTo` | NA | `dct:Standard (IRI)` | If your data conforms to an established standard or specification, use this property to indicate which one. The [wikidata](https://www.wikidata.org/) URI of the specification must be used. | 0..\* | `https://www.wikidata.org/wiki/Q19597236` for FHIR |
| [distribution](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution) | An available distribution of the dataset. | `dcat:distribution` | NA | `dcat:Distribution` | Metadata element used as a key link to the class Distribution. | 0..\* | NA |
| [documentation](http://xmlns.com/foaf/spec/#term_page) | A page or document about this thing. | `foaf:page` | NA | `foaf:Document (IRI)` | The value of this property is the IRI directing to the webpage or document about the dataset. | 0..\* | NA |
| [frequency](http://purl.org/dc/terms/accrualPeriodicity) | The frequency with which items are added to a collection. | `dct:accrualPeriodicity` | [EU Vocabularies Frequency Authority List](http://publications.europa.eu/resource/authority/frequency) | `skos:Concept` | "The value of this property should be the IRI from the listed controlled vocabulary, indicating the frequency at which the dataset is updated. | 0..1 | `http://publications.europa.eu/resource/authority/frequency/WEEKLY` |
| [geographical coverage](http://purl.org/dc/terms/spatial) | Spatial characteristics of the resource. | `dct:spatial` | EU Vocabularies Lists: <br> [Continents](http://publications.europa.eu/resource/authority/continent/) <br> [Countries](http://publications.europa.eu/resource/authority/country) <br> [Places](http://publications.europa.eu/resource/authority/place/) <br> OR <br>[Geonames](http://sws.geonames.org/) OR <br>[CBS Classificaties en begrippen](https://vocabs.cbs.nl/nl/) | `dct:Location` | The EU Vocabularies Name Authority Lists must be used for continents, countries and places that are in those lists; if a particular location is not in one of the mentioned Named Authority Lists, Geonames URIs must be used. For districts or neighborhoods in NL, the Dutch vocab can be used. However, it might in many cases be desirable to keep the geographical coverage broader (e.g. indicating that NL is covered), to not expose detailed information of subject's locations. | 0..\* | `http://publications.europa.eu/resource/authority/place/NLD_AMS` |
| [has version](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_has_version) | This resource has a more specific, versioned resource. | `dcat:hasVersion` | NA | `dcat:Dataset` | Indicate the dataset which is the other version of the current dataset. | 0..\* | NA |
| [health theme](https://healthdcat-ap.github.io/#Dataset.healththeme) | A category of the Dataset or tag describing the Dataset. | `healthdcatap:healthTheme` | NA | `skos:Concept` | This property is a structured way to tag the dataset with different health themes. This could include, for example, the specific disease the dataset is about. More details can be provided, if desirable, in the keywords' property. *Current status*: the HealthDCAT-AP working group is currently exploring is other sources (ontologies, thesauri) can be used for this, next to [Wikidata](https://www.wikidata.org/). | 0..\* | `https://www.wikidata.org/wiki/Q58624061` |
| [in series](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_in_series) | A dataset series of which the dataset is part. | `dcat:inSeries` | NA | `dcat:DatasetSeries` | This property points to which Dataset Series the Dataset is part of. | 0..\* | NA |
| [is referenced by](http://purl.org/dc/terms/isReferencedBy) | A related resource that references, cites, or otherwise points to the described resource. | `dct:isReferencedBy` | NA | `rdfs:Resource` | The value of this property is the IRI of the doi to the publication or other related resource. | 0..\* | `https://doi.org/10.1186/s13690-021-00709-x` |
| [language](http://purl.org/dc/terms/language) | A language of the resource. | `dct:language` | [EU Vocabularies Language Named Authority List](http://publications.europa.eu/resource/authority/language) | `dct:LinguisticSystem` | The language of the Dataset. For this property, the values from the EU Vocabularies Languages Named Authority List must be used. If your Dataset contains multiple languages, this property can be repeated.  | 0..\* | `http://publications.europa.eu/resource/authority/language/NLD` |
| [legal basis](https://healthdcat-ap.github.io/#Dataset.haslegalbasis) | Indicates use or applicability of a Legal Basis. | `dpv:hasLegalBasis` | [DPV Taxonomy](https://w3c.github.io/dpv/2.0/dpv/modules/legal_basis.html#vocab-legal-basis) | `dpv:LegalBasis` | The legal basis can be provided as a value from the dpv taxonomy (see Controlled vocabulary column). <br><br>While the applicable legislation indicates which legislation mandates the publication of the dataset, the legal basis property described the legal basis for initial collection and processing of (personal) data. <br> Example value for this property could be: dpv:Consent. | 0..\* | `dpv:Consent` |
| [maximum typical age](https://healthdcat-ap.github.io/#Dataset.maxtypicalage) | Maximum typical age of the population within the dataset. | `healthdcatap:maxTypicalAge` | NA | `xsd:nonNegativeInteger` | The approximate maximum age of subjects in the dataset, if applicable. Approximate age is given to protect potentially sensitive information of subjects in the dataset. | 0..1 | NA |
| [minimum typical age](https://healthdcat-ap.github.io/#Dataset.mintypicalage) | Minimum typical age of the population within the dataset. | `healthdcatap:minTypicalAge` | NA | `xsd:nonNegativeInteger` | The approximate minimum age of subjects in the dataset, if applicable. Approximate age is given to protect potentially sensitive information of subjects in the dataset. | 0..1 | NA |
| [modification date](http://purl.org/dc/terms/modified) | Date on which the resource was changed. | `dct:modified` | NA | `xsd:dateTime` | This property indicates changes to the dataset, not the metadata record. An absent value may mean the resource hasn't changed since publication, the modification date is unknown, or the resource is continuously updated. | 0..1 | 2024-06-04T13:36:10.246Z |
| [number of records](https://healthdcat-ap.github.io/#Dataset.numberofrecords) | Size of the dataset in terms of the number of records. | `healthdcatap:numberOfRecords` | NA | `xsd:nonNegativeInteger` | Number of records inside a Dataset. | 0..1 | NA |
| [number of unique individuals](https://healthdcat-ap.github.io/#Dataset.numberofuniqueindividuals) | Number of records for unique individuals. | `healthdcatap:numberOfUniqueIndividuals` | NA | `xsd:nonNegativeInteger` | This property is not mandatory, since not all datasets might include data from individuals. | 0..1 | NA |
| [other identifier](https://healthdcat-ap.github.io/#Dataset.otheridentifier) | Links a resource to an adms:Identifier class. | `adms:identifier` | NA | `adms:Identifier` | Examples for secondary identifiers are `MAST/ADS`, `DataCite`, `DOI`, `EZID` or `W3ID` (if not used for the original identifier). This property makes use of another, small class: `adms:Identifier`, where you provide the identifier and the name of the identifier schema (e.g., DOI). | 0..\* | NA |
| [personal data](https://healthdcat-ap.github.io/#Dataset.haspersonaldata) | Indicates association with Personal Data. | `dpv:hasPersonalData` | [DPV Taxonomy](https://w3c.github.io/dpv/2.0/pd/) | `dpv:PersonalData` | The different types of personal information that are collected in the dataset can be indicated with this property. Values can be picked from the dpv taxonomy (see controlled vocabulary column). <br>For example: dpv-pd:Gender. | 0..\* | NA |
| [population coverage](https://healthdcat-ap.github.io/#Dataset.populationcoverage) | A definition of the population within the dataset. | `healthdcatap:populationCoverage` | NA | `rdfs:Literal` | This field is a free text description of the population covered in the dataset. | 0..\* | Adults aged 18–65 diagnosed with type 2 diabetes in the Netherlands between 2015 and 2020 |
| [purpose](https://w3c.github.io/dpv/2.0/dpv/#dfn-haspurpose) | Indicates association with Purpose. | `dpv:hasPurpose` | [DPV Taxonomy Purposes](https://w3c.github.io/dpv/2.1/dpv/#vocab-purposes) | `dpv:Purpose` | One (or many) category or sub-category of the purposes can be chosen from the taxonomy provided by dpv (see the controlled vocabulary column). <br> Example value could be: dpv:ResearchAndDevelopment. | 0..\* | `dpv:ResearchAndDevelopment` |
| [qualified attribution](https://www.w3.org/TR/prov-o/#qualifiedAttribution) | Attribution is the ascribing of an entity to an agent. | `prov:qualifiedAttribution` | NA | `prov:Attribution` | This property makes use of another small class (`prov:Attribution`). There, you can choose one of the roles as listed in the controlled vocabulary and link that to a specific Agent (expressed with `foaf:Agent`). Note that for HealthDCAT-AP, the list of roles might be extended in the future. <br>Example: `https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#processor` <br><br> Use this property if you would like to indicate the **funder** of the (research project that resulted in creation of the) dataset. <br>The value for role then becomes: `https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#funder`" | 0..\* | See Usage Note |
| [qualified relation](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Dataset.qualifiedrelation) | Link to a description of a relationship with another resource. | `dcat:qualifiedRelation` | NA | `dcat:Relationship` | This property makes use of another small class (`dcat:Relationship`), in which you can indicate the related resource (via its identifier) and the nature of the relation (based on a controlled vocabulary, which is described in the information of the class). | 0..\* | NA |
| [quality annotation](https://www.w3.org/TR/vocab-dqv/#dqv:hasQualityAnnotation) | Refers to a quality annotation. | `dqv:hasQualityAnnotation` | NA | `dqv:QualityCertificate` | This property makes use of another small class (`dqv:QualityCertificate`), in which you indicate the IRI of the quality certificate, linked to the described resource (via the identifier of the dataset). See that class for more information. | 0..\* | NA |
| [release date](http://purl.org/dc/terms/issued) | Date of formal issuance of the resource. | `dct:issued` | NA | `xsd:dateTime` | This property should point to the first known date of issuance, such as the publication date in a data repository. | 0..1 | 2023-12-10T13:16:10.246Z |
| [retention period](https://healthdcat-ap.github.io/#Dataset.retentionPeriod) | A temporal period in which the dataset is available for secondary use. | `healthdcatap:retentionPeriod` | NA | `dct:PeriodOfTime` | This property makes use of the class `dct:PeriodOfTime`, in which a start and end date should be provided. | 0..1 | NA |
| [sample](https://healthdcat-ap.github.io/#Dataset.sample) | Links to a sample of an Asset (which is itself an Asset). | `adms:sample` | NA | `dcat:Distribution` | This property makes use of the `dcat:Distribution` class to describe a sample distribution of the dataset, which can be anonymized or synthetic data, or the data dictionary provided in `CSVW format`. This is currently further developed by the TEHDAS2 program. More information can be [found here.](https://healthdcat-ap.github.io/#sample-distribution) | 0..\* | NA |
| [source](http://purl.org/dc/terms/source) | A related resource from which the described resource is derived. | `dct:source` | NA | `dcat:Dataset` | Indicate the dataset on which this described dataset is based. | 0..\* | NA |
| [status](https://www.w3.org/TR/vocab-adms/#adms-status) | The status of the Asset in the context of a particular workflow process. | `adms:status` | [EU Vocabularies Dataset Status Named Authority List](https://publications.europa.eu/resource/authority/dataset-status) | `skos:Concept` | This property makes use of a controlled vocabulary to indicate the status of the described dataset. | 0..1 | `http://publications.europa.eu/resource/authority/dataset-status/COMPLETED` |
| [temporal coverage](http://purl.org/dc/terms/temporal) | Temporal characteristics of the resource. | `dct:temporal` | NA | `dct:PeriodOfTime` | The start and end date of the period that the dataset covers. This property makes use of a small class: Period of Time, in which a start and end date can be given. | 0..\* | NA |
| [temporal resolution](http://purl.org/dc/terms/temporalResolution) | Minimum time period resolvable in the dataset. | `dcat:temporalResolution` | NA | `xsd:duration` | If the dataset is a time-series, this should correspond to the spacing of items in the series. For other kinds of dataset, this property will usually indicate the smallest time difference between items in the dataset. The time period has to be provided in the `xsd:duration` format. | 0..1 | NA |
| [type](http://purl.org/dc/terms/type) | The nature or genre of the resource. | `dct:type` | [EU Vocabularies Dataset Type Named Authority List](http://publications.europa.eu/resource/authority/dataset-type)| `skos:Concept` | A recommended controlled vocabulary data-type is foreseen. Health datasets with personal information must use 'personal data'. This list supports dataset categorization for the EU Open Data Portal. Currently, 'PERSONAL_DATA' is not included in the EU vocabulary and cannot be filled out. | 0..\* | `http://publications.europa.eu/resource/authority/dataset-type/PERSONAL_DATA` |
| [version](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Dataset.version) | The version indicator (name or identifier) of a resource. | `dcat:version` | NA | `rdfs:Literal` | Suggested practice: track major_version.minor_version. Register a new identifier for major changes (e.g., 1.0.0 for an unchanged dataset). | 0..1 | NA |
| [version notes](https://www.w3.org/ns/legacy_adms#versionNotes) | A description of changes between this version and the previous version of the Asset. | `adms:versionNotes` | NA | `rdfs:Literal` | Provide a short description of changes made to the dataset from the previous version. | 0..\* | NA |
| [was generated by](https://www.w3.org/TR/prov-o/#wasGeneratedBy) | Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation. | `prov:wasGeneratedBy` | NA | `prov:Activity` | NA | 0..\* | NA |

### [Data Service](http://www.w3.org/ns/dcat#DataService)

A collection of operations that provides access to one or more datasets or data processing functions. <br><br>
`Usage note`: A Data service offers the possibility to access and query the data of one (or several datasets) through operations. It offers more extensive possibilities to access the data than the [Distribution](#distribution) through a variety of potential actions. An example of a Data Service is a [Beacon API](https://docs.genomebeacons.org/) to query genomics data.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [access rights](http://purl.org/dc/terms/accessRights) | Information about who accesses the resource or an indication of its security status. | `dct:accessRights` | [EU Vocabularies Access Rights Authority List](http://publications.europa.eu/resource/authority/access-right) | [Rights Statement (IRI)](http://publications.europa.eu/resource/authority/access-right) | Information that indicates whether the Dataset is publicly accessible, has access restrictions, or is not public. This property is required to adopt one of the predefined values listed in the Access Rights Named Authority List provided by the Publications Office. This designation informs data users whether the dataset is considered open data or is classified as non-public. | 1 | For non-public data, use the value: `http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC` |
| [contact point](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) | Relevant contact information for the cataloged resource. | `dcat:contactPoint` | NA | `vcard:Kind` | This property points to a contact point (department or person) that can answer questions about the data service. Details on how to describe these are provided under class `vcard:Kind`. <br> Whenever possible, use **general contact information** (for example from a department) instead of contact information of an individual. | 1 | mailto: `data-access-committee@xumc.nl` <br> with the name Data Access Committee of the x UMC (see `vcard:Kind`) |
| [description](http://purl.org/dc/terms/description) | An account of the resource. | `dct:description` | NA | `rdfs:Literal` | Briefly describe the data service provided. You can repeat this description in multiple languages. | 1..\* | A data service that provides API access to real-time electrocardiogram (ECG) monitoring data for clinical research applications. |
| [end point description](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_description) | A description of the services available via the end-points, including their operations, parameters, etc. | `dcat:endpointDescription` | NA | `rdfs:Resource` | Provides technical documentation that explains how to access and interact with the data service’s endpoint. | 1 | TBD |
| [end point URL](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_url) | The root location or primary endpoint of the service (a Web-resolvable IRI). | `dcat:endpointURL` | NA | `rdfs:Resource` | Provide the URL of the endpoint that users can interact with to access the data service. This should be a direct link to the service's endpoint, such as an API URL, SPARQL endpoint, or similar. | 1 | NA |
| [identifier](http://purl.org/dc/terms/identifier) | An unambiguous reference to the resource within a given context. | `dct:identifier` | NA | `rdfs:Literal` | Provide a unique identifier for the data service. This could be a globally unique and persistent identifier, such as a DOI, URN, or UUID. If no persistent identifier is available, you may use the accessURL or endpointURL as the identifier, provided it is stable and unique to the service. | 1 | NA |
| [licence](http://purl.org/dc/terms/license) | A legal document giving official permission to do something with the resource. | `dct:license` | [Geonovum licence list](https://definities.geostandaarden.nl/dcat-ap-nl/nl/) | `dct:LicenseDocument` | For public data, use a Creative Commons (CC) license (see [Geonovum options](https://definities.geostandaarden.nl/dcat-ap-nl/nl/)). For most National Health Data Catalogue data services, where data is not public, use the 'not open' license from Geonovum and specify data reuse agreements in the `dct:rights` property. | 1 | NA |
| [publisher](http://purl.org/dc/terms/publisher) | An entity responsible for making the resource available. | `dct:publisher` | NA | `foaf:Agent` | The organisation or individual responsible for making the data service available. In the context of data services, the publisher is typically the organisation that manages or provides access to the service. For details, see the class [Agent](#agent). | 1 | name: Radboud University Medical Center <br> identifier: `https://ror.org/05wg1m734` <br> (see class foaf: Agent) |
| [theme](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme) | A main category of the resource. A resource can have multiple themes. | `dcat:theme` | [EU Vocabularies Theme Authority List](https://publications.europa.eu/resource/authority/data-theme) | `skos:Concept` | This property should use the [controlled vocabulary](https://publications.europa.eu/resource/authority/data-theme). In the Health Data Catalogue, most data services will use `NAL:data-theme` 'HEAL', but additional values from the same vocabulary are allowed. | 1..\* | `https://publications.europa.eu/resource/authority/data-theme/HEAL` |
| [title](http://purl.org/dc/terms/title) | A name given to the resource. | `dct:title` | NA | `rdfs:Literal` | NA | 1..\* | NA |

#### Recommended Properties

<!-- TODO: This table misses an example column. -->
| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [applicable legislation](https://semiceu.github.io/DCAT-AP/r5r/releases/3.0.0/#applicableLegislation) | The legislation that is applicable to this resource. | `dcatap:applicableLegislation` | NA |`eli:LegalResource` | TBA | 0..\* |
| [application profile](http://purl.org/dc/terms/conformsTo) | An established standard to which the described resource conforms. | `dct:conformsTo` | NA | `dct:Standard` | The standards referred here SHOULD describe the Data Service and not the data it serves. The latter is provided by the dataset with which this Data Service is connected. For instance, the data service adheres to the OGC WFS API standard, while the associated dataset adheres to the [INSPIRE](https://knowledge-base.inspire.ec.europa.eu/index_en) Address data model. | 0..\* |
| [creator](http://purl.org/dc/terms/creator) | An entity responsible for making the resource. | `dct:creator` | NA | `foaf:Agent` | Note that the Health-RI model diverges from DCAT-AP NL here, which reduces the maximum number of creators to 1. The Health-RI model allows the specification of multiple creators of a data service. | 0..\* |
| [format](http://purl.org/dc/terms/format) | The file format, physical medium, or dimensions of the resource. | `dct:format` | [EU Vocabularies File Type Authority List](http://publications.europa.eu/resource/authority/file-type) | `dct:MediaType or Extent` | The term from the authority table should be used. | 0..\* |
| [HVD Category](https://semiceu.github.io/DCAT-AP/r5r/releases/3.0.0/#hvdCategory) | A data category defined in the High Value Dataset Implementing Regulation. | `dcatap:hvdCategory` | NA | `skos:Concept` | NA | 0..\* |
| [keyword](https://www.w3.org/ns/dcat#keyword) | A keyword or tag describing the resource. | `dcat:keyword` | NA | `rdfs:Literal` | NA | 0..\* |
| [landing page](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_landing_page) | A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information. | `dcat:landingPage` | NA | `foaf:Document` | It is intended to point to a landing page at the original data service provider, not to a page on a site of a third party, such as an aggregator. | 0..\* |
| [language](http://purl.org/dc/terms/language) | A language of the resource. | `dct:language` | [EU Vocabularies Language Authority List](http://publications.europa.eu/resource/authority/language) | `dct:LinguisticSystem` | Indicates the natural language used in the data service, indicated with a value from the [EU controlled vocabulary](https://publications.europa.eu/resource/authority/language). | 0..\* |
| [modification date](http://purl.org/dc/terms/modified) | Date on which the resource was changed. | `dct:modified` | NA | `xsd:dateTime` | This property indicates the date of the last changes to the dataset, not the metadata record. An absent value may mean the resource hasn't changed since publication, the modification date is unknown, or the resource is continuously updated. | 0..1 |
| [other identifier](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataservice-other-identifier) | Links a resource to an `adms:Identifier` class. | `adms:identifier` | NA | `adms:Identifier` | NA | 0..\* |
| [rights](http://purl.org/dc/terms/rights) | Information about rights held in and over the resource. | `dct:rights` | NA | `dct:RightsStatement` | NA | 0..\* |
| [serves dataset](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_serves_dataset) | A collection of data that this data service can distribute. | `dcat:servesDataset` | NA | `dcat:Dataset` | This property connects the Data Service class to its corresponding dataset(s), ensuring every data service links to at least one `dcat:Dataset`. While essential for metadata implementation teams on each node, it's less relevant for researchers to collect. | 0..\* |

### [Dataset Series](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series)

A collection of datasets that are published separately, but share some characteristics that group them. <br><br>
`Usage note`: A Dataset Series is a collection of similar datasets that are somehow interrelated but published separately. An example is consecutive datasets split by year and/or datasets separated by location. Instead of being made available in a single dataset, the individual (e.g. yearly) datasets are linked together with the Dataset Series class.

#### Mandatory Properties

<!-- TODO: This table misses an example column. -->
| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [contact point](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) | Relevant contact information for the cataloged resource. | `dcat:contactPoint` | NA | `vcard:Kind` | This property points to a contact point (department or person) that can answer questions about the dataset series. Details on how to describe these are provided under class `vcard:Kind`. <br> Whenever possible, use **general contact information** (for example from a department) instead of contact information of an individual. | 1..\* |
| [description](http://purl.org/dc/terms/description) | An account of the resource. | `dct:description` | NA | `rdfs:Literal` | Provide a brief description of the dataset series in the catalog. You can repeat this in multiple languages. | 1..\* |
| [title](http://purl.org/dc/terms/title) | A name given to the resource. | `dct:title` | NA |  `rdfs:Literal` | Provide a unique title for your Dataset Series. It can be provided in multiple languages. | 1..\* |

#### Recommended Properties

<!-- TODO: This table misses an example column. -->
| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [applicable legislation](http://data.europa.eu/r5r/applicableLegislation) | The legislation that is applicable to this resource. | `dcatap:applicableLegislation` | NA | `eli:LegalResource` | The legislation that mandates the creation or management of the Dataset Series. | 0..\* |
| [frequency](http://purl.org/dc/terms/accrualPeriodicity) | The frequency with which items are added to a collection. | `dct:accrualPeriodicity` | [EU Vocabularies Frequency Authority List](http://publications.europa.eu/resource/authority/frequency) | `skos:Concept` | The frequency of a dataset series is not equal to the frequency of the dataset in the collection. | 0..1 |
| [geographical coverage](http://purl.org/dc/terms/spatial) | Spatial characteristics of the resource. | `dct:spatial` | EU Vocabularies Lists: <br> [Continents](http://publications.europa.eu/resource/authority/continent/) <br> [Countries](http://publications.europa.eu/resource/authority/country) <br> [Places](http://publications.europa.eu/resource/authority/place/) <br> OR <br>[Geonames](http://sws.geonames.org/) OR <br>[CBS Classificaties en begrippen](https://vocabs.cbs.nl/nl/) | `dct:Location` | The EU Vocabularies Name Authority Lists must be used for [continents](https://publications.europa.eu/resource/authority/continent/), [countries](https://publications.europa.eu/resource/authority/country), and [places](https://publications.europa.eu/resource/authority/place/) that are in those lists. If a particular location is not in one of the mentioned Named Authority Lists, [Geonames URIs](https://sws.geonames.org/) must be used. For districts or neighbourhoods in NL, the [Dutch vocab](https://vocabs.cbs.nl/nl/) can be used. However, it might in many cases be desirable to keep the geographical coverage broader (e.g., indicating that NL is covered) to avoid exposing detailed information about the subjects' locations. | 0..\* |
| [modification date](http://purl.org/dc/terms/modified) | Date on which the resource was changed. | `dct:modified` | NA | `xsd:dateTime` | This does not correspond to the most recently modified dataset in the collection of the dataset series. | 0..1 |
| [publisher](http://purl.org/dc/terms/publisher) | An entity responsible for making the resource available. | `dct:publisher` | NA | `foaf:Agent` | The publisher of the dataset series may not be the publisher of all datasets. E.g., a digital archive could take over the publishing of older datasets in the series. | 0..1 |
| [release date](http://purl.org/dc/terms/issued) | Date of formal issuance of the resource. | `dct:issued` | NA | `xsd:dateTime` | This refers to the moment when the dataset series was established as a managed resource. This is not equal to the release date of the oldest dataset in the collection of the dataset series. | 0..1 |
| [temporal coverage](http://purl.org/dc/terms/temporal) | Temporal characteristics of the resource. | `dct:temporal` | NA | `dct:PeriodOfTime` | When temporal coverage is a dimension in the dataset series, then the temporal coverage of each dataset in the collection should be part of the temporal coverage. In that case, an open-ended value is recommended, e.g., after 2012. | 0..\* |

### [Distribution](http://www.w3.org/ns/dcat#Distribution)

A physical embodiment of the Dataset in a particular format. <br><br>
`Usage note`: Used to describe the different ways that a single dataset can be made available in. I.e., it can be downloaded, or it can be accessed online in one or more distributions (e.g. one in a downloadable `.csv` file, another file with an access or query webpage)

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [access URL](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_url) | A URL of the resource that gives access to a distribution of the dataset. E.g., landing page, feed, SPARQL endpoint. | `dcat:accessURL` | NA | `IRI` | Add a link that points to where the dataset can be found. If it's hosted in a Data Repository, include the link to its entry. For datasets not in a repository (like registries), but still available for secondary use, provide a link to an access request form or a webpage with instructions for accessing the data. | 1 | NA |
| [byte size](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution.bytesize) | The size of a Distribution in bytes. | `dcat:byteSize` | NA | `xsd:nonNegativeInteger` | Describes the size of the distribution (the actual file) in bytes, and is therefore expressed as a non-negative integer. If the actual size is not know, it can be estimated. | 1 | NA |
| [format](http://purl.org/dc/terms/format) | The file format, physical medium, or dimensions of the resource. | `dct:format` | [EU Vocabularies File Type Authority List](http://publications.europa.eu/resource/authority/file-type) | `dct:MediaType or Extent` | This property can be used to describe a media format in more detail than `media type` (using IANA media type) when needed. Instances of this property should use a URL, e.g., from the [File Type vocabulary](https://publications.europa.eu/resource/authority/file-type). For instance, for mzML files, the value of this property could be: `http://edamontology.org/format_3244` | 1 | `http://publications.europa.eu/resource/authority/file-type/TSV` |
| [license](http://purl.org/dc/terms/license) | A legal document giving official permission to do something with the resource. | `dct:license` | [Geonovum licence list](https://definities.geostandaarden.nl/dcat-ap-nl/nl/) | `dct:LicenseDocument` | For public data, use a Creative Commons (CC) license (see [Geonovum options](https://definities.geostandaarden.nl/dcat-ap-nl/nl/)). For most National Health Data Catalogue distributions, where data is not public, use the 'not open' license from Geonovum and specify data reuse agreements in the `dct:rights` property. | 1 | NA |
| [rights](http://purl.org/dc/terms/rights) | Information about rights held in and over the resource. | `dct:rights` | NA | `dct:RightsStatement` | A statement that concerns all rights not addressed in fields `license` or `access rights`. In case of not open data (as specified in the `dct:licence` property), further agreements regarding data reuse (e.g., Data Transfer Agreement, DTA) should be stated in this property. <br> The rights statement should be a free-text statement placed at a web-accessible location such that the value of this property is the IRI pointing to that statement. <br> Current status: This recommendation on how to state data transfer/reuse conditions will be piloted in 2025. | 1 | NA |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [access service](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_service) | A data service that gives access to the distribution of the dataset | `dcat:accessService` | NA | `dcat:DataService` | This property links the distribution class to the corresponding data service(s). | 0..1 | NA |
| [applicable legislation](https://semiceu.github.io/DCAT-AP/r5r/releases/3.0.0/#applicableLegislation) | The legislation that is applicable to this resource. | `dcatap:applicableLegislation` | NA | `eli:LegalResource` | The legislation that mandates the creation or management of the Distribution. | 0..\* | NA |
| [checksum](https://spdx.org/rdf/spdx-terms-v2.2/#d4e1930) | The checksum property provides a mechanism that can be used to verify that the contents of a file or package have not changed. | `spdx:checksum` | NA | `spdx:Checksum` | The checksum is related to the downloadURL. This property makes use of the `spdx:Checksum` class, which itself has two properties to indicate checksum algorithm and checksum value (see [Checksum](#checksum) class for further details). | 0..1 | NA |
| [compression format](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution.compressionformat) | The compression format of the distribution in which the data is contained in a compressed form, e.g., to reduce the size of the downloadable file. | `dcat:compressFormat` | [IANA Media Types](http://www.iana.org/assignments/media-types/media-types.xhtml) | `dct:MediaType` | It MUST be expressed using a media type as defined in the official register of media types managed by [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml). | 0..1 | NA |
| [description](http://purl.org/dc/terms/description) | An account of the resource. | `dct:description` | NA | `rdfs:Literal` | Provide specific details about the distribution here, complementing the description of the related Dataset. This field can be repeated for different language versions of the description. | 0..\* | NA |
| [documentation](http://xmlns.com/foaf/spec/#term_page) | A homepage for some thing. | `foaf:page` | NA | `foaf:Document (IRI)` | This page can contain additional information about the distribution. | 0..\* | NA |
| [download URL](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_download_url) | The URL of the downloadable file in a given format. E.g., CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType. | `dcat:downloadURL` | NA | `IRI` | If the dataset is openly accessible and available in a repository, you can directly include a link to the downloadable file here. | 0..1 | NA |
| [language](http://purl.org/dc/terms/language) | A language of the resource. | `dct:language` | [EU Vocabularies Language Authority List](http://publications.europa.eu/resource/authority/language) |  `dct:LinguisticSystem (IRI)` | Indicates the natural language used in the Distribution, indicated with a value from the EU controlled vocabulary. Not all distributions might have a language, for example, imaging data. <br> Note that here the Health-RI model diverges from DCAT-AP NL, which allows a maximum of 1 language per Distribution. The Health-RI model allows multiple languages in the same Distribution. | 0..\* | NA |
| [linked schemas](http://purl.org/dc/terms/conformsTo) | An established standard to which the described resource conforms. | `dct:conformsTo` | NA | `dct:Standard (IRI)` | This property SHOULD be used to indicate the model, schema, ontology, view, or profile to which this representation of a dataset conforms, in a machine-readable form. This is generally a complementary concern to the media-type or format. Use a reference to the official publication of the respective schema. | 0..\* | NA |
| [media type](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_media_type) | The media type of the distribution as defined by IANA. \[[IANA-MEDIA-TYPES](https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types)\]. | `dcat:mediaType` | [IANA media types](https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types) | `IRI` | Use the specified vocabularies, prioritizing [IANA media types](https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types) whenever possible. If unavailable, consider other ontologies, such as [ZonMw generic terms](https://bioportal.bioontology.org/ontologies/ZONMW-GENERIC/?p=classes&conceptid=http%3A%2F%2Fpurl.org%2Fzonmw%2Fgeneric%2F10105), to describe the format. If IANA media types do not sufficiently describe the format, use "format" to describe it in more detail. | 0..1 | `https://www.iana.org/assignments/media-types/text/csv` |
| [modification date](http://purl.org/dc/terms/modified) | Date on which the resource was changed. | `dct:modified` | NA | `xsd:dateTime` | NA | 0..1 | NA |
| [packaging format](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution.packagingformat) | The package format of the distribution in which one or more data files are grouped together, e.g., to enable a set of related files to be downloaded together. | `dcat:packageFormat` | [IANA media types](https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types) | `dct:MediaType` | It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA.  | 0..1 | NA |
| [release date](http://purl.org/dc/terms/issued) | Date of formal issuance of the resource. | `dct:issued` | NA | `xsd:dateTime` | The date the dataset distribution was issued. | 0..1 | NA |
| [retention period](https://healthdcat-ap.github.io/#Dataset.retentionPeriod) | A temporal period in which the dataset is available for secondary use. | `healthdcatap:retentionPeriod` | NA | `dct:PeriodOfTime` | This property makes use of the class `dct:PeriodOfTime`, in which a start and end date should be provided. | 0..1 | NA |
| [status](https://www.w3.org/ns/legacy_adms#status) | The status of the Asset in the context of a particular workflow process. | `adms:status` | [EU Vocabularies Distribution Status Authority List](http://publications.europa.eu/resource/authority/distribution-status) | `skos:Concept` | It MUST take one of the values: Completed, Deprecated, Under Development, Withdrawn, from the provided controlled vocabulary. | 0..1 | NA |
| [temporal resolution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution.temporalresolution) | Minimum time period resolvable in the dataset. | `dcat:temporalResolution` | NA |`xsd:duration` | If applicable, this property indicates the minimum time period resolvable in the dataset distribution, expressed in `xsd:duration` format (see for more information [here](https://www.w3schools.com/xml/schema_dtypes_date.asp)) | 0..1 | NA |
| [title](http://purl.org/dc/terms/title) | A name given to the resource. | `dct:title` | NA | `rdfs:Literal` | A title given to the distribution. This property can be repeated to provide names in parallel languages. | 0..\* | Data Access Request of Healthy Brain study |

### [Agent](http://xmlns.com/foaf/spec/#term_Agent)

Any entity carrying out actions with respect to the (Core) entities Catalogue, Datasets, Data Services and Distributions. <br><br>
`Usage note`: A person or organisation that is associated with the catalogue or dataset. This class is instantiated in these classes whenever the range is `foaf:Agent`.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [email](http://xmlns.com/foaf/spec/#term_mbox) | An email address via which contact can be made. This property SHOULD be used to provide the email address of the Agent, specified using fully qualified mailto: URI scheme [RFC6068]. The email SHOULD be used to establish a communication channel to the agent. | `foaf:mbox` | NA | `rdfs:Resource` | It is possible to provide the email address of the appropriate institution or department if no personal email address can be provided. <br>The email address has to be provided starting with `mailto:` prefix. <br> For example: mailto:info@example.com / mailto:jane.doe@example.com | 1 |
| [identifier](http://purl.org/dc/terms/identifier) | A unique identifier of the agent. | `dct:identifier` | ORCID: <https://orcid.org/> <br> ROR: <https://ror.org/> <br> ISNI: <https://isni.org/page/search-database/> <br> TOOI: <https://standaarden.overheid.nl/tooi/waardelijsten/> <br> Wikidata: <https://www.wikidata.org/> | `rdfs:Literal` | Specify the entity (person or organisation) by providing an identifier. We recommend using an ORCID identifier for a person or ROR identifier for an organisation. Dutch governmental organisations are listed in TOOI. If these are not available, you can use ISNI, or Wikidata or any other identifier you may have. If you have multiple identifiers, you should provide them all. | 1..\* |
| [name](http://xmlns.com/foaf/spec/#term_name) | A name for some thing. | `foaf:name` | NA | `rdfs:Literal` | This property refers to the given name of the entity. Example: Jane Doe (for a person) and Radboudumc (for an organisation). This property can be repeated for different versions of the name (e.g. the name in different languages). | 1..\* |
| [URL](http://xmlns.com/foaf/spec/#term_homepage) | A homepage for some thing. | `foaf:homepage` | NA | `rdfs:Resource` | Provide the URL of the page containing contact information, such as a contact form or details for reaching out. If a specific contact page is unavailable, the main website of the Agent is sufficient. | 1 |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [country](http://purl.org/dc/terms/spatial) | Country of the agent. | `dct:spatial` | [EU Vocabularies Country Authority List](https://publications.europa.eu/resource/authority/country) | `dct:Location` | Use the appropriate term from the EU authority table. Example for the Netherlands: `http://publications.europa.eu/resource/authority/country/NLD` | 0..\* |
| [publisher note](https://healthdcat-ap.github.io/#Dataset.publishernote) | A property used to provide additional context about a publisher. | `healthdcatap:publisherNote` | NA | `rdfs:Literal` | This property can be repeated for parallel language versions of the publisher's notes. Example: "Sciensano is a research institute and the national public health institute of Belgium. It is a so-called federal scientific institution that operates under the authority of the federal minister of Public Health and the federal minister of Agriculture of Belgium."@en | 0..1 |
| [publisher type](https://healthdcat-ap.github.io/#Dataset.publishertype) | A category (type) of organisation that makes the Dataset available | `healthdcatap:publisherType` | NA | `skos:Concept` | A [controlled vocabulary](https://raw.githubusercontent.com/SEMICeu/ADMS-AP/master/purl.org/ADMS_SKOS_v1.00.rdf) is provided, denoting commonly recognised health publishers. *Current status*: Specifically for the health domain, a controlled vocabulary is being developed to include commonly recognised health publishers. This vocabulary is currently under development. Version 1.0 includes the following types: Academia-ScientificOrganisation, Company, IndustryConsortium, LocalAuthority, NationalAuthority, NonGovernmentalOrganisation, NonProfitOrganisation, PrivateIndividual, RegionalAuthority, StandardisationBody and SupraNationalAuthority. These should use the following URL format: *`http://purl.org/adms/publishertype/[type]`*. | 0..1 |
| [type](http://purl.org/dc/terms/type) | A type of the agent that makes the Catalogue or Dataset available. | `dct:type` |[ADMS Agent Type](https://raw.githubusercontent.com/SEMICeu/ADMS-AP/master/purl.org/ADMS_SKOS_v1.00.rdf) | `skos:Concept` | NA | 0..1 |

### [Kind](https://www.w3.org/TR/vcard-rdf/#d4e1819)

A description following the vCard specification. <br><br>
`Usage note`: Used to describe contact information for [Dataset](#dataset) and [Dataset Series](#dataset-series). This class is instantiated in these classes whenever the range is `vcard:Kind`.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [formatted name](https://www.w3.org/TR/vcard-rdf/#d4e891) | The formatted text corresponding to the name of the object. | `vcard:fn` | NA | `xsd:string` | Provide the full name of the contact point, such as the name of a person or department responsible for communication. | 1 |
| [has email](https://www.w3.org/TR/vcard-rdf/#d4e183) | To specify the electronic mail address for communication with the object. | `vcard:hasEmail` | NA | `rdfs:Resource` | When naming a contact point, this information needs to be further specified with additional information, i.e., an email address. This email address does not need to be a direct contact to the person responsible for the management of the data, it could be a generic information email. The email address has to be provided starting with `mailto:` prefix. <br> For example: `mailto:info@example.com` / `mailto:jane.doe@example.com` | 1 |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [contact page](https://www.w3.org/TR/vcard-rdf/#d4e605) | To specify a uniform resource locator associated with the object. | `vcard:hasURL` | NA | `rdfs:Resource` | A webpage that either allows to make contact (i.e. a webform) or the information contains how to get into contact. | 0..\* |

### [Attribution](https://www.w3.org/ns/prov#Attribution)

Attribution is the ascribing of an entity to an agent. <br><br>
`Usage note`: This class is instantiated by the property "qualified attribution".

#### Mandatory Properties

There are currently no mandatory properties for this class.

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [agent](https://www.w3.org/TR/2013/REC-prov-o-20130430/#p_agent) | The prov:agent property references an prov:Agent which influenced a resource. | `prov:agent` | NA | `foaf:Agent` | This property points to another instance of class `foaf:Agent`. | 0..1 |
| [role](https://www.w3.org/TR/vocab-dcat-3/#Property:relationship_hadRole) | The function of an entity or agent with respect to another entity or resource. | `dcat:hadRole` | [Codelist CI_RoleCode](https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml) | `rdfs:Resource (IRI)` | Choose one of the roles as listed in the controlled vocabulary. Note that for HealthDCAT-AP, the list of roles might be extended in the future. <br> Example: `https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#processor` | 0..1 |

### [Checksum](https://spdx.org/rdf/terms/#d4e2091)

A value that allows the contents of a file to be authenticated. <br><br>
`Usage note`: This class is instantiated by properties in other classes that have the range `spdx:Checksum`.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [algorithm](https://spdx.org/rdf/terms/#algorithm) | Identifies the algorithm used to produce the subject Checksum. | `spdx:algorithm` | [Checksum Algorithm members](https://spdx.org/rdf/terms/#d4e2129) | `spdx:ChecksumAlgorithm` | Choose one member of the checksum algorithm members as indicated on the webpage linked in the Controlled Vocabulary column. | 1 |
| [checksum value](https://spdx.org/rdf/terms/#checksumValue) | The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm. | `spdx:checksumValue` | NA | `xsd:hexBinary` | NA | 1 |

#### Recommended Properties

There are currently no recommended properties for this class.

### [Identifier](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Identifier)

An identifier in a particular context, consisting of the string that is the identifier; an optional identifier for the identifier scheme; an optional identifier for the version of the identifier scheme; an optional identifier for the agency that manages the identifier scheme. <br><br>
`Usage note`: This class is instantiated by the property "other identifier".

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [notation](https://www.w3.org/2009/08/skos-reference/skos.html#notation) | A string that is an identifier in the context of the identifier scheme referenced by its datatype. | `skos:notation` | NA | `rdfs:Literal` | The value of this property is the alternative identifier of the dataset, next to the one indicated in the dct:identifier property. | 1 |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [schema agency](https://www.w3.org/ns/legacy_adms#schemaAgency) | The name of the agency that issued the identifier. | `adms:schemaAgency` | NA | `rdfs:Literal` | NA | 0..1 |

### [Period of time](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Periodoftime)

An interval of time that is named or defined by its start and end dates. <br><br>
`Usage note`: This class is instantiated by properties in other classes that have the range `dct:PeriodOfTime`.

#### Mandatory Properties

There are currently no mandatory properties for this class.

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [end date](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Periodoftime.enddate) | The end of the period. | `dcat:endDate` | NA | `xsd:dateTime` | NA | 0..1 |
| [start date](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Periodoftime.startdate) | The start of the period. | `dcat:startDate` | NA | `xsd:dateTime` | NA | 0..1 |

### [Relationship](https://w3c.github.io/dxwg/dcat/#Class:Relationship)

An association class for attaching additional information to a relationship between DCAT Resources. <br><br>
`Usage note`: This class is instantiated by the property "qualified relation" (`dcat:qualifiedRelation`) in other classes. Use this class to describe a relationship with another resource or dataset. Within the class, that resource is indicated, as well as the role this resource has in relation to the described one. The role is indicated based on a controlled vocabulary.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [had role](https://www.w3.org/TR/vocab-dcat-3/#Property:relationship_hadRole) | The function of an entity or agent with respect to another entity or resource. | `dcat:hadRole` | [IANA Link Relations](https://www.iana.org/assignments/link-relations/link-relations.xhtml) <br> or [ISO Codelist](https://standards.iso.org/iso/19115/resources/Codelists/gml/DS_AssociationTypeCode.xml) | `skos:Concept (IRI)` | Specify, ideally with a value from the linked controlled vocabulary, the nature of the relationship between the linked resources. <br> Example: `http://www.iana.org/assignments/relation/related` | 1..\* |
| [relation](https://www.w3.org/TR/vocab-dcat-3/#Property:relationship_hadRole) | A related resource. | `dct:relation` | NA | `rdfs:Resource (IRI)` | This property establishes the link between the described and the related resources. The value of this property is the IRI of the related resource. | 1..\* |

#### Recommended Properties

There are currently no recommended properties for this class.

### [Quality certificate](https://www.w3.org/TR/vocab-dqv/#dqv:QualityCertificate)

An annotation that associates a resource (especially a dataset or a distribution) to another resource (for example, a document) that certifies the resource's quality according to a set of quality assessment rules. <br><br>
`Usage note`: This class is instantiated by the property "quality annotation" (`dqv:hasQualityAnnotation`) in other classes. Use this class to provide a link between the resource or dataset and an associated quality annotation.

#### Mandatory Properties

There are currently no mandatory properties for this class.

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [target](https://www.w3.org/TR/annotation-vocab/#hastarget) | The relationship between an Annotation and its Target. | `oa:hasTarget` | NA | `rdfs:Resource (IRI)` | This property has to be filled with the same value as the `dct:identifier` of the dataset described, in order to link the quality certificate to that dataset. [See also the example in HealthDCAT-AP.](https://healthdcat-ap.github.io/#dqvhasqualityannotation) | 0..1 |
| [body](https://www.w3.org/TR/annotation-vocab/#hasbody) | The object of the relationship is a resource that is a body of the Annotation. | `oa:hasBody` | NA | `rdfs:Resource (IRI)` | IRI pointing to the location where the quality certificate can be found. | 0..1 |

## Further Information

### Model extension

This is a Health-RI core metadata schema, which means it is designed to be “minimal” and cover the basic metadata elements of catalogue resources. If you come from a specific working group or domain and see some of the important elements from your domain should be represented in the metadata, you could build an extension (or so-called petal) of this model for your domain's specific needs. For more information on this, please check out the [process description for domain-specific metadata](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/545783826/Domain-specific+metadata+schema+development).
