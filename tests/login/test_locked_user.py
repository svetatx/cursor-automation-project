from data.users import LockedUser

def test_locked_user_cannot_login(login):
    login.open()
    login.login(LockedUser.username, LockedUser.password)