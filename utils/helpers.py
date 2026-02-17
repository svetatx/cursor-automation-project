"""Common helper functions for tests."""

from pathlib import Path


def take_screenshot(page, name: str) -> str:
    """Take a screenshot and return the file path."""
    reports_dir = Path("reports/screenshots")
    reports_dir.mkdir(parents=True, exist_ok=True)
    filepath = reports_dir / f"{name}.png"
    page.screenshot(path=str(filepath))
    return str(filepath)
