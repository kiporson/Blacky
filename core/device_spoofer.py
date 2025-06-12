
import random

def spoof_device():
    brands = ['Samsung', 'Xiaomi', 'OnePlus', 'Realme', 'OPPO', 'Vivo', 'Asus']
    models = ['Galaxy A53', 'Redmi Note 12', 'Nord CE 3', 'GT Neo 3', 'F19 Pro', 'Y33s', 'ROG Phone 5']
    android_versions = ['10', '11', '12', '13']

    spoofed_device = {
        'brand': random.choice(brands),
        'model': random.choice(models),
        'android_version': random.choice(android_versions),
        'user_agent': generate_user_agent()
    }
    return spoofed_device

def generate_user_agent():
    base = "Mozilla/5.0 (Linux; Android {version}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    model = random.choice(['SM-A515F', 'M2007J20CI', 'RMX3085', 'CPH2219'])
    version = random.choice(['10', '11', '12', '13'])
    return base.format(version=version, model=model)

# Backwards compatibility wrapper
def spoof():
    return spoof_device()
