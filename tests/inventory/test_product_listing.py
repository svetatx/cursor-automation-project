from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.users import StandardUser


def test_product_listing_displays_after_login(page):
    login = LoginPage(page)
    login.open()
    login.login(StandardUser.username, StandardUser.password)

    inventory = InventoryPage(page)
    inventory.wait_for_products()

    assert inventory.get_product_count() > 0
