import pytest
from pyshacl import validate


@pytest.mark.parametrize(
    ("shacl", "example"),
    [
        ("Catalog", "example-catalog"),
        ("Dataset", "example-dataset"),
        ("Dataset-mandatory", "example-dataset-mandatory"),
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
        ("Dataset-mandatory", "example-dataset-bad"),
        ("Dataset-mandatory", "dataset-nomodified"),
        ("Dataset-mandatory", "dataset-nopublisher"),
        ("Dataset-mandatory", "dataset-nolicense"),
        ("Dataset-mandatory", "dataset-nodescription"),
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
        ("Dataset-mandatory", "dataset-iso8601"),
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
    return rf"Formalisation(shacl)/Core/PiecesShape/{shacl}.ttl"
