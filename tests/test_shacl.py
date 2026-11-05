import pytest
from pyshacl import validate


@pytest.mark.parametrize(
    ("shacl", "example"),
    [
        ("Catalog", "example-catalog"),
        ("Dataset", "example-dataset"),
        ("Distribution", "example-distribution"),
        ("DataService", "example-dataservice"),
    ],
)
def test_core_shapes_examples(shacl, example):
    shacl_graph = get_shacl_path(shacl)
    example_graph = get_example_path(example)

    conform, _, result_text = validate(
        data_graph=example_graph,
        shacl_graph=shacl_graph,
        allow_warnings=False,
        meta_shacl=True,
    )
    assert conform, result_text


@pytest.mark.parametrize(
    ("shacl", "example"),
    [
        ("Dataset", "example-dataset-bad"),
        ("Dataset", "dataset-nomodified"),
        ("Dataset", "dataset-nopublisher"),
        ("Dataset", "dataset-nolicense"),
        ("Dataset", "dataset-nodescription"),
    ],
)
def test_core_shapes_negative(shacl, example):
    shacl_graph = get_shacl_path(shacl)
    example_graph = get_testcase_path(example)

    conform, _, result_text = validate(
        data_graph=example_graph,
        shacl_graph=shacl_graph,
        allow_warnings=False,
        meta_shacl=True,
    )
    assert not conform, result_text


@pytest.mark.parametrize(
    ("shacl", "example"),
    [
        ("Dataset", "dataset-iso8601"),
    ],
)
def test_core_shapes_good(shacl, example):
    shacl_graph = get_shacl_path(shacl)
    example_graph = get_testcase_path(example)

    conform, _, result_text = validate(
        data_graph=example_graph,
        shacl_graph=shacl_graph,
        allow_warnings=False,
        meta_shacl=True,
    )
    assert not conform, result_text


def get_example_path(example):
    return rf"Formalisation(shacl)/Core/Example-Data/{example}.ttl"


def get_testcase_path(testcase):
    return rf"tests/testdata/{testcase}.ttl"


def get_shacl_path(shacl):
    return rf"Formalisation(shacl)/Core/FairDataPointShape/{shacl}.ttl"

def test_new_properties_and_csvw_example_coverage():
    from rdflib import Graph, Namespace, URIRef
    from rdflib.namespace import RDF, DCTERMS
    data = Graph().parse(get_example_path("example-dataset"))
    dataset = URIRef("http://example.com/dataset")
    csvw = Namespace("http://www.w3.org/ns/csvw#")
    dqv = Namespace("http://www.w3.org/ns/dqv#")
    for property_iri in (
        DCTERMS.alternative, DCTERMS.provenance, dqv.hasQualityAnnotation,
        URIRef("http://edamontology.org/has_topic"),
        URIRef("http://healthdataportal.eu/ns/health#hasVariables"),
        URIRef("https://w3id.org/health-ri/metadata-vocabulary#anatomicalLocationCovered"),
        URIRef("https://w3id.org/health-ri/metadata-vocabulary#healthConditionOfInterest"),
        URIRef("https://schema.org/measurementTechnique"),
    ):
        assert list(data.objects(dataset, property_iri)), f"Missing: {property_iri}"
    group = URIRef("http://example.com/dataset/variables")
    table = URIRef("http://example.com/dataset/variables/table")
    column = URIRef("http://example.com/dataset/variables/age")
    assert (group, RDF.type, csvw.TableGroup) in data
    assert (group, csvw.table, table) in data
    assert (table, RDF.type, csvw.Table) in data
    assert (table, csvw.column, column) in data
    assert (column, RDF.type, csvw.Column) in data
    for prop in (csvw.name, csvw.title, csvw.datatype, csvw.propertyUrl, DCTERMS.description):
        assert list(data.objects(column, prop))
    dist = Graph().parse(get_example_path("example-distribution"))
    assert (
        URIRef("http://example.com/distribution"),
        URIRef("http://data.europa.eu/r5r/availability"),
        URIRef("http://publications.europa.eu/resource/authority/planned-availability/STABLE"),
    ) in dist


def test_correct_dqv_namespace_in_dataset_shape():
    from rdflib import Graph, URIRef
    from rdflib.namespace import SH
    graph = Graph().parse(get_shacl_path("Dataset"))
    prop = URIRef("http://data.health-ri.nl/core/p2/DatasetShape#dqv:hasQualityAnnotation")
    path = URIRef("http://www.w3.org/ns/dqv#hasQualityAnnotation")
    assert (prop, SH.path, path) in graph


def test_csvw_tablegroup_example_conforms():
    conform, _, report = validate(
        data_graph=get_example_path("example-dataset"),
        shacl_graph=get_shacl_path("TableGroup"),
        allow_warnings=False,
        meta_shacl=True,
    )
    assert conform, report


def test_csvw_missing_column_name_is_rejected():
    from rdflib import Graph, Namespace, URIRef
    graph = Graph().parse(get_example_path("example-dataset"))
    graph.remove((URIRef("http://example.com/dataset/variables/age"),
                  Namespace("http://www.w3.org/ns/csvw#").name, None))
    conform, _, report = validate(
        data_graph=graph,
        shacl_graph=get_shacl_path("TableGroup"),
        allow_warnings=False,
        meta_shacl=True,
    )
    assert not conform, report


@pytest.mark.xfail(strict=True, reason="Pending separately scoped ICD-10 regex fix")
def test_icd10_iri_should_be_accepted():
    from rdflib import Graph
    graph = Graph().parse(get_example_path("example-dataset"))
    graph.parse(get_example_path("example-icd10"))
    conform, _, report = validate(
        data_graph=graph,
        shacl_graph=get_shacl_path("Dataset"),
        allow_warnings=False,
        meta_shacl=True,
    )
    assert conform, report
