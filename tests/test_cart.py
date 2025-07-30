import pytest
import random
import playwright.sync_api as sync_playwright
from conftest import login

def test_add_random_item_to_cart(page):
    login(page)
    assert page.is_visible('div.inventory_list')  # Ensure inventory list is visible

    all_items = page.query_selector_all('div.inventory_item')
    assert all_items, "No inventory items found!"

    random_item = random.choice(all_items)

    # Select add-to-cart button for the random item
    add_button = random_item.query_selector('button[data-test^="add-to-cart"]')
    assert add_button, "No add-to-cart button found for the selected item!"
    add_button.click()

    # Verify item was added to cart by checking cart badge 
    assert page.is_visible('.shopping_cart_badge')  # Check if item was added to cart
    assert page.inner_text('.shopping_cart_badge') == '1'  # Ensure cart bad
    page.pause()