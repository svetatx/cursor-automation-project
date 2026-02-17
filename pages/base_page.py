"""Base page with shared logic for all page objects."""

from config.settings import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, page, url: str = ""):
        self.page = page
        self.url = url
        self.timeout = DEFAULT_TIMEOUT

    def open(self, url: str = None) -> None:
        """Navigate to the given URL or self.url."""
        target = url or self.url
        self.page.goto(target, timeout=self.timeout)

    def wait_for_load(self, selector: str) -> None:
        """Wait for an element to be visible."""
        self.page.locator(selector).wait_for(state="visible", timeout=self.timeout)
