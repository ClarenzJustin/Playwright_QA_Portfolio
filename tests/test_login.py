import pytest
from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

   
    assert "inventory" in browser.url

def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("wrong_user", "wrong_pass")

    
    assert "Epic sadface" in login_page.get_error_message()
    