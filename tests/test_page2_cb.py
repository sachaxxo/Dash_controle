from pages.page2_cb import update_page2_table


def test_update_page2_table_no_filter():
    data, badge = update_page2_table("Toutes", ["Tous"])
    assert isinstance(data, list)
    assert len(data) > 0
    assert "lignes affichées" in badge


def test_update_page2_table_region_filter():
    data, badge = update_page2_table("TotalUS", ["Tous"])
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(row["region"] == "TotalUS" for row in data)
    assert "lignes affichées" in badge


def test_update_page2_table_type_filter():
    data, badge = update_page2_table("Toutes", ["organic"])
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(row["type"] == "organic" for row in data)
    assert "lignes affichées" in badge


def test_update_page2_table_region_and_type_filter():
    data, badge = update_page2_table("TotalUS", ["organic"])
    assert isinstance(data, list)
    assert all(row["region"] == "TotalUS" for row in data)
    assert all(row["type"] == "organic" for row in data)
    assert "lignes affichées" in badge