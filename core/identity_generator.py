
import random
import string

def generate_email():
    domains = ['gmail.com', 'yahoo.com', 'outlook.com']
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{name}@{random.choice(domains)}"

def generate_username():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choices(chars, k=length))

def generate_identity():
    return {
        "email": generate_email(),
        "username": generate_username(),
        "password": generate_password()
    }
