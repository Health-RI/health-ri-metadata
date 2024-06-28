import pytest
from pyshacl import validate


@pytest.mark.parametrize(
    ("shacl", "example"),
    [
        ("Catalog", "example-catalog"),
        ("Dataset", "example-dataset"),
        ("Distribution", "example-distribution"),
    ],
)
def test_core_shapes(shacl, example):
    shacl_graph = rf"Formalisation(shacl)/Core/PiecesShape/{shacl}.ttl"
    example_graph = rf"Formalisation(shacl)/Core/Example-Data/{example}.ttl"

    conform, _, result_text = validate(
        data_graph=example_graph,
        shacl_graph=shacl_graph,
        allow_warnings=False,
        meta_shacl=True,
    )
    assert conform, result_text
