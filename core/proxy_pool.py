
import random

PROXIES = [
    "http://123.45.67.89:8080",
    "http://98.76.54.32:3128",
    "http://111.222.333.444:8000",
    "http://185.45.12.99:1080",
    "http://200.100.50.25:9999"
]

def get_random_proxy():
    return random.choice(PROXIES)

def get_all_proxies():
    return PROXIES
