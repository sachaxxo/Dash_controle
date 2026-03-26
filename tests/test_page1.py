from dash import dcc
import dash_bootstrap_components as dbc

from pages.page1 import create_layout


def test_page1_layout_exists():
    layout = create_layout()
    assert layout is not None


def test_page1_contains_a_card():
    layout = create_layout()
    cards = [child for child in layout.children if isinstance(child, dbc.Card)]
    assert len(cards) == 1


def test_page1_contains_two_graphs():
    layout = create_layout()
    card = layout.children[0]
    body = card.children[1]
    row = body.children[0]

    graph_count = 0
    for col in row.children:
        if isinstance(col.children, list):
            for item in col.children:
                if isinstance(item, dcc.Graph):
                    graph_count += 1
        elif isinstance(col.children, dcc.Graph):
            graph_count += 1

    assert graph_count == 2