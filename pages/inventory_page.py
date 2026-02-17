"""Inventory / product listing page object."""

from pages.base_page import BasePage
from data.constants import INVENTORY_LIST_SELECTOR, INVENTORY_ITEM_SELECTOR


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_list = page.locator(INVENTORY_LIST_SELECTOR)
        self.inventory_items = page.locator(INVENTORY_ITEM_SELECTOR)
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.add_to_cart_buttons = page.locator("button.btn_inventory")

    def wait_for_products(self) -> None:
        self.inventory_list.wait_for(state="visible", timeout=self.timeout)

    def get_product_count(self) -> int:
        return self.inventory_items.count()

    def add_product_to_cart(self, index: int = 0) -> None:
        self.add_to_cart_buttons.nth(index).click()

    def get_cart_badge_count(self) -> int:
        """Return the numeric value shown in the cart badge, or 0 if hidden."""
        if not self.cart_badge.is_visible():
            return 0
        return int(self.cart_badge.text_content())

    def go_to_cart(self) -> None:
        self.cart_link.click()
