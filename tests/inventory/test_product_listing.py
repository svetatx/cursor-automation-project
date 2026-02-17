"""Inventory / product listing tests."""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.users import BASE_URL, USERS


def test_product_listing_displays_after_login(page):
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(USERS["standard"]["username"], USERS["standard"]["password"])

    inventory = InventoryPage(page)
    inventory.wait_for_products()

    assert inventory.get_product_count() > 0
