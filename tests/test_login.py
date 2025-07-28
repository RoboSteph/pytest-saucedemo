import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context() # ensures each test runs in fresh isolated browser context/profile
        page = context.new_page() # new browser tab
        yield page
        browser.close()

def test_login(browser):
    page = browser
    page.goto("https://www.saucedemo.com/")
    page.fill('input[data-test="username"]', "standard_user")
    page.fill('input[data-test="password"]', "secret_sauce")
    page.click('input[data-test="login-button"]')
    assert not page.is_visible('h3[data-test="error"]') # check for login error message
    assert page.is_visible('div.inventory_list') # check if list of products is visible
    assert page.url == "https://www.saucedemo.com/inventory.html"
    page.click('button[id="react-burger-menu-btn"]') # open the sidebar menu
    # page.pause()
    assert page.is_visible('a[data-test="logout-sidebar-link"]') # check if logout button is visible to ensure logged in
    page.close()