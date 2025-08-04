import pytest
import yaml
from playwright.sync_api import sync_playwright

def load_credentials():
    """Load credentials from YAML file"""
    with open("credentials.yaml", "r") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="session")
def credentials():
    return load_credentials()

@pytest.fixture(scope="session")
def playwright_instance():
    """Create a Playwright instance for the session"""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright_instance):
    """Create a fresh browser instance for each test"""
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()
    
@pytest.fixture(scope="function")
def page(browser):
    """Creates fresh browser page for each test"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def login(page, username, password):
    page.goto("https://www.saucedemo.com/")
    page.fill('input[data-test="username"]', username)
    page.fill('input[data-test="password"]', password)
    page.click('input[data-test="login-button"]')
