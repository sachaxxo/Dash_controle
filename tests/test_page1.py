from dash import dcc
import dash_bootstrap_components as dbc

from pages.page1 import create_layout
from pages.page1 import build_region_figure, load_data
from pages.page1 import update_region_graph


def test_callback_invalid_region():
    result = update_region_graph("INVALID_REGION")
    # soit no_update, soit figure
    assert result is not None
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

    


def test_build_region_figure():
    df = load_data()
    fig = build_region_figure(df, "TotalUS")
    assert fig is not None
    
from pages.page1 import get_region_total_text, load_data


def test_get_region_total_text():
    df = load_data()
    text = get_region_total_text(df, "TotalUS")
    assert "Volume total cumulé" in text