import pytest
import re

def validate_password(password: str):
    if len(password) < 8:
        return False
    
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"\d", password):
        return False
    
    if re.search(r"[^A-Za-z0-9]", password):
        return False
    return True



@pytest.mark.parametrize("password, expected_result", [
    ("Teo123456", True),
    ("Teo1234#6", False),
    ("teo123456", False),
    ("TEO123456", False),
    ("12345678", True),
])

def test_validate_password(password, expected_result):
    assert validate_password(password) == expected_result
