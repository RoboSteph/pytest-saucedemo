import pytest
import yaml
from playwright.sync_api import sync_playwright

def load_credentials():
    with open("credentials.yaml", "r") as file:
        credentials = yaml.safe_load(file)
    return credentials

@pytest.fixture
def credentials():
    return load_credentials()

@pytest.fixture(scope="function")
def page():
    """Creates fresh browser page for each test"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page() 
        yield page
        context.close()
        browser.close()

def login(page, username, password):
    page.goto("https://www.saucedemo.com/")
    page.fill('input[data-test="username"]', username)
    page.fill('input[data-test="password"]', password)
    page.click('input[data-test="login-button"]')
