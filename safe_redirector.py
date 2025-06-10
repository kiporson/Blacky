import random

def get_safe_domain():
    with open("domain_pool.txt", "r") as f:
        domains = [d.strip() for d in f if d.strip()]
    return random.choice(domains)

if __name__ == "__main__":
    print("🌐 Safe redirect domain:", get_safe_domain())
