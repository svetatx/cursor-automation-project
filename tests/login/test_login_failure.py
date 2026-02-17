"""Login failure tests."""

from pages.login_page import LoginPage
from data.users import BASE_URL


def test_login_with_invalid_credentials_shows_error(page):
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login("invalid_user", "wrong_password")

    login.error.wait_for(state="visible")
    assert "Username and password do not match" in login.error.text_content()
