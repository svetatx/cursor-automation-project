from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.users import StandardUser


def _start_checkout_with_single_item(page) -> CheckoutPage:
    """Shared setup: login, add one item to cart, navigate to checkout step one."""
    login = LoginPage(page)
    login.open()
    login.login(StandardUser.username, StandardUser.password)

    inventory = InventoryPage(page)
    inventory.wait_for_products()
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()

    cart = CartPage(page)
    cart.wait_for_cart()
    cart.proceed_to_checkout()

    return CheckoutPage(page)


def test_checkout_flow_completes_successfully(page):
    """Happy path: Login → add item → checkout → success page."""
    checkout = _start_checkout_with_single_item(page)

    checkout.fill_shipping_info("Test", "User", "12345")
    checkout.continue_to_review()
    checkout.finish_checkout()

    assert checkout.is_order_complete()


def test_checkout_validation_missing_first_name(page):
    """Validation error when First Name is missing."""
    checkout = _start_checkout_with_single_item(page)

    checkout.fill_shipping_info("", "User", "12345")
    checkout.submit_step_one()

    error_text = checkout.get_error_message()
    assert "First Name is required" in error_text


def test_checkout_validation_missing_postal_code(page):
    """Validation error when Zip/Postal Code is missing."""
    checkout = _start_checkout_with_single_item(page)

    checkout.fill_shipping_info("Test", "User", "")
    checkout.submit_step_one()

    error_text = checkout.get_error_message()
    assert "Postal Code is required" in error_text


def test_checkout_back_navigation_from_overview(page):
    """Back navigation works from overview (step two) via Cancel button."""
    checkout = _start_checkout_with_single_item(page)

    checkout.fill_shipping_info("Test", "User", "12345")
    checkout.continue_to_review()

    # On checkout overview, Cancel should navigate back to the inventory page
    checkout.cancel_checkout()

    assert "/inventory.html" in page.url
