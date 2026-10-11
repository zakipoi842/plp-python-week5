# Week 5 Assignment — password_generator.py
# Uses the random and string modules to build random passwords.

import random
import string

def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        # Add one random character from characters to password
        password += random.choice(characters)
    return password

# Make one password using the default length (8)
p1 = make_password()

# Make one password with a length of 12
p2 = make_password(12)

print("Password:", p1)
print("Length:", len(p1))
print("Password:", p2)
print("Length:", len(p2))