import dash
import dash_bootstrap_components as dbc
from dash import html

import pages.page2_cb
import pages.page3_cb


app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True,
)

app.title = "Dash Luret"
server = app.server

navbar = dbc.NavbarSimple(
    brand="Dash Luret",
    brand_href="/",
    color="dark",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="/")),
        dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
        dbc.NavItem(dbc.NavLink("Page 3", href="/page3")),
    ],
)

app.layout = dbc.Container(
    [
        navbar,
        html.Div(dash.page_container, className="mt-4"),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run(debug=True)