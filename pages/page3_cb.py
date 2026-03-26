from dash import Input, Output, callback, dcc
from pages.page3 import load_markdown


@callback(
    Output("page3-content", "children"),
    Input("page3-tabs", "active_tab"),
)
def update_tab_content(active_tab):
    if active_tab == "tab-1":
        content = load_markdown("expli1.md")
    elif active_tab == "tab-2":
        content = load_markdown("expli2.md")
    elif active_tab == "tab-3":
        content = load_markdown("expli3.md")
    else:
        content = "Aucun contenu"

    return dcc.Markdown(content)