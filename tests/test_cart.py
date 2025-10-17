import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_to_cart(browser):
    
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

 
    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")

    assert inventory_page.get_cart_count() == 1

def test_remove_item_from_cart(browser):
 
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.remove_item_from_cart("Sauce Labs Backpack")

    assert inventory_page.get_cart_count() == 0
