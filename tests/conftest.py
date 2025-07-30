import pytest
import yaml
from playwright.sync_api import sync_playwright

def load_credentials():
    with open("credentials.yaml", "r") as file:
        credentials = yaml.safe_load(file)
    return credentials

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context() # ensures each test runs in fresh isolated browser context/profile
        page = context.new_page() # new browser tab
        yield page
        context.close()
        browser.close()

def login(browser):
    credentials = load_credentials()
    page = browser
    page.goto("https://www.saucedemo.com/")
    page.fill('input[data-test="username"]', credentials["username"])
    page.fill('input[data-test="password"]', credentials["password"])
    page.click('input[data-test="login-button"]')
