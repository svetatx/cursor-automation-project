from pages.login_page import LoginPage
from data.users import LockedUser


def test_login_with_invalid_credentials_shows_error(page):
    login = LoginPage(page)
    login.open()
    login.login("invalid_user", "wrong_password")

    login.error.wait_for(state="visible")
    assert "Username and password do not match" in login.error.text_content()
