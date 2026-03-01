from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.users import StandardUser


def test_add_product_to_cart_and_view(page):
    login = LoginPage(page)
    login.open()
    login.login(StandardUser.username, StandardUser.password)

    inventory = InventoryPage(page)
    inventory.wait_for_products()
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()

    cart = CartPage(page)
    cart.wait_for_cart()

    assert cart.get_cart_item_count() >= 1
