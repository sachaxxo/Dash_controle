import dash_bootstrap_components as dbc
from dash import dash_table

from pages.page2 import create_layout, load_data, get_region_options, get_type_options


def test_page2_layout_exists():
    layout = create_layout()
    assert layout is not None


def test_page2_contains_card():
    layout = create_layout()
    cards = [child for child in layout.children if isinstance(child, dbc.Card)]
    assert len(cards) == 1


def test_page2_data_is_loaded():
    df = load_data()
    assert len(df) > 0
    assert "region" in df.columns
    assert "type" in df.columns


def test_page2_region_options_are_unique():
    df = load_data()
    options = get_region_options(df)
    values = [option["value"] for option in options if option["value"] != "Toutes"]
    assert len(values) == len(set(values))


def test_page2_type_options_are_unique():
    df = load_data()
    options = get_type_options(df)
    values = [option["value"] for option in options if option["value"] != "Tous"]
    assert len(values) == len(set(values))


def test_page2_contains_datatable():
    layout = create_layout()
    card = layout.children[0]
    body = card.children[1]

    found_table = False
    for element in body.children:
        if isinstance(element, dash_table.DataTable):
            found_table = True

    assert found_table