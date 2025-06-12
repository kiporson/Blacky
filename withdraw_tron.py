import os
import requests
from main import load_dotenv

TRON_API = "https://api.trongrid.io/wallet/createtransaction"
TRX_ADDRESS = os.getenv("TRX_ADDRESS")
TRX_PK = os.getenv("TRX_PRIVATE_KEY")

def withdraw_trx(amount=10):
    print(f"📤 Withdraw TRX ke {TRX_ADDRESS} sebesar {amount} TRX (mocked template)")
    # Real integration needs tronpy or signing manually (not included here for safety)
    # This is a template for actual signed API call

if __name__ == "__main__":
    withdraw_trx()
