"""Shopping cart page object."""

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_list = page.locator(".cart_list")
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator(".checkout_button")
        self.continue_shopping = page.locator("a.btn_secondary")

    def wait_for_cart(self) -> None:
        self.cart_list.wait_for(state="visible", timeout=self.timeout)

    def get_cart_item_count(self) -> int:
        return self.cart_items.count()

    def proceed_to_checkout(self) -> None:
        self.checkout_button.click()
