from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../../.env")

def binance () :
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    return api_key, api_secret