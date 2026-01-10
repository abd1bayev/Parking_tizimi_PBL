from user.service import AuthService


def test_register_and_login(test_storage):
    auth = AuthService(test_storage)
    assert auth.royxatdan_otish("testuser", "pass123", "user@example.com") is True
    # duplicate username
    assert auth.royxatdan_otish("testuser", "x", "user2@example.com") is False
    # invalid email
    assert auth.royxatdan_otish("u2", "p", "bad-email") is False
    # login success/fail
    assert auth.login("testuser", "pass123") is True
    assert auth.login("testuser", "wrong") is False
