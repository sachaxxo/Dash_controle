import dash

from app import app


def test_app_exists():
    assert app is not None


def test_dash_pages_enabled():
    assert isinstance(app, dash.Dash)
    assert app.use_pages is True