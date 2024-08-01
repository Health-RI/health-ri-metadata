# Core Metadata Schema Specification

## Latest published version
Plateau 1: [https://github.com/Health-RI/health-ri-metadata/tree/master/Formalisation(shacl)/Core/PiecesShape](https://github.com/Health-RI/health-ri-metadata/tree/master/Formalisation(shacl)/Core/PiecesShape)

## Purpose and audience

This repository outlines the Core Metadata Schema, detailing the classes and entities involved and offering usage notes for developers. It addresses the schema's design and application but excludes discussion on the national catalog and its onboarding process. It aims at a technical audience tasked with implementing the metadata schema and stakeholders interested in a detailed understanding of the core schema.

* [Introduction](#introduction)
    * [Scope](#scope)
    * [Mandatory and Recommended](#mandatory-and-recommended)
    * [Terminology](#terminology)
    * [Used Prefixes](#used-prefixes)
    * [Overview and Diagram](#overview-and-diagram)
* [Main Classes](#main-classes)
    * [Mandatory Classes](#mandatory-classes)
    * [Recommended Classes](#recommended-classes)
    * [Abstract Class](#abstract-class)
* [Main Properties per Class](#main-properties-per-class)
    * [Catalog](#catalog)
    * [Dataset](#dataset)
    * [Dataset Series](#dataset-series)
    * [Data Service](#data-service)
    * [Distribution](#distribution)
    * [Agent](#agent)
    * [Kind](#kind)
    * [Cataloged Resource](#cataloged-resource)
* [Feedback, Support, Extension and Implementation](#further-information)

## Introduction

### Scope

To make it easier to share, find and reuse data, the Health-RI nodes decided to list resources in a national directory that can be accessed internationally. They all agreed on what basic information should be included, and that the catalog should be interoperable with other EU portals, which led to the creation of the Core Metadata Schema.

This schema describes the minimum amount of information that should be used to describe resources across Health-RI nodes through the national directory, which is in line with what Plateau 1 offers. The schema can be changed or extended to meet the needs of different areas, and new versions will be released in the future.

### Mandatory and Recommended

Following the [DCAT-AP 3.0](https://semiceu.github.io/DCAT-AP/releases/3.0.0/) specification, we categorize components into `mandatory` and `recommended` classes and properties. A potential third category, `optional`, may be introduced in the future.

In the context of data exchange:

*   **Mandatory** `Class`: Senders **MUST** provide information about instances of the class; Receivers MUST process information about instances of the class.
    
*   **Recommended** `Class`: Senders **SHOULD** provide information about instances of the class if available; Receivers MUST process information about instances of the class.
    
*   **Optional** `Class`: Senders **MAY** provide the information but are not obliged to do so; Receivers MUST process information about instances of the class.
    
*   **Mandatory** `property`: Senders MUST provide the information for that property; Receivers MUST process the information for that property.
    
*   **Recommended** `property`: Senders SHOULD provide the information if available; Receivers MUST process the information for that property.
    
*   **Optional** `property`: Senders MAY provide the information but are not obliged to do so; Receivers MUST process the information for that property.
    

### Terminology

According to [DCAT-AP](https://semiceu.github.io/DCAT-AP/releases/3.0.0/):

*   An **Application Profile** defines the mandatory, recommended, and optional components for a specific use case by leveraging terminology from foundational standards. Additionally, it suggests standardized vocabularies to maintain consistency in the use of terms and data.
    
*   A **Dataset** is a self-contained set of data produced by a specific organization, which can be accessed or downloaded for various uses. A **Data Portal** is an online platform that offers a catalog of datasets and tools to help users locate and utilize these datasets effectively.
    

### Used Prefixes

| **Prefix** | **Namespace IRI** | **Source** |
| --- | --- | --- | 
| `dcat` | `http://www.w3.org/ns/dcat#` | \[[VOCAB-DCAT](https://w3c.github.io/dxwg/dcat/#bib-vocab-dcat "https://w3c.github.io/dxwg/dcat/#bib-vocab-dcat")\] |
| `dct` | `http://purl.org/dc/terms/` | \[[DCT](https://w3c.github.io/dxwg/dcat/#bib-dcterms "https://w3c.github.io/dxwg/dcat/#bib-dcterms")\] |
| `foaf` | `http://xmlns.com/foaf/0.1/` | \[[FOAF](https://w3c.github.io/dxwg/dcat/#bib-foaf "https://w3c.github.io/dxwg/dcat/#bib-foaf")\] |
| `owl` | `http://www.w3.org/2002/07/owl#` | \[[OWL2-SYNTAX](https://w3c.github.io/dxwg/dcat/#bib-owl2-syntax "https://w3c.github.io/dxwg/dcat/#bib-owl2-syntax")\] |
| `rdf` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` | \[[RDF-SYNTAX-GRAMMAR](https://w3c.github.io/dxwg/dcat/#bib-rdf-syntax-grammar "https://w3c.github.io/dxwg/dcat/#bib-rdf-syntax-grammar")\] |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` | \[[RDF-SCHEMA](https://w3c.github.io/dxwg/dcat/#bib-rdf-schema "https://w3c.github.io/dxwg/dcat/#bib-rdf-schema")\] |
| `skos` | `http://www.w3.org/2004/02/skos/core#` | \[[SKOS-REFERENCE](https://w3c.github.io/dxwg/dcat/#bib-skos-reference "https://w3c.github.io/dxwg/dcat/#bib-skos-reference")\] |
| `time` | `http://www.w3.org/2006/time#` | \[[OWL-TIME](https://w3c.github.io/dxwg/dcat/#bib-owl-time "https://w3c.github.io/dxwg/dcat/#bib-owl-time")\] |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` | \[[XMLSCHEMA11-2](https://w3c.github.io/dxwg/dcat/#bib-xmlschema11-2 "https://w3c.github.io/dxwg/dcat/#bib-xmlschema11-2")\] |
| `vcard` | `http://www.w3.org/2006/vcard/ns#` | \[[VCARD](https://www.w3.org/TR/vcard-rdf/ "https://www.w3.org/TR/vcard-rdf/")\] |

### Overview and Diagram

An overview of the Metadata schema core is presented in the [UML](https://www.omg.org/spec/UML "https://www.omg.org/spec/UML") diagram depicted below. The UML showcases the primary classes (entities), excluding the detailed definitions such as `rdfs:label` and `rdfs:comment`. Each block denotes a class and comprises a list of its attributes (properties). If a class is connected to another class by a closed arrow, indicating that it inherits all properties from the other class. For example, `dcat:DatasetSeries` inherits from `dcat:Dataset` which inherits from `dcat:Resource`. The other arrows, represent relations and contain the type of relation, such as `dcat:Dataset` connects to a `dcat:DatasetSeries` via the predicate `dcat:inSeries`, and include the cardinality, such as `dcat:Dataset` can be connected via `dcat:inSeries` to zero or more `dcat:DatasetSeries`.

- HRI core metadata schema diagram (plateau 1):
<img src="Images/1.0_plateau1/HRICoreSchemaReleasePlateau1.jpg" alt="diagram" width=1080 height=560 title="diagram">

## Main Classes

### Mandatory Classes
   
| **Class name** | **Definition** | **Usage Note** | **URI** | **Example** |
| --- | --- | --- | --- | --- |
| [Dataset](#dataset) | A resource type. <br>A meaningful collection of data, published or curated by a single organisation or individual, and available for access or download in one or more representations. | When focusing on health data, a dataset typically contains structured information gathered from a study or research project related to health topics. This might include clinical trial results, public health statistics, patient records, survey data, etc.  <br>How the data in a dataset can be accessed is defined in the Distribution, which usually points to the actual data files available for access or download. Datasets are often included in a catalog, which organizes and provides metadata about multiple datasets, making them easier to find and use. The term 'organization or individual' refers to any entity responsible for creating, maintaining, or distributing the dataset. | `dcat:Dataset` | Questionnaire data of the Personalised RISk-based MAmmascreening Study (PRISMA),  <br>Clinical data for Inflammatory Bowel Disease (IBD) from AUMC, LUMC and UMCG |
| [Catalog](#catalog) | A catalog that is listed in the National catalog. | Used to describe a bundle of datasets (and other resources) under a single title, for example a collection or a study. | `dcat:Catalog` | NA  |
| [Agent](#agent) | An entity that is associated with catalog and/or Datasets. | A person or organization that is associated with the catalogue and/or datasets. | `foaf:Agent` | NA  |
| [Cataloged Resource](#cataloged-resource) | Resource published or curated by a single agent. | This is an abstract class, we do not use this class, instead we use specifications of it (e.g. Dataset). This is mainly for a high level grouping and the reuse of properties. | `dcat:Resource` | NA  |
| [Kind](#kind) | A description following the vCard specification, e.g. to provide telephone number and e-mail address for a contact point. | Used to describe contact information for Dataset and DatasetSeries. | `vcard:Kind` | NA  |

### Recommended Classes

| **Class name** | **Definition** | **Usage Note** | **URI** |
| --- | --- | --- | --- |   
| [Distribution](#distribution) | An available distribution of the dataset. | Used to describe the different ways that a single dataset can be made available in. I.e., it can be downloaded or it can be accessed online in one or more distributions (e.g. one in a downloadable .csv file, another file with an access or query webpage) | `dcat:Distribution` |
| [Dataset Series](#dataset-series) | A collection of datasets that are published separately, but share some characteristics that group them. | With Dataset Series we refer to data, somehow interrelated, that are published separately. An example is budget data split by year and/or country, instead of being made available in a single dataset. | `dcat:DatasetSeries` |
| [Data Service](#data-service) | A Resource type.  <br>A collection of operations that provides access to one or more datasets or data processing functions. | The kind of service can be indicated using the `dcterms:type` property. Its value may be taken from a controlled vocabulary that should be defined in the community. | `dcat:DataService` |

### _Abstract Class_

_**Cataloged Resource**_ is a generic concept from the DCAT vocabulary, that is rarely used directly, but indirectly through its extensions. We recommend avoiding using `dcat:Resource` directly for your document and requesting a model extension or update, in case the type/class you need is not in this schema.

| **Class name** | **Definition** | **Usage Note** | **URI** |
| --- | --- | --- | --- |   
| [_Cataloged Resource_](#cataloged-resource) | The class resource, everything. | This class is for grouping and class hierarchy relation purposes. | `dcat:Resource` |

## Main Properties per Class

### [Catalog](https://www.w3.org/TR/vocab-dcat-3/#Class:Catalog)

A curated collection of metadata about resources. A web-based data catalog is typically represented as a single instance of this class.

#### Mandatory Properties
   
| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- |  
| [title](http://purl.org/dc/terms/title) | A name given to the resource. | `dct:title` | `rdfs:Literal` | A name given to the catalogue. This property can be repeated for providing titles in different languages. This is a required field and needs to be unique. | 1..\* | Inflammatory Bowel Disease catalogue,  <br>Inflammatoire darmziekten catalogus |
| [description](http://purl.org/dc/terms/description) | A free-text account of the record. | `dct:description` | `rdfs:Literal` | A brief informative description of the catalogue. This property can be repeated for descriptions in different languages. | 1..\* | This catalogue describes the core metadata of AUMC Inflammatory Bowel Disease datasets or  <br>This catalogue describes breast cancer imaging, clinical and omics datasets. |
| [publisher](http://purl.org/dc/terms/publisher) | The entity responsible for making the catalogue available. | `dct:publisher` | `foaf:Agent` | The organization that published the catalogue (e.g. the specific UMC in question). In case of a multicenter study, the publisher is the organisation who makes the catalogue available online. To list multiple organisations involved, refer to the "creator" property. | 1..\* | name: Radboud University Medical Center  <br>identifier: https://ror.org/05wg1m734  <br>(see class foaf: Agent) |

#### Recommended Properties
    
| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | 
| [catalog](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_catalog) | A catalog that is listed in the catalog. | `dcat:catalog` | `dcat:Catalog` | NA  | 0..\* |
| [dataset](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset) | relates every catalog to its containing datasets. | `dcat:dataset` | `dcat:Dataset` | The connection to the one or more datasets that this catalog describes. | 0..\* |
| [service](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_service) | A service that is listed in the catalog. | `dcat:service` | `dcat:DataService` | NA  | 0..\* |

### [Dataset](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset)

A meaningful collection of data, published or curated by a single organisation or individual, and available for access or download in one or more representations.

#### Mandatory Properties
 
| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- | 
| [contact point](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) | Relevant contact information for the catalog resource. | `dcat:contactPoint` | `vcard:Kind` | Contact information that can be used, for example, for sending requests for information or access to the dataset. Ideally, a data access committee or other service desk (a contact point that is rather persistent over time). | 1..\* | mailto: data-access-committee@xumc.nl  <br>with name Data Access Committee of the x UMC (see vcard:Kind) |
| [creator](http://purl.org/dc/terms/creator) | The entity responsible for producing the resource. | `dct:creator` | `foaf:Agent` | The person or persons responsible for creating the dataset. | 1..\* | Jip Fictief, Inez Maginary, Fabio Abricated for name of foaf:Agent |
| [description](http://purl.org/dc/terms/description) | A free-text account of the record | `dct:description` | `rdfs:Literal` | A free-text informative description of the dataset. This property can be repeated for providing descriptions in different languages. | 1..\* | The primary aim of the PRISMA study was to investigate the potential value of risk-tailored versus traditional breast cancer screening protocols in the Netherlands. Data collection took place between 2014-2019, resulting in ∼67,000 mammograms, ∼38,000 surveys, ∼10,000 blood samples and ∼600 saliva samples. |
| [issued](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/issued/) | Date of formal issuance (e.g., publication) of the resource. | `dct:issued` | `xsd:dateTime` | The date and time when the dataset was first issued. | 1..1 | 2024-06-04T13:36:10.246Z |
| [identifier](http://purl.org/dc/terms/identifier) | A unique identifier of the resource being described or catalogued. | `dct:identifier` | `xsd:string` | The main globally unique and persistent identifier of the dataset. Recommended practice is to identify the dataset by means of a string conforming to an identification system such as Digital Object Identifier (DOI). | 1..1 | https://doi.org/10.34894/ZLOYOJ |
| [modified](http://purl.org/dc/terms/modified) | Most recent date on which the catalog entry was changed, updated or modified. | `dct:modified` | `xsd:dateTime` | The value indicates a change to the actual dataset, not a change to the catalog record. An absent value may indicate that the resource has never changed after its initial publication, or that the date of last modification is not known, or that the resource is continuously updated. | 1..1 | 2024-06-04T13:36:10.246Z |
| [publisher](http://purl.org/dc/terms/publisher) | The entity responsible for making the resource available. | `dct:publisher` | `foaf:Agent` | The organization that published the dataset (e.g. the specific UMC in question). Can differ from catalogue publisher. | 1..\* | Radboud University Medical Center; identifier https://ror.org/05wg1m734 (see foaf: Agent) |
| [theme](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme) | A main category of the resource. A resource can have multiple themes. | `dcat:theme` | `IRI` | Consists of 1 or more IRIs (links) separated by commas. When set, it specifies relevant ontology concepts that classify the dataset. Typically, these can be looked up using the Ontology Lookup Service (OLS) or Bioportal | 1..\* | http://publications.europa.eu/resource/authority/data-theme/HEAL |
| [title](http://purl.org/dc/terms/title) | A name given to the record. | `dct:title` | `rdfs:Literal` | A name given to the Dataset. This property can be repeated for providing names in parallel languages. | 1..\* | Questionnaire data of the Personalised RISk-based MAmmascreening Study (PRISMA) |
| [license](http://purl.org/dc/terms/license) | A legal document under which the resource is made available. | `dct:license` | `IRI` | This should contain a URL that provides details regarding the license that is applicable to this dataset (open data commons, data access policy link etc.) | 1..1 | NA  |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- |    
| [distribution](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution) | An available distribution of the dataset. | `dcat:distribution` | `dcat:Distribution` | Use this property to point to the distribution of this dataset when a distribution is available. | 0..\* | NA  |
| [keyword](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_keyword) | A keyword or tag describing the dataset. | `dcat:keyword` | `rdfs:Literal` | Use this property to add keywords that describe the dataset for better findability. | 0..\* | NA  |
| [type](http://purl.org/dc/terms/type) | The nature or genre of the resource. | `dct:type` | `IRI` | The value SHOULD be taken from a well governed and broadly recognised controlled vocabulary, such as [DCMI Type vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#DCMIType) | 0..\* | http://purl.org/dc/dcmitype/MovingImage |
| [version](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version) | The version indicator (name or identifier) of a resource. | `dcat:version` | `rdfs:Literal` | NA  | 0..\* | NA  |
| [in series](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_in_series) | A dataset series of which the dataset is part. | `dcat:inSeries` | `dcat:DatasetSeries` | NA  | 0..\* | NA  |

### [Dataset Series](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series)


#### Mandatory Properties
  
| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- |   
| [contact point](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) | Relevant contact information for the catalog resource. | `dcat:contactPoint` | `vcard:Kind` | Contact information that can be used, for example, for sending requests for information or access to the dataset. Ideally, a data access committee or other service desk (a contact point that is rather persistent over time). | 1..\* | mailto: data-access-committee@xumc.nl  <br>with name Data Access Committee of the x UMC (see vcard:Kind) |
| [creator](http://purl.org/dc/terms/creator) | The entity responsible for producing the resource. | `dct:creator` | `foaf:Agent` | The person or persons responsible for creating the dataset. | 1..\* | Jip Fictief, Inez Maginary, Fabio Abricated for name of foaf:Agent |
| [description](http://purl.org/dc/terms/description) | A free-text account of the record | `dct:description` | `rdfs:Literal` | A free-text informative description of the dataset. This property can be repeated for providing descriptions in different languages. | 1..\* | The primary aim of the PRISMA study was to investigate the potential value of risk-tailored versus traditional breast cancer screening protocols in the Netherlands. Data collection took place between 2014-2019, resulting in ∼67,000 mammograms, ∼38,000 surveys, ∼10,000 blood samples and ∼600 saliva samples. |
| [issued](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/issued/) | Date of formal issuance (e.g., publication) of the resource. | `dct:issued` | `xsd:dateTime` | The date and time when the dataset was first issued. | 1..1 | 2024-06-04T13:36:10.246Z |
| [identifier](http://purl.org/dc/terms/identifier) | A unique identifier of the resource being described or catalogued. | `dct:identifier` | `xsd:string` | The main globally unique and persistent identifier of the dataset. Recommended practice is to identify the dataset by means of a string conforming to an identification system such as Digital Object Identifier (DOI). | 1..1 | https://doi.org/10.34894/ZLOYOJ |
| [modified](http://purl.org/dc/terms/modified) | Most recent date on which the catalog entry was changed, updated or modified. | `dct:modified` | `xsd:dateTime` | The value indicates a change to the actual dataset, not a change to the catalog record. An absent value may indicate that the resource has never changed after its initial publication, or that the date of last modification is not known, or that the resource is continuously updated. | 1..1 | 2024-06-04T13:36:10.246Z |
| [publisher](http://purl.org/dc/terms/publisher) | The entity responsible for making the resource available. | `dct:publisher` | `foaf:Agent` | The organization that published the dataset (e.g. the specific UMC in question). Can differ from catalogue publisher. | 1..\* | Radboud University Medical Center; identifier https://ror.org/05wg1m734 (see foaf: Agent) |
| [theme](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme) | A main category of the resource. A resource can have multiple themes. | `dcat:theme` | `IRI` | Consists of 1 or more IRIs (links) separated by commas. When set, it specifies relevant ontology concepts that classify the dataset. Typically, these can be looked up using the Ontology Lookup Service (OLS) or Bioportal | 1..\* | http://publications.europa.eu/resource/authority/data-theme/HEAL |
| [title](http://purl.org/dc/terms/title) | A name given to the record. | `dct:title` | `rdfs:Literal` | A name given to the Dataset. This property can be repeated for providing names in parallel languages. | 1..\* | Questionnaire data of the Personalised RISk-based MAmmascreening Study (PRISMA) |
| [license](http://purl.org/dc/terms/license) | A legal document under which the resource is made available. | `dct:license` | `IRI` | This should contain a URL that provides details regarding the license that is applicable to this dataset (open data commons, data access policy link etc.) | 1..1 | NA  |

#### Recommended Properties
  
| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- |   
| [distribution](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution) | An available distribution of the dataset. | `dcat:distribution` | `dcat:Distribution` | Use this property to point to the distribution of this dataset when a distribution is available. | 0..\* | NA  |
| [type](http://purl.org/dc/terms/type) | The nature or genre of the resource. | `dct:type` | `IRI` | The value SHOULD be taken from a well governed and broadly recognised controlled vocabulary, such as [DCMI Type vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#DCMIType) | 0..\* | http://purl.org/dc/dcmitype/MovingImage |
| [version](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version) | The version indicator (name or identifier) of a resource. | `dcat:version` | `rdfs:Literal` | NA  | 0..\* | NA  |
| [in series](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_in_series) | A dataset series of which the dataset is part. | `dcat:inSeries` | `dcat:DatasetSeries` | NA  | 0..\* | NA  |

### [Data Service](http://www.w3.org/ns/dcat#DataService)
---------------------------------------------------------------------------------------------

A collection of operations that provides access to one or more datasets or data processing functions.

#### Mandatory Properties
  
| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | 
| [end point URL](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_url) | The root location or primary endpoint of the service (a Web-resolvable IRI). | `dcat:endPointURL` | `IRI` | NA  | 1..\* |
| [title](http://purl.org/dc/terms/title) | A name given to the distribution. | `dct:title` | `rdfs:Literal` | NA  | 1..\* |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- |  
| [end point description](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_description) | A description of the services available via the end-points, including their operations, parameters etc. | `dcat:endpointDescription` | `rdfs:Literal` | An endpoint description may be expressed in a machine-readable form, such as an OpenAPI (Swagger) description \[[OpenAPI](https://www.w3.org/TR/vocab-dcat-3/#bib-openapi)\], an OGC `GetCapabilities` response \[[WFS](https://www.w3.org/TR/vocab-dcat-3/#bib-wfs)\], \[[ISO-19142](https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19142)\], \[[WMS](https://www.w3.org/TR/vocab-dcat-3/#bib-wms)\], \[[ISO-19128](https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19128)\], a SPARQL Service Description \[[SPARQL11-SERVICE-DESCRIPTION](https://www.w3.org/TR/vocab-dcat-3/#bib-sparql11-service-description)\], an \[[OpenSearch](https://www.w3.org/TR/vocab-dcat-3/#bib-opensearch)\] or \[[WSDL20](https://www.w3.org/TR/vocab-dcat-3/#bib-wsdl20)\] document, a Hydra API description \[[HYDRA](https://www.w3.org/TR/vocab-dcat-3/#bib-hydra)\], else in text or some other informal mode if a formal representation is not possible. | 0..\* |
| [serves dataset](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_serves_dataset) | A collection of data that this data service can distribute. | `dcat:servesDataset` | `dcat:Dataset` | NA  | 0..\* |

### [Distribution](http://www.w3.org/ns/dcat#Distribution)

An available distribution of the dataset.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** | **Example** |
| --- | --- | --- | --- | --- | --- | --- |  
| [title](http://purl.org/dc/terms/title) | A name given to the distribution. | `dct:title` | `rdfs:Literal` | the name of the dataset in combination with the format of the distribution can be used | 1..\* | CSV-distribution of the questionnaire data of the Personalised RISk-based MAmmascreening Study (PRISMA) |
| [access URL](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_url) | A URL of the resource that gives access to a distribution of the dataset. E.g., landing page, feed, SPARQL endpoint. | `dcat:accessURL` | `IRI` | This property contains a URL that gives access to a Distribution of the Dataset. The resource at the access URL may contain information about how to get the Dataset. | 1..\* | NA  |
| [media type](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_media_type) | The media type of the distribution as defined by IANA \[[IANA-MEDIA-TYPES](https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types)\]. | `dcat:mediaType` | `IRI` | This property _SHOULD_ be used when the media type of the distribution is defined in IANA \[[IANA-MEDIA-TYPES](https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types)\], otherwise `dcterms:format` _MAY_ be used with different values. | 1..\* | https://www.iana.org/assignments/media-types/text/csv |
| [description](http://purl.org/dc/terms/description) | A free-text account of the distribution. | `dct:description` | `rdfs:Literal` | NA  | 1..\* | NA  |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- |
| [access service](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_service) | A data service that gives access to the distribution of the dataset | `dcat:accessService` | `dcat:DataService` | `dcat:accessService` _SHOULD_ be used to link to a description of a `dcat:DataService` that can provide access to this distribution. | 0..\* |
| [download URL](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_download_url) | The URL of the downloadable file in a given format. E.g., CSV file or RDF file. The format is indicated by the distribution's `dcterms:format` and/or `dcat:mediaType` | `dcat:downloadURL` | `IRI` | NA  | 0..\* |

### [Agent](http://xmlns.com/foaf/spec/#term_Agent)

An entity that is associated with catalog and/or Datasets. Agent can be individuals or organisations, If the Agent is an organisation, the use of the Organization Ontology is recommended.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- |   
| [name](http://xmlns.com/foaf/spec/#term_name) | A name for some thing. | `foaf:name` | `xsd:string` | This property contains a name of the agent. This property can be repeated for different versions of the name (e.g. the name in different languages) | 1..1 |
| [identifier](http://purl.org/dc/terms/identifier) | A unique identifier of the resource being described or catalog. | `dct:identifier` | `rdfs:Literal` |   A unique identifier of a person or organisation being described, like [ORCID](https://orcid.org) for a researcher or [ROR](https://ror.org) for an organization.  | 1..1 |

#### Recommended Properties

No recommended properties are identified for this release.

### Kind

Contact information of the contact point for Dataset and DatasetSeries.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | 
| [formatted name](https://w3.org/TR/vcard-rdf/#d4e891) | The full name of the object | `vcard:fn` | `xsd:string` | NA  | 1   |
| [has email](https://www.w3.org/TR/vcard-rdf/#d4e183) | To specify the electronic mail address for communication with the object | `vcard:hasEmail` | `IRI` | NA  | 1   |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | 
| [has url](https://www.w3.org/TR/vcard-rdf/#d4e183) | To specify a URL associated with the contact point | `vcard:hasURL` | `IRI` | NA  | 0..n |

### Cataloged Resource

All things described by RDF are called _resources_, and they are instances of the class `dcat:Resource`. This is the class of everything. All other classes are [subclasses](https://www.w3.org/TR/rdf12-schema/#def-subclass) of this class. To read more, go to

## Further Information

### Feedback - Git Issues

If you wish to extend the model, such as with Resource, and/or create a new concept, please open an issue [here](https://github.com/Health-RI/health-ri-metadata/issues) and provide a clear explanation for the extension. Assign the issue to either ‘**brunasv’ or ‘xiaofengleo’**, and we will work with you to implement the addition in the next release.

### Model extension

Within DCAT and DCAT-AP, the term "resource" generally encompasses all objects that can be described using [RDF](https://www.w3.org/RDF/). However, there are specific categories and attributes used to indicate the different types of resources:

*   `dcat:Dataset` is a type of `dcat:Resource` representing a collection of data
    
*   `dcat:Distribution` is a type of `dcat:Resourcee` representing an available form or representation of a dataset.
    
*   `dcat:Catalog` is a type of `dcat:Resource` representing a collection of datasets.
    
*   `dcat:DataService` , introduced in DCAT version 2, is a type of Resource representing a service for accessing data.
    

In DCAT and DCAT-AP, the vocabulary is focused on datasets. Nonetheless, users may need to portray a variety of resources specific to certain domains, like biobanks or patient registries. In such cases, we propose potential scenarios for modifying or augmenting DCAT to accurately depict your resource type:

*   **Use** `dcat:Resource` **directly**: If the asset you are dealing with is not in line with the `dcat:Dataset` definition, you can use the broader term `dcat:Resource`. This term allows you to represent almost any type of asset. However, this approach may not be completely clear for users who are trying to understand the essence of the asset. We can de define the asset type further with specific vocabularies over time.
    
*   **Expand with Personalised Classes**: If there is a need to represent specific resources, such as biobanks or patient registries, it may be beneficial to supplement the foundational DCAT vocabulary with custom classes. For example:
    

`:Collection a rdfs:Class ;`

`rdfs:subClassOf dcat:Resource .`

and

`:PatientRegistry a rdfs:Class ;`

`rdfs:subClassOf dcat:Dataset .`

When creating custom classes, it is essential to provide detailed metadata for each type of resource. This will enable users and systems to distinguish between them and comprehend their subtle differences. For instance, consider the distinction between a collection and a dataset. Therefore, it is crucial to provide specific and unambiguous information to ensure complete understanding.

### Notes on Alignment

To create the current core metadata schema, we examined existing metadata from the [COVID-19 national portal](https://covid19initiatives.health-ri.nl/), metadata schema provided by Health-RI nodes (e.g., [ABC metadata](https://github.com/AmsterdamUMC/ABC-metadata-project)), and standards used in portals across Europe and beyond (e.g., W3C, DCAT, DCAT-AP). With the help of metadata specialists, we mapped their classes and properties and decided to reuse DCAT and DCAT-AP for implementation. The Core metadata schema includes DCAT v3 and selected DCAT-AP mandatory classes, ensuring compatibility with international catalogs. DCAT-AP covers the identified requirements for exchanging information about datasets and services in Europe. Alignment with DCAT NL is under development.

### Implementation

The model is part of the requirements to onboard to the Health-RI catalog, and documentation for users is not yet released. However, users can start the onboarding process by publishing their metadata according to this schema in a FAIR Data Point. To start:
- read the explanation of all classes and properties in the [Core Metadata Schema Specification](https://github.com/Health-RI/health-ri-metadata) 
- collect and map your metadata instances to the model using this [example metadata collection sheet](https://github.com/Health-RI/health-ri-metadata/blob/master/Implementation/metadata%20collection%20sheet%20template.xlsx)
- import the provided [shacl](https://github.com/Health-RI/health-ri-metadata/tree/master/Formalisation(shacl)/Core/PiecesShape) to your FDP (note: tutorial on how to configure your FDP for Health-RI's requirements is being developed)
- For a complete overview of the onboarding process, users can look for the [Metadata Onboarding on the National Catalogue](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/279150593) with details on how to implement and connect to it.
- For an overview of the mapping pipeline visit the [Mapping Pipeline](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/290291734).    
- With any further questions or comments please contact Health-RI via the [Health-RI Servicedesk](https://www.health-ri.nl/health-ri-servicedesk) or via [servicedesk@health-ri.nl](mailto:servicedesk@health-ri.nl "mailto:servicedesk@health-ri.nl")
