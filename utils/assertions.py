"""Custom assertion helpers."""


def assert_url_contains(page, expected: str) -> None:
    """Assert that the current URL contains the expected string."""
    assert expected in page.url, f"Expected URL to contain '{expected}', got {page.url}"
