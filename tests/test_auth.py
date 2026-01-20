from user.service import AuthService


def test_register_and_login(test_storage):
    auth = AuthService(test_storage)
    
    # Register admin (programmatically)
    assert auth.royxatdan_otish("admin_main", "admin_pass", "+998 90 111 11 11", role="admin") is True
    
    # Register operator (CLI method)
    assert auth.royxatdan_otish("operator_test", "op_pass", "+998 91 222 22 22", role="operator") is True
    
    # Register user (CLI method)
    assert auth.royxatdan_otish("user_test", "pass123", "+998 93 123 45 67", role="user") is True
    
    # duplicate username
    assert auth.royxatdan_otish("user_test", "x", "+998 93 200 20 20", role="user") is False
    
    # invalid phone
    assert auth.royxatdan_otish("u2", "p", "bad-phone", role="user") is False
    
    # login success/fail
    assert auth.login("user_test", "pass123") is True
    assert auth.login("user_test", "wrong") is False
    
    # Admin can login
    assert auth.login("admin_main", "admin_pass") is True
    
    # Operator can login
    assert auth.login("operator_test", "op_pass") is True
