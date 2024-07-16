# Core Metadata Schema Specification

### Latest published version
Plateau 1: [https://github.com/Health-RI/health-ri-metadata/tree/master/Formalisation(shacl)/Core/PiecesShape](https://github.com/Health-RI/health-ri-metadata/tree/master/Formalisation(shacl)/Core/PiecesShape)

### Purpose and audience

This repository outlines the Core Metadata Schema, detailing the classes and entities involved and offering usage notes for developers. It addresses the schema's design and application but excludes discussion on the national catalog and its onboarding process. It aims at a technical audience tasked with implementing the metadata schema and stakeholders interested in a detailed understanding of the core schema.

* [Introduction](#Introduction)
    * [Scope](#Scope)
    * [Mandatory and Recommended](#Mandatory-and-Recommended)
    * [Terminology](#Terminology)
    * [Used Prefixes](#Used-Prefixes)
    * [Overview and Diagram](#Overview-and-Diagram)
* [Main Classes](#Main-Classes)
    * [Mandatory Classes](#Mandatory-Classes)
    * [Recommended Classes](#Recommended-Classes)
    * [Abstract Class](#Abstract-Class)
* [Main Properties per Class](#Main-Properties-per-Class)
    * [Catalog](#Catalog)
    * [Dataset](#Dataset)
    * [Dataset Series](#Dataset-Series)
    * [Data Service](#Data-Service)
    * [Distribution](#Distribution)
    * [Agent](#Agent)
    * [Project](#Project)
    * [Kind](#Kind)
    * [Cataloged Resource](#Cataloged-Resource)
* [Feedback, Support, Extension and Implementation](#Further-Information)

Introduction
============

Scope
-----

To make it easier to share, find and reuse data, the Health-RI nodes decided to list resources in a national directory that can be accessed internationally. They all agreed on what basic information should be included, and that the catalog should be interoperable with other EU portals, which led to the creation of the Core Metadata Schema.

This schema describes the minimum amount of information that should be used to describe resources across Health-RI nodes through the national directory, which is in line with what Plateau 1 offers. The schema can be changed or extended to meet the needs of different areas, and new versions will be released in the future.

Mandatory and Recommended
-------------------------

Following the DCAT-AP specification, we categorize components into 'mandatory' and 'recommended' classes and properties. A potential third category, 'Optional,' may be introduced in the future.

In the context of data exchange:

*   **Mandatory** Class: Senders **MUST** provide information about instances of the class; Receivers MUST process information about instances of the class.
    
*   **Recommended** Class: Senders **SHOULD** provide information about instances of the class if available; Receivers MUST process information about instances of the class.
    
*   **Optional** Class: Senders **MAY** provide the information but are not obliged to do so; Receivers MUST process information about instances of the class.
    
*   Mandatory property: Senders MUST provide the information for that property; Receivers MUST process the information for that property.
    
*   Recommended property: Senders SHOULD provide the information if available; Receivers MUST process the information for that property.
    
*   Optional property: Senders MAY provide the information but are not obliged to do so; Receivers MUST process the information for that property.
    

Terminology
-----------

According to DCAT-AP:

*   An **Application Profile** defines the mandatory, recommended, and optional components for a specific use case by leveraging terminology from foundational standards. Additionally, it suggests standardized vocabularies to maintain consistency in the use of terms and data.
    
*   A **Dataset** is a self-contained set of data produced by a specific organization, which can be accessed or downloaded for various uses. A **Data Portal** is an online platform that offers a catalog of datasets and tools to help users locate and utilize these datasets effectively.
    

Used Prefixes
-------------

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:87px">
      <col style="width:266px">
      <col style="width:177px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" style="background-color:#005a9c" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="125" data-cell-background="#005a9c" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="3167"><span data-renderer-mark="true" data-text-custom-color="#ffffff" class="fabric-text-color-mark" style="--custom-palette-color:var(--ds-text-inverse, #FFFFFF)">Prefix</span></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" style="background-color:#005a9c" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="381" data-cell-background="#005a9c" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="3177"><span data-renderer-mark="true" data-text-custom-color="#ffffff" class="fabric-text-color-mark" style="--custom-palette-color:var(--ds-text-inverse, #FFFFFF)">Namespace IRI</span></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" style="background-color:#005a9c" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="253" data-cell-background="#005a9c" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="3194"><span data-renderer-mark="true" data-text-custom-color="#ffffff" class="fabric-text-color-mark" style="--custom-palette-color:var(--ds-text-inverse, #FFFFFF)">Source</span></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3206"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3214"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://www.w3.org/ns/dcat#</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3244">[<a data-testid="link-with-safety" href="https://w3c.github.io/dxwg/dcat/#bib-vocab-dcat" title="https://w3c.github.io/dxwg/dcat/#bib-vocab-dcat" data-renderer-mark="true" class="cc-1rn59kg">VOCAB-DCAT</a>]</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3262"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3269"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://purl.org/dc/terms/</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3298">[<a data-testid="link-with-safety" href="https://w3c.github.io/dxwg/dcat/#bib-dcterms" title="https://w3c.github.io/dxwg/dcat/#bib-dcterms" data-renderer-mark="true" class="cc-1rn59kg">DCT</a>]</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3309"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3317"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://xmlns.com/foaf/0.1/</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3347">[<a data-testid="link-with-safety" href="https://w3c.github.io/dxwg/dcat/#bib-foaf" title="https://w3c.github.io/dxwg/dcat/#bib-foaf" data-renderer-mark="true" class="cc-1rn59kg">FOAF</a>]</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3359"><code class="code cc-1o5d2cw" data-renderer-mark="true">owl</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3366"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://www.w3.org/2002/07/owl#</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3400">[<a data-testid="link-with-safety" href="https://w3c.github.io/dxwg/dcat/#bib-owl2-syntax" title="https://w3c.github.io/dxwg/dcat/#bib-owl2-syntax" data-renderer-mark="true" class="cc-1rn59kg">OWL2-SYNTAX</a>]</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3419"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdf</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3426"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://www.w3.org/1999/02/22-rdf-syntax-ns#</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3473">[<a data-testid="link-with-safety" href="https://w3c.github.io/dxwg/dcat/#bib-rdf-syntax-grammar" title="https://w3c.github.io/dxwg/dcat/#bib-rdf-syntax-grammar" data-renderer-mark="true" class="cc-1rn59kg">RDF-SYNTAX-GRAMMAR</a>]</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3499"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3507"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://www.w3.org/2000/01/rdf-schema#</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3548">[<a data-testid="link-with-safety" href="https://w3c.github.io/dxwg/dcat/#bib-rdf-schema" title="https://w3c.github.io/dxwg/dcat/#bib-rdf-schema" data-renderer-mark="true" class="cc-1rn59kg">RDF-SCHEMA</a>]</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3566"><code class="code cc-1o5d2cw" data-renderer-mark="true">skos</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3574"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://www.w3.org/2004/02/skos/core#</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3614">[<a data-testid="link-with-safety" href="https://w3c.github.io/dxwg/dcat/#bib-skos-reference" title="https://w3c.github.io/dxwg/dcat/#bib-skos-reference" data-renderer-mark="true" class="cc-1rn59kg">SKOS-REFERENCE</a>]</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3636"><code class="code cc-1o5d2cw" data-renderer-mark="true">time</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3644"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://www.w3.org/2006/time#</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3676">[<a data-testid="link-with-safety" href="https://w3c.github.io/dxwg/dcat/#bib-owl-time" title="https://w3c.github.io/dxwg/dcat/#bib-owl-time" data-renderer-mark="true" class="cc-1rn59kg">OWL-TIME</a>]</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3692"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3699"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://www.w3.org/2001/XMLSchema#</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3736">[<a data-testid="link-with-safety" href="https://w3c.github.io/dxwg/dcat/#bib-xmlschema11-2" title="https://w3c.github.io/dxwg/dcat/#bib-xmlschema11-2" data-renderer-mark="true" class="cc-1rn59kg">XMLSCHEMA11-2</a>]</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="125">
            <p data-renderer-start-pos="3757"><code class="code cc-1o5d2cw" data-renderer-mark="true">vcard</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="381">
            <p data-renderer-start-pos="3766"><code class="code cc-1o5d2cw" data-renderer-mark="true">http://www.w3.org/2006/vcard/ns#</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="253">
            <p data-renderer-start-pos="3802">[<a data-testid="link-with-safety" href="https://www.w3.org/TR/vcard-rdf/" title="https://www.w3.org/TR/vcard-rdf/" data-renderer-mark="true" class="cc-1rn59kg">VCARD</a>]</p>
         </td>
      </tr>
   </tbody>
</table>

Overview and Diagram
--------------------

An overview of the Metadata schema core is presented in the [UML](https://www.omg.org/spec/UML "https://www.omg.org/spec/UML") diagram depicted below. The UML showcases the primary classes (entities), excluding the detailed definitions such as rdfs:label rdfs:comment. Each block denotes a class and comprises a list of its attributes (properties). If a class is connected to another class by a closed arrow, indicating that it inherits all properties from the other class. For example, `dcat:DatasetSeries` inherits from `dcat:Dataset` which inherits from `dcat:Resource`. The other arrows, represent relations and contain the type of relation, such as `dcat:Dataset` connects to a `dcat:DatasetSeries` via the predicate `dcat:inSeries`, and include the cardinality, such as `dcat:Dataset` can be connected via `dcat:inSeries` to zero or more `dcat:DatasetSeries`.

- HRI core metadata schema diagram (plateau 1):
<img src="https://github.com/Health-RI/health-ri-metadata/blob/master/Images/1.0_plateau1/HRICoreSchemaReleasePlateau1.jpg" alt="diagram" width=1080 height=560 title="diagram">

Main Classes
============

Mandatory Classes
-----------------

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:84px">
      <col style="width:143px">
      <col style="width:196px">
      <col style="width:108px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="120" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="4674"><strong data-renderer-mark="true">Class name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="205" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="4688"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="280" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="4702"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="155" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="4716"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="120">
            <p data-renderer-start-pos="4725"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#dataset" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#dataset" data-renderer-mark="true" class="cc-1rn59kg">Dataset</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="205">
            <p data-renderer-start-pos="4736">A resource type.<br>A collection of data, published or curated by a single agent, and available for access or download in one or more representations.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="280">
            <p data-renderer-start-pos="4887">Used to describe one or more datasets. This describes details about the dataset(s). However, a single dataset can have different ways in which they are made available to potential users. How the data in a dataset can be accessed is defined in the Distribution.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="155">
            <p data-renderer-start-pos="5151"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Dataset</code></p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="120">
            <p data-renderer-start-pos="5169"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#catalog" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#catalog" data-renderer-mark="true" class="cc-1rn59kg">Catalog</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="205">
            <p data-renderer-start-pos="5180">A catalog that is listed in the National catalog.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="280">
            <p data-renderer-start-pos="5233">Used to describe a bundle of datasets, data services, biobanks, patient registries, or guidelines together under a single title.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="155">
            <p data-renderer-start-pos="5365"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Catalog</code></p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="120">
            <p data-renderer-start-pos="5383"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#agent" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#agent" data-renderer-mark="true" class="cc-1rn59kg">Agent</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="205">
            <p data-renderer-start-pos="5392">An entity that is associated with catalog and/or Datasets.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="280">
            <p data-renderer-start-pos="5454"><mark id="b3bb2200-b0c5-43df-a9ad-23e061a55fa2" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="b3bb2200-b0c5-43df-a9ad-23e061a55fa2" class="cc-1rnxqbw">If the Agent is an organisation, the use of the </mark><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-org/" title="https://www.w3.org/TR/vocab-org/" data-renderer-mark="true" class="cc-1rn59kg"><mark id="b3bb2200-b0c5-43df-a9ad-23e061a55fa2" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="b3bb2200-b0c5-43df-a9ad-23e061a55fa2" class="cc-1rnxqbw"><mark id="5f510486-53fc-4713-9f5d-22440083f4c8" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="5f510486-53fc-4713-9f5d-22440083f4c8" class="cc-1rnxqbw">Organization Ontology</mark></mark></a><a data-testid="link-with-safety" href="http://www.w3.org/TR/2013/CR-vocab-org-20130625/" title="http://www.w3.org/TR/2013/CR-vocab-org-20130625/" data-renderer-mark="true" class="cc-1rn59kg"><mark id="b3bb2200-b0c5-43df-a9ad-23e061a55fa2" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="b3bb2200-b0c5-43df-a9ad-23e061a55fa2" class="cc-1rnxqbw"> </mark></a><mark id="b3bb2200-b0c5-43df-a9ad-23e061a55fa2" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="b3bb2200-b0c5-43df-a9ad-23e061a55fa2" class="cc-1rnxqbw">is recommended.</mark></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="155">
            <p data-renderer-start-pos="5545"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:Agent</code></p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="120">
            <p data-renderer-start-pos="5561"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#cataloged-resource" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#cataloged-resource" data-renderer-mark="true" class="cc-1rn59kg">Cataloged Resource</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="205">
            <p data-renderer-start-pos="5583">Resource published or curated by a single agent.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="280">
            <p data-renderer-start-pos="5635">This is an abstract class, we do not use this class, instead we use specifications of it (e.g. Dataset). This is mainly for a high level grouping and the reuse of properties.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="155">
            <p data-renderer-start-pos="5813"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Resource</code></p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="120">
            <p data-renderer-start-pos="5832"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Kind" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Kind" data-renderer-mark="true" class="cc-1rn59kg">Kind</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="205">
            <p data-renderer-start-pos="5840">A description following the vCard specification, e.g. to provide telephone number and e-mail address for a contact point.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="280">
            <p data-renderer-start-pos="5965">Used to describe contact information for Dataset and DatasetSeries.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="155">
            <p data-renderer-start-pos="6036"><code class="code cc-1o5d2cw" data-renderer-mark="true">vcard:Kind</code></p>
         </td>
      </tr>
   </tbody>
</table>

Recommended Classes
-------------------

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:132px">
      <col style="width:132px">
      <col style="width:132px">
      <col style="width:132px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="6075"><strong data-renderer-mark="true">Class name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="6089"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="6103"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="6117"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="6126"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Distribution" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Distribution" data-renderer-mark="true" class="cc-1rn59kg">Distribution</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="6142">An available distribution of the dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="6187">Used to describe the different ways that a single dataset can be made available in. I.e., it can be downloaded or it can be accessed online in one or more distributions (e.g. one in a downloadable .csv file, another file with an access or query webpage)</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="6444"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Distribution</code></p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="6467"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Dataset-Series" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Dataset-Series" data-renderer-mark="true" class="cc-1rn59kg">Dataset Series</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="6485">A resource type.</p>
            <p data-renderer-start-pos="6504">Dataset series are defined in [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19115" title="https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19115" data-renderer-mark="true" class="cc-1rn59kg">ISO-19115</a>] as a collection of datasets […] sharing common characteristics. However, their use is not limited to geospatial data, although in other domains they can be named differently (e.g., time series, data slices) and defined more or less strictly (see, e.g., the notion of "dataset slice" in <a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-vocab-data-cube" title="https://www.w3.org/TR/vocab-dcat-3/#bib-vocab-data-cube" data-renderer-mark="true" class="cc-1rn59kg">VOCAB-DATA-CUBE</a>).</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="6853">With Dataset Series we refer to data, somehow interrelated, that are published separately. An example is budget data split by year and/or country, instead of being made available in a single dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7056"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:DatasetSeries</code></p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7080"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Data-Service" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Data-Service" data-renderer-mark="true" class="cc-1rn59kg">Data Service</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7096">A Resource type.<br>A collection of operations that provides access to one or more datasets or data processing functions.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7218">The kind of service can be indicated using the <code class="code cc-1o5d2cw" data-renderer-mark="true">dcterms:type</code> property. Its value may be taken from a controlled vocabulary that should be defined in the community.</p>
            <p data-renderer-start-pos="7383"><em data-renderer-mark="true"><mark id="c86f74c7-67b8-4933-ab00-f27e8dc6ba04" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="c86f74c7-67b8-4933-ab00-f27e8dc6ba04" class="cc-1rnxqbw">DRAFT EXAMPLE:</mark></em></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7402"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:DataService</code></p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7424"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Project" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Project" data-renderer-mark="true" class="cc-1rn59kg">Project</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7435">A project (a collective endeavour of some kind).</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7487">Used to describe a project that is connected to one or more datasets. A resource type</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7576"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:Project</code></p>
         </td>
      </tr>
   </tbody>
</table>

_Abstract Class_
----------------

_**Cataloged Resource**_ is a generic concept from the DCAT vocabulary, that is rarely used directly, but indirectly through its extensions. We recommend avoiding using `dcat:Resource` directly for your document and requesting a model extension or update, in case the type/class you need is not in this schema.

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:132px">
      <col style="width:132px">
      <col style="width:132px">
      <col style="width:132px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="7919"><strong data-renderer-mark="true">Class name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="7933"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="7947"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="7961"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7970"><a data-testid="link-with-safety" href="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Cataloged-Resource" title="https://github.com/Health-RI/health-ri-metadata?tab=readme-ov-file#Cataloged-Resource" data-renderer-mark="true" class="cc-1rn59kg"><em data-renderer-mark="true">Cataloged Resource</em></a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="7992"><code class="code cc-1o5d2cw" data-renderer-mark="true">The class resource, everything.</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8027">This class is for grouping and class hierarchy relation purposes.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8096"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Resource</code></p>
         </td>
      </tr>
   </tbody>
</table>

Main Properties per Class
=========================

[Catalog](https://www.w3.org/TR/vocab-dcat-3/#Class:Catalog "https://www.w3.org/TR/vocab-dcat-3/#Class:Catalog")
----------------------------------------------------------------------------------------------------------------

A curated collection of metadata about resources. A web-based data catalog is typically represented as a single instance of this class.

### Mandatory Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="8314"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="8331"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="8345"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="8352"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="8366"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="8380"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8397"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/title" title="http://purl.org/dc/terms/title" data-renderer-mark="true" class="cc-1rn59kg">title</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8406">A name given to the resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8439"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:title</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8452"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8468">The name of the catalog. This is a required field and needs to be unique.&nbsp;</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8546">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8556"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/description" title="http://purl.org/dc/terms/description" data-renderer-mark="true" class="cc-1rn59kg">description</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8571">A free-text account of the record.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8609"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:description</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8628"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8644">A brief description of the catalog. It can consist of multiple strings. For example, this catalog describes breast cancer imaging datasets.&nbsp;</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8788">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8798"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/publisher" title="http://purl.org/dc/terms/publisher" data-renderer-mark="true" class="cc-1rn59kg">publisher</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8811">The entity responsible for making the resource available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8872"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:publisher</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8889"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:Agent</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8903">The organisation or a person that has published the catalog</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="8967">1..*</p>
         </td>
      </tr>
   </tbody>
</table>

### Recommended Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9003"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9020"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9034"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9041"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9055"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9069"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9086"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_catalog" title="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_catalog" data-renderer-mark="true" class="cc-1rn59kg">catalog</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9097">A catalog that is listed in the catalog.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9141"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:catalog</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9157"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Catalog</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9173">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9179">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9189"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset" title="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset" data-renderer-mark="true" class="cc-1rn59kg">dataset</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9200">relates every catalog to its containing datasets.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9253"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:dataset</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9269"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Dataset</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9285">The connection to the one or more datasets that this catalog describes.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9361">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9371"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_service" title="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_service" data-renderer-mark="true" class="cc-1rn59kg">service</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9382">A service that is listed in the catalog.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9426"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:service</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9442"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:DataService</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9462">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="9468">0..*</p>
         </td>
      </tr>
   </tbody>
</table>

[Dataset](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset "https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset")
----------------------------------------------------------------------------------------------------------------

A collection of data, published or curated by a single agent, and available for access or download in one or more representations.

### Mandatory Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:81px">
      <col style="width:98px">
      <col style="width:81px">
      <col style="width:81px">
      <col style="width:132px">
      <col style="width:56px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="116" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9643"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="140" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9660"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="117" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9674"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="117" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9681"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="189" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9695"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="81" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="9709"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="9726"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point" title="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point" data-renderer-mark="true" class="cc-1rn59kg">contact point</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="9743">Relevant contact information for the catalog resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="9801"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:contactPoint</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="9822"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="0176add6-a7da-4acd-8aeb-48f40f98e7e5" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="0176add6-a7da-4acd-8aeb-48f40f98e7e5" class="cc-1rnxqbw">vcard:Kind</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="9836">Contact information that can be used, for example, for sending requests to further information or access to the Dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="9960">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="9970"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/creator" title="http://purl.org/dc/terms/creator" data-renderer-mark="true" class="cc-1rn59kg">creator</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="9981">The entity responsible for producing the resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10035"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:creator</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10050"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:Agent</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="10064">An agent (person or organisation) responsible for producing the dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="10140">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="10150"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/description" title="http://purl.org/dc/terms/description" data-renderer-mark="true" class="cc-1rn59kg">description</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="10165">A free-text account of the record</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10202"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:description</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10221"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="294d7e15-8d65-4c8e-ab26-ca4f368e9ce7" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="294d7e15-8d65-4c8e-ab26-ca4f368e9ce7" class="cc-1rnxqbw">rdfs:Literal</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="10237">A free-text description of the Dataset. This property can be repeated for parallel language versions of the description.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="10361">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="10371"><a data-testid="link-with-safety" href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/issued/" title="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/issued/" data-renderer-mark="true" class="cc-1rn59kg"><mark id="0efbfd9d-fe09-4886-ab68-ab75e464a8c4" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="0efbfd9d-fe09-4886-ab68-ab75e464a8c4" class="cc-1rnxqbw">issued</mark></a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="10381">Date of formal issuance (e.g., publication) of the resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10445"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:issued</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10459"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:dateTime</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="10475">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="10481"><mark id="3a772386-3677-4434-a22c-ff5ad7eac024" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="3a772386-3677-4434-a22c-ff5ad7eac024" class="cc-1rnxqbw">1..1</mark></p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="10491"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/identifier" title="http://purl.org/dc/terms/identifier" data-renderer-mark="true" class="cc-1rn59kg">identifier</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="10505">A unique identifier of the resource being described or catalogued.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10575"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:identifier</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10593"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:string</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="10607">The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the catalog.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="10718">1..1</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="10728"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/modified" title="http://purl.org/dc/terms/modified" data-renderer-mark="true" class="cc-1rn59kg">modified</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="10740">Most recent date on which the catalog entry was changed, updated or modified.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10821"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:modified</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="10837"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:dateTime</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="10853">The most recent date on which the Dataset was changed or modified.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="10923">1..1</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="10933"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/publisher" title="http://purl.org/dc/terms/publisher" data-renderer-mark="true" class="cc-1rn59kg">publisher</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="10946">The entity responsible for making the resource available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11007"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:publisher</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11024"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:Agent</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="11038">An agent (organisation or person) responsible for making the Dataset available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="11121">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="11131"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme" title="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme" data-renderer-mark="true" class="cc-1rn59kg"><mark id="06439b7c-fc96-43ef-8b56-7b268a042f4e" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="06439b7c-fc96-43ef-8b56-7b268a042f4e" class="cc-1rnxqbw">theme</mark></a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="11140">A main category of the resource. A resource can have multiple themes.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11213"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="e8143c9b-1da6-41c9-9616-a6696a617c44" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="e8143c9b-1da6-41c9-9616-a6696a617c44" class="cc-1rnxqbw">dcat:theme</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11227"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="38e24c59-4fbd-49cf-9835-5e90cdeea081" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="38e24c59-4fbd-49cf-9835-5e90cdeea081" class="cc-1rnxqbw">IRI</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="11234">It consists of 1 or more IRIs (links) separated by commas. <mark id="95b511b2-e9b7-4a7c-86e4-83785c313d80" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="95b511b2-e9b7-4a7c-86e4-83785c313d80" class="cc-1rnxqbw">When set, it specifies relevant ontology concepts that classify the dataset. </mark>Typically, these can be looked up using the <a data-testid="link-with-safety" href="https://www.ebi.ac.uk/ols/index" title="https://www.ebi.ac.uk/ols/index" data-renderer-mark="true" class="cc-1rn59kg"><u data-renderer-mark="true">Ontology Lookup Service (OLS)</u></a> or <a data-testid="link-with-safety" href="https://bioportal.bioontology.org/" title="https://bioportal.bioontology.org/" data-renderer-mark="true" class="cc-1rn59kg">Bioportal</a>.&nbsp;&nbsp;</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="11463">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="11473"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/title" title="http://purl.org/dc/terms/title" data-renderer-mark="true" class="cc-1rn59kg">title</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="11482">A name given to the record.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11513"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:title</code></p>
            <p data-renderer-start-pos="11524">&nbsp;</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11528"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="11544">A name given to the Dataset. This property can be repeated for providing names in parallel languages.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="11649">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="11821"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/license" title="http://purl.org/dc/terms/license" data-renderer-mark="true" class="cc-1rn59kg">license</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="11832">A legal document under which the resource is made available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11896"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:license</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11911"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="1065c46b-1c43-414a-af11-e91cd979cf1a" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="1065c46b-1c43-414a-af11-e91cd979cf1a" class="cc-1rnxqbw">IRI</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="11918">This should contain a URL that provides details regarding the license that is applicable to this dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="12027">1..1</p>
         </td>
      </tr>
   </tbody>
</table>

### Recommended Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12063"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12080"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12094"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12101"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12115"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12129"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12146"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution" title="https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution" data-renderer-mark="true" class="cc-1rn59kg">distribution</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12162">An available distribution of the dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12207"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:distribution</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12228"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Distribution</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12249">Use this property to point to the distribution of this dataset when a distribution is available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12349">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12359"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/relation" title="http://purl.org/dc/terms/relation" data-renderer-mark="true" class="cc-1rn59kg">relation</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12371">defines a relation</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12393"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:relation</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12409"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="cd08a08d-1fa9-4a83-89ba-5cfb31743055" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="cd08a08d-1fa9-4a83-89ba-5cfb31743055" class="cc-1rnxqbw">foaf:Project</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12425">Use this property to point to the related project of this dataset when a project is available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12523">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="11659"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/type" title="http://purl.org/dc/terms/type" data-renderer-mark="true" class="cc-1rn59kg">type</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="11667">The nature or genre of the resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11707"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:type</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="11719"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="84a3e0f7-37ad-4b45-8d81-8b8f4df947e5" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="84a3e0f7-37ad-4b45-8d81-8b8f4df947e5" class="cc-1rnxqbw">IRI</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="11726"><mark id="cf5c6ba1-822a-483f-a7e3-a94ac3b7299e" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="cf5c6ba1-822a-483f-a7e3-a94ac3b7299e" class="cc-1rnxqbw">A type of the Dataset. A recommended controlled vocabulary data-type is foreseen.</mark></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="11811">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12533"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version" title="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version" data-renderer-mark="true" class="cc-1rn59kg">version</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12544">The version indicator (name or identifier) of a resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12605"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="c3ebb829-ad09-4ac4-bd8f-989851c58eed" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="c3ebb829-ad09-4ac4-bd8f-989851c58eed" class="cc-1rnxqbw">dcat:version</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12621"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="e6fb29b0-7c9c-473e-bbc4-e2a7dcbf2273" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="e6fb29b0-7c9c-473e-bbc4-e2a7dcbf2273" class="cc-1rnxqbw">rdfs:Literal</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12637">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12643">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12653"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_in_series" title="https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_in_series" data-renderer-mark="true" class="cc-1rn59kg">in series</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12666">A dataset series of which the dataset is part.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12716"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:inSeries</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12733"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:DatasetSeries</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12755">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="12761">0..*</p>
         </td>
      </tr>
   </tbody>
</table>

[Dataset Series](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series "https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series")
-------------------------------------------------------------------------------------------------------------------------------------

### Mandatory Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:81px">
      <col style="width:98px">
      <col style="width:81px">
      <col style="width:81px">
      <col style="width:132px">
      <col style="width:56px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="116" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12811"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="140" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12828"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="117" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12842"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="117" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12849"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="189" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12863"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="81" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="12877"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="12894"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point" title="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point" data-renderer-mark="true" class="cc-1rn59kg">contact point</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="12911">Relevant contact information for the catalog resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="12969"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:contactPoint</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="12990"><code class="code cc-1o5d2cw" data-renderer-mark="true">vcard:Kind</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="13004">Contact information that can be used, for example, for sending requests to further information or access to the Dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="13128">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="13138"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/creator" title="http://purl.org/dc/terms/creator" data-renderer-mark="true" class="cc-1rn59kg">creator</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="13149">The entity responsible for producing the resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="13203"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:creator</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="13218"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:Agent</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="13232">An agent (person or organisation) responsible for producing the dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="13308">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="13318"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/description" title="http://purl.org/dc/terms/description" data-renderer-mark="true" class="cc-1rn59kg">description</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="13333">A free-text account of the record</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="13370"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:description</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="13389"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="13405">A free-text description of the Dataset. This property can be repeated for parallel language versions of the description.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="13529">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="13539"><a data-testid="link-with-safety" href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/issued/" title="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/issued/" data-renderer-mark="true" class="cc-1rn59kg">issued</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="13549">Date of formal issuance (e.g., publication) of the resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="13613"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:issued</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="13627"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:dateTime</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="13643">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="13649">1..1</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="13659"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/identifier" title="http://purl.org/dc/terms/identifier" data-renderer-mark="true" class="cc-1rn59kg">identifier</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="13673">A unique identifier of the resource being described or catalogued.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="13743"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:identifier</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="13761"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:string</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="13775">The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the catalog.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="13886">1..1</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="13896"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/modified" title="http://purl.org/dc/terms/modified" data-renderer-mark="true" class="cc-1rn59kg">modified</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="13908">Most recent date on which the catalog entry was changed, updated or modified.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="13989"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:modified</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="14005"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:dateTime</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="14021">The most recent date on which the Dataset was changed or modified.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="14091">1..1</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="14101"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/publisher" title="http://purl.org/dc/terms/publisher" data-renderer-mark="true" class="cc-1rn59kg">publisher</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="14114">The entity responsible for making the resource available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="14175"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:publisher</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="14192"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:Agent</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="14206">An agent (organisation or person) responsible for making the Dataset available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="14289">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="14299"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme" title="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme" data-renderer-mark="true" class="cc-1rn59kg">theme</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="14308">A main category of the resource. A resource can have multiple themes.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="14381"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:theme</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="14395"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="435b4949-9472-444e-9408-8d70f26a4186" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="435b4949-9472-444e-9408-8d70f26a4186" class="cc-1rnxqbw">IRI</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="14402">It consists of 1 or more IRIs (links) separated by commas. When set, it specifies relevant ontology concepts that classify the dataset. Typically, these can be looked up using the <a data-testid="link-with-safety" href="https://www.ebi.ac.uk/ols/index" title="https://www.ebi.ac.uk/ols/index" data-renderer-mark="true" class="cc-1rn59kg"><u data-renderer-mark="true">Ontology Lookup Service (OLS)</u></a> or <a data-testid="link-with-safety" href="https://bioportal.bioontology.org/" title="https://bioportal.bioontology.org/" data-renderer-mark="true" class="cc-1rn59kg">Bioportal</a>.&nbsp;&nbsp;</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="14631">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="14641"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/title" title="http://purl.org/dc/terms/title" data-renderer-mark="true" class="cc-1rn59kg">title</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="14650">A name given to the record.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="14681"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:title</code></p>
            <p data-renderer-start-pos="14692">&nbsp;</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="14696"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="14712">A name given to the Dataset. This property can be repeated for providing names in parallel languages.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="14817">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="14989"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/license" title="http://purl.org/dc/terms/license" data-renderer-mark="true" class="cc-1rn59kg">license</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="15000">A legal document under which the resource is made available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="15064"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:license</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="15079"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="ba7ac869-cc53-471e-9824-137e36634192" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="ba7ac869-cc53-471e-9824-137e36634192" class="cc-1rnxqbw">IRI</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="15086">This should contain a URL that provides details regarding the license that is applicable to this dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="15195">1..1</p>
         </td>
      </tr>
   </tbody>
</table>

### Recommended Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="15231"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="15248"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="15262"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="15269"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="15283"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="15297"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15314"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution" title="https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution" data-renderer-mark="true" class="cc-1rn59kg">distribution</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15330">An available distribution of the dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15375"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:distribution</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15396"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Distribution</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15417">Use this property to point to the distribution of this dataset when a distribution is available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15517">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15527"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/relation" title="http://purl.org/dc/terms/relation" data-renderer-mark="true" class="cc-1rn59kg">relation</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15539">defines a relation</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15561"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:relation</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15577"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:Project</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15593">Use this property to point to the related project of this dataset when a project is available.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15691">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="116">
            <p data-renderer-start-pos="14827"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/type" title="http://purl.org/dc/terms/type" data-renderer-mark="true" class="cc-1rn59kg">type</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="140">
            <p data-renderer-start-pos="14835">The nature or genre of the resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="14875"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:type</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="117">
            <p data-renderer-start-pos="14887"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="b69a3822-7d3f-4317-b1a0-69ed4af8fe25" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="b69a3822-7d3f-4317-b1a0-69ed4af8fe25" class="cc-1rnxqbw">IRI</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="189">
            <p data-renderer-start-pos="14894">A type of the Dataset. A recommended controlled vocabulary data-type is foreseen.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="81">
            <p data-renderer-start-pos="14979">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15701"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version" title="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version" data-renderer-mark="true" class="cc-1rn59kg">version</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15712">The version indicator (name or identifier) of a resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15773"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="c3ebb829-ad09-4ac4-bd8f-989851c58eed" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="c3ebb829-ad09-4ac4-bd8f-989851c58eed" class="cc-1rnxqbw">dcat:version</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15789"><code class="code cc-1o5d2cw" data-renderer-mark="true"><mark id="e6fb29b0-7c9c-473e-bbc4-e2a7dcbf2273" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="e6fb29b0-7c9c-473e-bbc4-e2a7dcbf2273" class="cc-1rnxqbw">rdfs:Literal</mark></code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15805">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="15811">0..*</p>
         </td>
      </tr>
   </tbody>
</table>

[Data Service](http://www.w3.org/ns/dcat#DataService "http://www.w3.org/ns/dcat#DataService")
---------------------------------------------------------------------------------------------

A collection of operations that provides access to one or more datasets or data processing functions.

### Mandatory Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
      <col style="width:88px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="15962"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="15979"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="15993"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="16000"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="16014"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="16028"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16045"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_url" title="https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_url" data-renderer-mark="true" class="cc-1rn59kg">end point URL</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16062">The root location or primary endpoint of the service (a Web-resolvable IRI).</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16142"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:endPointURL</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16162"><code class="code cc-1o5d2cw" data-renderer-mark="true">IRI</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16169">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16175">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16185"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/title" title="http://purl.org/dc/terms/title" data-renderer-mark="true" class="cc-1rn59kg">title</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16194">A name given to the distribution.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16231"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:title</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16244"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16260">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="">
            <p data-renderer-start-pos="16266">1..*</p>
         </td>
      </tr>
   </tbody>
</table>

### Recommended Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:67px">
      <col style="width:72px">
      <col style="width:88px">
      <col style="width:86px">
      <col style="width:142px">
      <col style="width:71px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="97" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="16302"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="103" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="16319"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="126" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="16333"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="124" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="16340"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="204" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="16354"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="102" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="16368"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="97">
            <p data-renderer-start-pos="16385"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_description" title="https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_description" data-renderer-mark="true" class="cc-1rn59kg">end point description</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="103">
            <p data-renderer-start-pos="16410">A description of the services available via the end-points, including their operations, parameters etc.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="126">
            <p data-renderer-start-pos="16517"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:endpointDescription</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="124">
            <p data-renderer-start-pos="16545"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="204">
            <p data-renderer-start-pos="16561">An endpoint description may be expressed in a machine-readable form, such as an OpenAPI (Swagger) description [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-openapi" title="https://www.w3.org/TR/vocab-dcat-3/#bib-openapi" data-renderer-mark="true" class="cc-1rn59kg">OpenAPI</a>], an OGC <code class="code cc-1o5d2cw" data-renderer-mark="true">GetCapabilities</code> response [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-wfs" title="https://www.w3.org/TR/vocab-dcat-3/#bib-wfs" data-renderer-mark="true" class="cc-1rn59kg">WFS</a>], [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19142" title="https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19142" data-renderer-mark="true" class="cc-1rn59kg">ISO-19142</a>], [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-wms" title="https://www.w3.org/TR/vocab-dcat-3/#bib-wms" data-renderer-mark="true" class="cc-1rn59kg">WMS</a>], [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19128" title="https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19128" data-renderer-mark="true" class="cc-1rn59kg">ISO-19128</a>], a SPARQL Service Description [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-sparql11-service-description" title="https://www.w3.org/TR/vocab-dcat-3/#bib-sparql11-service-description" data-renderer-mark="true" class="cc-1rn59kg">SPARQL11-SERVICE-DESCRIPTION</a>], an [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-opensearch" title="https://www.w3.org/TR/vocab-dcat-3/#bib-opensearch" data-renderer-mark="true" class="cc-1rn59kg">OpenSearch</a>] or [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-wsdl20" title="https://www.w3.org/TR/vocab-dcat-3/#bib-wsdl20" data-renderer-mark="true" class="cc-1rn59kg">WSDL20</a>] document, a Hydra API description [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-hydra" title="https://www.w3.org/TR/vocab-dcat-3/#bib-hydra" data-renderer-mark="true" class="cc-1rn59kg">HYDRA</a>], else in text or some other informal mode if a formal representation is not possible.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="102">
            <p data-renderer-start-pos="16974">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="97">
            <p data-renderer-start-pos="16984"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_serves_dataset" title="https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_serves_dataset" data-renderer-mark="true" class="cc-1rn59kg">serves dataset</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="103">
            <p data-renderer-start-pos="17002">A collection of data that this data service can distribute.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="126">
            <p data-renderer-start-pos="17065"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:servesDataset</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="124">
            <p data-renderer-start-pos="17087"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Dataset</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="204">
            <p data-renderer-start-pos="17103">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="102">
            <p data-renderer-start-pos="17109">0..*</p>
         </td>
      </tr>
   </tbody>
</table>

[Distribution](http://www.w3.org/ns/dcat#Distribution "http://www.w3.org/ns/dcat#Distribution")
-----------------------------------------------------------------------------------------------

An available distribution of the dataset.

### Mandatory Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:103px">
      <col style="width:122px">
      <col style="width:104px">
      <col style="width:86px">
      <col style="width:126px">
      <col style="width:92px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="148" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="17200"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="175" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="17217"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="149" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="17231"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="124" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="17238"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="181" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="17252"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="132" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="17266"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="148">
            <p data-renderer-start-pos="17283"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/title" title="http://purl.org/dc/terms/title" data-renderer-mark="true" class="cc-1rn59kg"><mark id="98f99001-8e94-4ebf-898f-457675beefa2" aria-disabled="true" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="98f99001-8e94-4ebf-898f-457675beefa2" class="cc-1rnxqbw">title</mark></a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="175">
            <p data-renderer-start-pos="17292">A name given to the distribution.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="149">
            <p data-renderer-start-pos="17329"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:title</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="124">
            <p data-renderer-start-pos="17342"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="181">
            <p data-renderer-start-pos="17358">the name of the dataset in combination with the format of the distribution can be used</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="132">
            <p data-renderer-start-pos="17449">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="148">
            <p data-renderer-start-pos="17459"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_url" title="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_url" data-renderer-mark="true" class="cc-1rn59kg">access URL</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="175">
            <p data-renderer-start-pos="17473">A URL of the resource that gives access to a distribution of the dataset. E.g., landing page, feed, SPARQL endpoint.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="149">
            <p data-renderer-start-pos="17593"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:accessURL</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="124">
            <p data-renderer-start-pos="17611"><code class="code cc-1o5d2cw" data-renderer-mark="true">IRI</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="181">
            <p data-renderer-start-pos="17618">This property contains a URL that gives access to a Distribution of the Dataset. The resource at the access URL may contain information about how to get the Dataset.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="132">
            <p data-renderer-start-pos="17787">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="148">
            <p data-renderer-start-pos="17797"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_media_type" title="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_media_type" data-renderer-mark="true" class="cc-1rn59kg">media type</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="175">
            <p data-renderer-start-pos="17811">The media type of the distribution as defined by IANA [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types" title="https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types" data-renderer-mark="true" class="cc-1rn59kg">IANA-MEDIA-TYPES</a>].</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="149">
            <p data-renderer-start-pos="17888"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:mediaType</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="124">
            <p data-renderer-start-pos="17906"><code class="code cc-1o5d2cw" data-renderer-mark="true">IRI</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="181">
            <p data-renderer-start-pos="17914">This property <em data-renderer-mark="true">SHOULD</em> be used when the media type of the distribution is defined in IANA [<a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types" title="https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types" data-renderer-mark="true" class="cc-1rn59kg">IANA-MEDIA-TYPES</a>], otherwise <code class="code cc-1o5d2cw" data-renderer-mark="true">dcterms:format</code> <em data-renderer-mark="true">MAY</em> be used with different values.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="132">
            <p data-renderer-start-pos="18085">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="148">
            <p data-renderer-start-pos="18095"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/description" title="http://purl.org/dc/terms/description" data-renderer-mark="true" class="cc-1rn59kg">description</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="175">
            <p data-renderer-start-pos="18110">A unique identifier of the resource being described or catalog.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="149">
            <p data-renderer-start-pos="18177"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:description</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="124">
            <p data-renderer-start-pos="18196"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="181">
            <p data-renderer-start-pos="18212">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="132">
            <p data-renderer-start-pos="18218">1..*</p>
         </td>
      </tr>
   </tbody>
</table>

### Recommended Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:59px">
      <col style="width:116px">
      <col style="width:83px">
      <col style="width:105px">
      <col style="width:95px">
      <col style="width:68px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="85" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="18254"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="166" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="18271"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="119" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="18285"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="151" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="18292"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="137" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="18306"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="98" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="18320"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="85">
            <p data-renderer-start-pos="18337"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_service" title="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_service" data-renderer-mark="true" class="cc-1rn59kg">access service</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="166">
            <p data-renderer-start-pos="18355">A data service that gives access to the distribution of the dataset</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="119">
            <p data-renderer-start-pos="18426"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:accessService</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="151">
            <p data-renderer-start-pos="18448"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:DataService</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="137">
            <p data-renderer-start-pos="18468"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:accessService</code> <em data-renderer-mark="true">SHOULD</em> be used to link to a description of a <code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:DataService</code> that can provide access to this distribution.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="98">
            <p data-renderer-start-pos="18598">0..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="85">
            <p data-renderer-start-pos="18608"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_download_url" title="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_download_url" data-renderer-mark="true" class="cc-1rn59kg">download URL</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="166">
            <p data-renderer-start-pos="18624">The URL of the downloadable file in a given format. E.g., CSV file or RDF file. The format is indicated by the distribution's <code class="code cc-1o5d2cw" data-renderer-mark="true">dcterms:format</code> and/or <code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:mediaType</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="119">
            <p data-renderer-start-pos="18790"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:downloadURL</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="151">
            <p data-renderer-start-pos="18810"><code class="code cc-1o5d2cw" data-renderer-mark="true">IRI</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="137">
            <p data-renderer-start-pos="18818">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="98">
            <p data-renderer-start-pos="18824">0..*</p>
         </td>
      </tr>
   </tbody>
</table>

Agent
-----

An entity that is associated with catalog and/or Datasets. Agent can be individuals or organisations, If the Agent is an organisation, the use of the Organization Ontology is recommended.

### Mandatory Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:63px">
      <col style="width:114px">
      <col style="width:93px">
      <col style="width:74px">
      <col style="width:116px">
      <col style="width:70px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="91" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19054"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="163" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19071"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="133" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19085"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="107" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19092"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="167" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19106"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="101" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19120"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="91">
            <p data-renderer-start-pos="19137"><a data-testid="link-with-safety" href="http://xmlns.com/foaf/spec/#term_name" title="http://xmlns.com/foaf/spec/#term_name" data-renderer-mark="true" class="cc-1rn59kg">name</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="163">
            <p data-renderer-start-pos="19145">A name for some thing.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="133">
            <p data-renderer-start-pos="19171"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:name</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="107">
            <p data-renderer-start-pos="19184"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:string</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="167">
            <p data-renderer-start-pos="19198">This property contains a name of the agent. This property can be repeated for different versions of the name (e.g. the name in different languages)</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="101">
            <p data-renderer-start-pos="19349">1..1</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="91">
            <p data-renderer-start-pos="19359"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/identifier" title="http://purl.org/dc/terms/identifier" data-renderer-mark="true" class="cc-1rn59kg">identifier</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="163">
            <p data-renderer-start-pos="19373">A unique identifier of the resource being described or catalog.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="133">
            <p data-renderer-start-pos="19440"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:identifier</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="107">
            <p data-renderer-start-pos="19458"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:string</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="167">
            <p data-renderer-start-pos="19472">&nbsp;</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="101">
            <p data-renderer-start-pos="19476">1..1</p>
         </td>
      </tr>
   </tbody>
</table>

### Recommended Properties

No recommended properties are identified for this release.

Project
-------

A project (a collective endeavour of some kind).

### Mandatory Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:88px">
      <col style="width:125px">
      <col style="width:95px">
      <col style="width:78px">
      <col style="width:72px">
      <col style="width:71px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="127" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19654"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="180" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19671"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="137" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19685"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="112" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19692"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="104" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19706"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="102" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="19720"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="127">
            <p data-renderer-start-pos="19737"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/description" title="http://purl.org/dc/terms/description" data-renderer-mark="true" class="cc-1rn59kg">description</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="180">
            <p data-renderer-start-pos="19752">description of the project</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="137">
            <p data-renderer-start-pos="19783"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:description</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="112">
            <p data-renderer-start-pos="19802"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="104">
            <p data-renderer-start-pos="19818">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="102">
            <p data-renderer-start-pos="19824">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="127">
            <p data-renderer-start-pos="19834"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/identifier" title="http://purl.org/dc/terms/identifier" data-renderer-mark="true" class="cc-1rn59kg">identifier</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="180">
            <p data-renderer-start-pos="19848">A unique identifier of the resource being described or catalog.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="137">
            <p data-renderer-start-pos="19915"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:identifier</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="112">
            <p data-renderer-start-pos="19933"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:string</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="104">
            <p data-renderer-start-pos="19947">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="102">
            <p data-renderer-start-pos="19953">1.1</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="127">
            <p data-renderer-start-pos="19962"><a data-testid="link-with-safety" href="http://purl.org/dc/terms/title" title="http://purl.org/dc/terms/title" data-renderer-mark="true" class="cc-1rn59kg">title</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="180">
            <p data-renderer-start-pos="19971">A name given to the resource.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="137">
            <p data-renderer-start-pos="20004"><code class="code cc-1o5d2cw" data-renderer-mark="true">dct:title</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="112">
            <p data-renderer-start-pos="20017"><code class="code cc-1o5d2cw" data-renderer-mark="true">rdfs:Literal</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="104">
            <p data-renderer-start-pos="20033">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="102">
            <p data-renderer-start-pos="20039">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="127">
            <p data-renderer-start-pos="20049"><a data-testid="link-with-safety" href="http://xmlns.com/foaf/spec/#term_fundedBy" title="http://xmlns.com/foaf/spec/#term_fundedBy" data-renderer-mark="true" class="cc-1rn59kg">funded by</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="180">
            <p data-renderer-start-pos="20062">An organization funding a project or person.</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="137">
            <p data-renderer-start-pos="20110"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:fundedBy</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="112">
            <p data-renderer-start-pos="20127"><code class="code cc-1o5d2cw" data-renderer-mark="true">foaf:Agent</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="104">
            <p data-renderer-start-pos="20141">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="102">
            <p data-renderer-start-pos="20147">1..*</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="127">
            <p data-renderer-start-pos="20157"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset" title="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset" data-renderer-mark="true" class="cc-1rn59kg">dataset</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="180">
            <p data-renderer-start-pos="20168">link to the project datasets</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="137">
            <p data-renderer-start-pos="20200"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:dataset</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="112">
            <p data-renderer-start-pos="20216"><code class="code cc-1o5d2cw" data-renderer-mark="true">dcat:Dataset</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="104">
            <p data-renderer-start-pos="20232">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="102">
            <p data-renderer-start-pos="20238">1..*</p>
         </td>
      </tr>
   </tbody>
</table>

### Recommended Properties

No recommended properties are identified for this release.

Kind
----

Contact information of the contact point for Dataset and DatasetSeries.

### Mandatory Properties

<table data-testid="renderer-table" data-number-column="false" data-table-width="760" data-layout="default">
   <colgroup>
      <col style="width:88px">
      <col style="width:125px">
      <col style="width:95px">
      <col style="width:78px">
      <col style="width:72px">
      <col style="width:71px">
   </colgroup>
   <tbody>
      <tr>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="127" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="20435"><strong data-renderer-mark="true">Property name</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="180" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="20452"><strong data-renderer-mark="true">Definition</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="137" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="20466"><strong data-renderer-mark="true">URI</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="112" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="20473"><strong data-renderer-mark="true">rdfs:Range</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="104" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="20487"><strong data-renderer-mark="true">Usage Note</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
         <th rowspan="1" colspan="1" colorname="" class="ak-renderer-tableHeader-sortable-column__wrapper" data-colwidth="102" aria-sort="none">
            <div class="ak-renderer-tableHeader-sortable-column">
               <p data-renderer-start-pos="20501"><strong data-renderer-mark="true">Cardinality</strong></p>
               <figure class="ak-renderer-tableHeader-sorting-icon__wrapper ak-renderer-tableHeader-sorting-icon__no-order">
                  <div class="ak-renderer-tableHeader-sorting-icon  cc-1eczmg9" role="button" tabindex="0" aria-label="No sort applied to the column" aria-disabled="false">
                     <div class="sorting-icon-svg__no_order ak-renderer-tableHeader-sorting-icon-inactive cc-37vp66">
                        <div class="cc-1uj2pwb"></div>
                     </div>
                  </div>
               </figure>
            </div>
         </th>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="127">
            <p data-renderer-start-pos="20518"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vcard-rdf/#d4e183" title="https://www.w3.org/TR/vcard-rdf/#d4e183" data-renderer-mark="true" class="cc-1rn59kg">has email</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="180">
            <p data-renderer-start-pos="20531">To specify the electronic mail address for communication with the object</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="137">
            <p data-renderer-start-pos="20607"><code class="code cc-1o5d2cw" data-renderer-mark="true">vcard:hasEmail</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="112">
            <p data-renderer-start-pos="20625"><code class="code cc-1o5d2cw" data-renderer-mark="true">IRI</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="104">
            <p data-renderer-start-pos="20632">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="102">
            <p data-renderer-start-pos="20638">1</p>
         </td>
      </tr>
      <tr>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="127">
            <p data-renderer-start-pos="20645"><a data-testid="link-with-safety" href="https://www.w3.org/TR/vcard-rdf/#d4e380" title="https://www.w3.org/TR/vcard-rdf/#d4e380" data-renderer-mark="true" class="cc-1rn59kg">has name</a></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="180">
            <p data-renderer-start-pos="20657">To specify the components of the name of the object</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="137">
            <p data-renderer-start-pos="20712"><code class="code cc-1o5d2cw" data-renderer-mark="true">vcard:hasName</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="112">
            <p data-renderer-start-pos="20729"><code class="code cc-1o5d2cw" data-renderer-mark="true">xsd:string</code></p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="104">
            <p data-renderer-start-pos="20743">NA</p>
         </td>
         <td rowspan="1" colspan="1" colorname="" data-colwidth="102">
            <p data-renderer-start-pos="20749">1</p>
         </td>
      </tr>
   </tbody>
</table>

### Recommended Properties

No recommended properties are identified for this release.

Cataloged Resource
------------------

All things described by RDF are called _resources_, and they are instances of the class `dcat:Resource`. This is the class of everything. All other classes are [subclasses](https://www.w3.org/TR/rdf12-schema/#def-subclass "https://www.w3.org/TR/rdf12-schema/#def-subclass") of this class. To read more, go to

Further Information
===============================================

### Feedback - Git Issues

If you wish to extend the model, such as with Resource, and/or create a new concept, please open an issue [here](https://github.com/Health-RI/health-ri-metadata/issues) and provide a clear explanation for the extension. Assign the issue to either ‘**brunasv’ or ‘xiaofengleo’**, and we will work with you to implement the addition in the next release.

### Model extension

Within DCAT and DCAT-AP, the term "resource" generally encompasses all objects that can be described using [RDF](https://www.w3.org/RDF/ "https://www.w3.org/RDF/"). However, there are specific categories and attributes used to indicate the different types of resources:

*   `dcat:Dataset` is a type of `dcat:Resource` representing a collection of data
    
*   `dcat:Distribution` is a type of `dcat:Resourcee` representing an available form or representation of a dataset.
    
*   `dcat:Catalog` is a type of `dcat:Resource` representing a collection of datasets.
    
*   `dcat:DataService` , introduced in DCAT version 2, is a type of Resource representing a service for accessing data.
    
*   `foaf:Project` is a type of `dcat:Resource` representing project-level information
    

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

To create the current core metadata schema, we examined existing metadata from the [COVID-19 national portal](https://covid19initiatives.health-ri.nl/ "https://covid19initiatives.health-ri.nl/"), metadata schema provided by Health-RI nodes (e.g., [ABC metadata](https://github.com/AmsterdamUMC/ABC-metadata-project "https://github.com/AmsterdamUMC/ABC-metadata-project")), and standards used in portals across Europe and beyond (e.g., W3C, DCAT, DCAT-AP). With the help of metadata specialists, we mapped their classes and properties and decided to reuse DCAT and DCAT-AP for implementation. The Core metadata schema includes DCAT v3 and selected DCAT-AP mandatory classes, ensuring compatibility with international catalogs. DCAT-AP covers the identified requirements for exchanging information about datasets and services in Europe. Alignment with DCAT NL is under development.

### Implementation

The model is part of the requirements to onboard to the Health-RI catalog, and documentation for users is not yet released. However, users can start the onboarding process by publishing their metadata according to this schema in a FAIR Data Point. To start:
- read the explanation of all classes and properties in the [Core Metadata Schema Specification](https://github.com/Health-RI/health-ri-metadata) 
- collect and map your metadata instances to the model using this [example metadata collection sheet](https://github.com/Health-RI/health-ri-metadata/blob/master/Implementation/metadata%20collection%20sheet%20template.xlsx)
- import the provided [shacl](https://github.com/Health-RI/health-ri-metadata/tree/master/Formalisation(shacl)/Core/PiecesShape) to your FDP (note: tutorial on how to configure your FDP for Health-RI's requirements is being developed)
- For a complete overview of the onboarding process, users can look for the [Metadata Onboarding on the National Catalogue](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/279150593) with details on how to implement and connect to it.
- For an overview of the mapping pipeline visit the [Mapping Pipeline](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/290291734).    
- With any further questions or comments please contact Health-RI via the [Health-RI Servicedesk](https://www.health-ri.nl/health-ri-servicedesk) or via [servicedesk@health-ri.nl](mailto:servicedesk@health-ri.nl "mailto:servicedesk@health-ri.nl")
