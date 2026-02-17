"""Locked user login tests."""

from pages.login_page import LoginPage
from data.users import BASE_URL, USERS


def test_locked_user_cannot_login(page):
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(USERS["locked"]["username"], USERS["locked"]["password"])

    login.error.wait_for(state="visible")
    assert "locked out" in login.error.text_content().lower()
