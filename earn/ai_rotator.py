import json
import random

# Simulasi performa dari database atau log
CPA_OFFERS = [
    {"url": "https://cpa1.com/offer", "score": 88},
    {"url": "https://cpa2.com/track", "score": 73},
    {"url": "https://cpa3.com/lead", "score": 92},
    {"url": "https://cpa4.com/conversion", "score": 65},
    {"url": "https://cpa5.com/register", "score": 79}
]

def select_best_offer(threshold=75):
    filtered = [o for o in CPA_OFFERS if o["score"] >= threshold]
    if not filtered:
        return random.choice(CPA_OFFERS)
    return sorted(filtered, key=lambda x: -x["score"])[0]

if __name__ == "__main__":
    best = select_best_offer()
    print("🎯 AI ROTATOR memilih:", best["url"])
