from dash import Input, Output, callback

from pages.page2 import load_data


@callback(
    Output("page2-table", "data"),
    Output("page2-badge", "children"),
    Output("page2-kpi-rows", "children"),
    Output("page2-kpi-price", "children"),
    Output("page2-kpi-volume", "children"),
    Input("page2-region-select", "value"),
    Input("page2-type-checklist", "value"),
)
def update_page2_table(selected_region, selected_types):
    df = load_data()

    if selected_region and selected_region != "Toutes":
        df = df[df["region"] == selected_region]

    if selected_types and "Tous" not in selected_types:
        df = df[df["type"].isin(selected_types)]

    row_count = len(df)

    if row_count == 0:
        avg_price_text = "0.00"
        total_volume_text = "0"
    else:
        avg_price_text = f"{df['AveragePrice'].mean():.2f}"
        total_volume_text = f"{df['Total Volume'].sum():,.0f}".replace(",", " ")

    return (
        df.to_dict("records"),
        f"{row_count} lignes affichées",
        str(row_count),
        avg_price_text,
        total_volume_text,
    )