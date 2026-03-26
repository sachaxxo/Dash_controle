from dash import Input, Output, callback

from pages.page2 import load_data


@callback(
    Output("page2-table", "data"),
    Output("page2-badge", "children"),
    Input("page2-region-select", "value"),
    Input("page2-type-checklist", "value"),
)
def update_page2_table(selected_region, selected_types):
    df = load_data()

    if selected_region and selected_region != "Toutes":
        df = df[df["region"] == selected_region]

    if selected_types and "Tous" not in selected_types:
        df = df[df["type"].isin(selected_types)]

    return df.to_dict("records"), f"{len(df)} lignes affichées"
