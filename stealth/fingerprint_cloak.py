
import random

def cloak_fingerprint():
    canvas_noise = random.uniform(0.1, 2.0)
    font_override = random.choice(['Arial', 'Verdana', 'Times New Roman'])
    resolution = random.choice(['1920x1080', '1366x768', '1440x900'])
    print(f"🕵️‍♂️ Cloak aktif - Canvas Noise: {canvas_noise}, Font: {font_override}, Resolution: {resolution}")
