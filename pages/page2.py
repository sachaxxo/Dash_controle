from pathlib import Path

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table, html
import dash

try:
    dash.register_page(__name__, path="/page2", name="Page 2")
except dash.exceptions.PageError:
    pass

DATA_PATH = Path(__file__).resolve().parent.parent / "datas" / "avocado.csv"

COLUMNS_TO_HIDE = [
    "Unnamed: 0",
    "4046",
    "4225",
    "4770",
    "Small Bags",
    "Large Bags",
    "XLarge Bags",
]


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)

    columns_to_drop = [col for col in COLUMNS_TO_HIDE if col in df.columns]
    if columns_to_drop:
        df = df.drop(columns=columns_to_drop)

    return df


def get_region_options(df: pd.DataFrame) -> list[dict]:
    regions = sorted(df["region"].dropna().unique())
    return [{"label": "Toutes", "value": "Toutes"}] + [
        {"label": region, "value": region} for region in regions
    ]


def get_type_options(df: pd.DataFrame) -> list[dict]:
    avocado_types = sorted(df["type"].dropna().unique())
    return [{"label": "Tous", "value": "Tous"}] + [
        {"label": avocado_type, "value": avocado_type} for avocado_type in avocado_types
    ]


def create_layout():
    df = load_data()

    return dbc.Container(
        [
            dbc.Card(
                [
                    dbc.CardHeader(
                        html.H2("Page 2 - Tableau des données", className="mb-0")
                    ),
                    dbc.CardBody(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            dbc.Label("Région"),
                                            dbc.Select(
                                                id="page2-region-select",
                                                options=get_region_options(df),
                                                value="Toutes",
                                            ),
                                        ],
                                        xs=12,
                                        md=6,
                                        className="mb-3",
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Label("Type d'avocat"),
                                            dbc.Checklist(
                                                id="page2-type-checklist",
                                                options=get_type_options(df),
                                                value=["Tous"],
                                                inline=True,
                                            ),
                                        ],
                                        xs=12,
                                        md=6,
                                        className="mb-3",
                                    ),
                                ]
                            ),
                            dbc.Badge(
                                f"{len(df)} lignes affichées",
                                id="page2-badge",
                                color="primary",
                                className="mb-3",
                            ),
                            dash_table.DataTable(
                                id="page2-table",
                                columns=[{"name": col, "id": col} for col in df.columns],
                                data=df.to_dict("records"),
                                sort_action="native",
                                page_size=12,
                                style_table={"overflowX": "auto"},
                            ),
                        ]
                    ),
                ],
                className="shadow-sm",
            )
        ],
        fluid=True,
        className="py-4",
    )
layout = create_layout()
