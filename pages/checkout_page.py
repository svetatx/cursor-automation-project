"""Checkout flow page object (steps one, two, complete)."""

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Use stable data-test attributes that match the live Saucedemo app
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.cancel_button = page.locator("[data-test='cancel']")
        self.error = page.locator("[data-test='error']")
        self.complete_header = page.locator(".complete-header")

    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def submit_step_one(self) -> None:
        """Click Continue on checkout step one without assuming success or failure."""
        self.continue_button.click()

    def continue_to_review(self) -> None:
        """Happy-path: step one -> step two of checkout."""
        self.submit_step_one()
        # Wait for the overview page to load before interacting with the Finish button
        self.page.wait_for_url("**/checkout-step-two.html", timeout=self.timeout)

    def finish_checkout(self) -> None:
        # Ensure the Finish button is present and visible before clicking
        self.finish_button.wait_for(state="visible", timeout=self.timeout)
        self.finish_button.click()

    def get_error_message(self) -> str:
        """Return the validation error message shown on checkout step one."""
        self.error.wait_for(state="visible", timeout=self.timeout)
        return self.error.text_content()

    def cancel_checkout(self) -> None:
        """Click the Cancel button (used on step two to navigate back)."""
        self.cancel_button.click()

    def is_order_complete(self) -> bool:
        self.complete_header.wait_for(state="visible", timeout=self.timeout)
        return "Thank you" in self.complete_header.text_content()
