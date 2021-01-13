import pytest
from time import sleep
# from playwright.sync_api import Page


def test_visit_admin_dashboard(page, base_url):
    page.goto(base_url)
    page.type('#kw', text="playwright")
    page.click("#su")
    sleep(2)
    assert page.title() == "playwright_百度搜索ssss"
