import pytest
import yaml
from playwright.sync_api import sync_playwright
from conftest import login

def test_login(page, credentials):
    login(page, credentials["username"], credentials["password"])
    # Ensure no login error message appears
    assert not page.is_visible('h3[data-test="error"]')
    # List of products should be visible
    assert page.is_visible('div.inventory_list')
    # Verify URL after login 
    assert page.url == "https://www.saucedemo.com/inventory.html"
    # Open menu
    page.click('button[id="react-burger-menu-btn"]')
    # Logout button should be visible
    assert page.is_visible('a[data-test="logout-sidebar-link"]')
    page.close()

def test_invalid_user(page, credentials):
    page.goto("https://www.saucedemo.com/")
    page.fill('input[id="user-name"]', "invalid_user")
    page.fill('input[id="password"]', credentials["password"])
    page.click('input[type="submit"]')
    # Login error message should be visible
    assert page.is_visible('h3[data-test="error"]')
    # List of products should not be visible
    assert not page.is_visible('div.inventory_list')
    assert page.url == "https://www.saucedemo.com/"

def test_invalid_password(page, credentials):
    page.goto("https://www.saucedemo.com/")
    page.fill('input[id="user-name"]', credentials["username"])
    page.fill('input[id="password"]', "invalid_password")
    page.click('input[type="submit"]')
    # Login error message should be visible
    assert page.is_visible('h3[data-test="error"]') 
    # List of products should not be visible
    assert not page.is_visible('div.inventory_list') 
    assert page.url == "https://www.saucedemo.com/"

def test_logout(page, credentials):
    login(page, credentials["username"], credentials["password"])
    # List of products should be visible
    assert page.is_visible('div.inventory_list') 
    page.click('button[id="react-burger-menu-btn"]')
    #Select logout
    page.click('a[data-test="logout-sidebar-link"]') 
    assert page.is_visible('input[data-test="username"]') 
    # List of products should not be visible after logout
    assert not page.is_visible('div.inventory_list') 
    # Verify URL after logout
    assert page.url == "https://www.saucedemo.com/" 
    page.close()

def test_locked_user(page, credentials):
    page.goto("https://www.saucedemo.com/")
    page.fill('input[id="user-name"]', credentials["locked_user"])
    page.fill('input[id="password"]', credentials["password"])
    page.click('input[type="submit"]')
    # Login error message should be visible
    locked_error_message = "Epic sadface: Sorry, this user has been locked out."
    assert page.inner_text('h3[data-test="error"]') == locked_error_message
    # List of products should not be visible
    assert not page.is_visible('div.inventory_list')
    assert page.url == "https://www.saucedemo.com/"