from pathlib import Path
import dash

import dash_bootstrap_components as dbc
from dash import dcc, html

DOCS_PATH = Path(__file__).resolve().parent.parent / "docs"

try:
    dash.register_page(__name__, path="/page3", name="Page 3")
except dash.exceptions.PageError:
    pass


def load_markdown(filename: str) -> str:
    with open(DOCS_PATH / filename, "r", encoding="utf-8") as f:
        return f.read()


def create_layout():
    return dbc.Container(
        [
            dbc.Card(
                [
                    dbc.CardHeader(
                        html.H2("Page 3 - Documentation", className="mb-0")
                    ),
                    dbc.CardBody(
                        [
                            dbc.Tabs(
                                [
                                    dbc.Tab(
                                        label="Explication 1",
                                        tab_id="tab-1",
                                    ),
                                    dbc.Tab(
                                        label="Explication 2",
                                        tab_id="tab-2",
                                    ),
                                    dbc.Tab(
                                        label="Explication 3",
                                        tab_id="tab-3",
                                    ),
                                ],
                                id="page3-tabs",
                                active_tab="tab-1",
                            ),
                            html.Div(id="page3-content"),
                        ]
                    ),
                ]
            )
        ],
        fluid=True,
        className="py-4",
    )
layout = create_layout()

dcc.Loading(
    id="loading",
    type="circle",
    children=html.Div(id="page3-content")
)