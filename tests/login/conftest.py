import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login(page: Page) -> LoginPage:
    return LoginPage(page)