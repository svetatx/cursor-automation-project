"""Login success tests."""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.users import BASE_URL, USERS


def test_login_success(page):
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(USERS["standard"]["username"], USERS["standard"]["password"])

    inventory = InventoryPage(page)
    inventory.wait_for_products()
