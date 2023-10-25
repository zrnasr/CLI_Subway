import re

def validate_password(password):
    assert re.fullmatch(r'^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z]).{8,}$', password), ("Invalid password. should contains a-z, 0-9, and at least 8 characters.")