import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(browser):
   
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

   
    checkout_page = CheckoutPage(browser)
    checkout_page.start_checkout()
    checkout_page.fill_information("Clarenz", "Yumul", "12345")
    checkout_page.finish_checkout()

  
    success_message = checkout_page.get_success_message()
    assert "THANK YOU" in success_message.upper()
