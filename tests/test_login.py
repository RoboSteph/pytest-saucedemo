import pytest
import yaml
from playwright.sync_api import sync_playwright
from conftest import login

def test_login(page):
    login(page)
    assert not page.is_visible('h3[data-test="error"]') # check for login error message
    assert page.is_visible('div.inventory_list') # check if list of products is visible
    assert page.url == "https://www.saucedemo.com/inventory.html"
    page.click('button[id="react-burger-menu-btn"]') # open the sidebar menu
    # page.pause()
    assert page.is_visible('a[data-test="logout-sidebar-link"]') # check if logout button is visible to ensure logged in
    page.close()