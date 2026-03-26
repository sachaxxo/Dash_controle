from pages.page3_cb import update_tab_content
from pages.page3 import load_markdown


def test_markdown_files_exist():
    content = load_markdown("expli1.md")
    assert len(content) > 0

def test_update_tab_content():
    result = update_tab_content("tab-1")
    assert result is not None