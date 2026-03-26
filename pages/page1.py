from pathlib import Path
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dcc, html, no_update
from dash import no_update
DATA_PATH = Path(__file__).resolve().parent.parent / "datas" / "avocado.csv"

try:
    dash.register_page(__name__, path="/", name="Page 1")
except dash.exceptions.PageError:
    pass


REGIONS_TOTALS = [
    "MidSouth",
    "Northeast",
    "SouthCentral",
    "Southeast",
    "TotalUS",
    "West",
]


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    return df


def build_totals_figure(df: pd.DataFrame):
    filtered = df[df["region"].isin(REGIONS_TOTALS)]
    totals = (
        filtered.groupby("region", as_index=False)["Total Volume"]
        .sum()
        .sort_values("Total Volume", ascending=False)
    )

    fig = px.bar(
        totals,
        x="region",
        y="Total Volume",
        title="Volumes totaux des régions imposées",
    )
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    return fig


def build_region_figure(df: pd.DataFrame, region: str):
    filtered = df[df["region"] == region]
    totals = (
        filtered.groupby("year", as_index=False)["Total Volume"]
        .sum()
        .sort_values("year")
    )

    fig = px.line(
        totals,
        x="year",
        y="Total Volume",
        markers=True,
        title=f"Volumes vendus pour {region}",
    )
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    return fig


def create_layout():
    df = load_data()
    default_region = "TotalUS"

    return dbc.Container(
        [
            dbc.Card(
                [
                    dbc.CardHeader(html.H2("Page 1 - Comparaison des volumes", className="mb-0")),
                    dbc.CardBody(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dcc.Graph(
                                            id="page1-totals-graph",
                                            figure=build_totals_figure(df),
                                            style={"display": "block"},
                                        ),
                                        md=7,
                                        xs=12,
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Badge(
                                                "Choix de la région",
                                                color="primary",
                                                className="mb-3",
                                            ),
                                            dbc.Select(
                                                id="page1-region-select",
                                                options=[
                                                    {"label": region, "value": region}
                                                    for region in sorted(df["region"].dropna().unique())
                                                ],
                                                value=default_region,
                                                className="mb-3",
                                            ),
                                            dcc.Graph(
                                                id="page1-region-graph",
                                                figure=build_region_figure(df, default_region),
                                            ),
                                        ],
                                        md=5,
                                        xs=12,
                                    ),
                                ],
                                className="g-4",
                            )
                        ]
                    ),
                ],
                className="shadow-sm",
            )
        ],
        fluid=True,
        className="py-4",
    )

@callback(
    Output("page1-region-graph", "figure"),
    Input("page1-region-select", "value"),
)
def update_region_graph(selected_region):
    if selected_region is None:
        return no_update

    df = load_data()

    if selected_region not in df["region"].unique():
        return no_update

    return build_region_figure(df, selected_region)
layout = create_layout()