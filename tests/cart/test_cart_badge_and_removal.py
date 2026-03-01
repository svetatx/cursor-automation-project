from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.users import StandardUser


def login_and_open_inventory(page) -> InventoryPage:
    """Helper to log in and land on the inventory page."""
    login = LoginPage(page)
    login.open()
    login.login(StandardUser.username, StandardUser.password)

    inventory = InventoryPage(page)
    inventory.wait_for_products()
    return inventory


def test_add_single_item_updates_cart_badge(page):
    inventory = login_and_open_inventory(page)

    inventory.add_product_to_cart(0)

    assert inventory.get_cart_badge_count() == 1


def test_add_multiple_items_updates_cart_badge(page):
    inventory = login_and_open_inventory(page)

    inventory.add_product_to_cart(0)
    inventory.add_product_to_cart(1)
    inventory.add_product_to_cart(2)

    assert inventory.get_cart_badge_count() == 3


def test_remove_item_updates_cart_badge(page):
    inventory = login_and_open_inventory(page)

    # Add two items first so we can remove one
    inventory.add_product_to_cart(0)
    inventory.add_product_to_cart(1)
    assert inventory.get_cart_badge_count() == 2

    # The same button toggles between Add to cart / Remove
    inventory.add_product_to_cart(0)

    assert inventory.get_cart_badge_count() == 1


def test_add_from_inventory_and_navigate_to_cart(page):
    inventory = login_and_open_inventory(page)

    inventory.add_product_to_cart(0)
    inventory.go_to_cart()

    cart = CartPage(page)
    cart.wait_for_cart()

    assert cart.get_cart_item_count() == 1

