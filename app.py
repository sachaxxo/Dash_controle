import dash
import dash_bootstrap_components as dbc
from pages.page2 import create_layout

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True,
)

app.title = "Dash Luret"
app.layout = create_layout()

server = app.server

if __name__ == "__main__":
    app.run(debug=True)