import json

def load_config (filePath):
    with open (filePath, "r") as file:
        config = json.load(file)
    return config

class Binance:
    def __init__(self, file_path):
        config = load_config(file_path)
        self.api_key = config["API_KEY"]
        self.api_secret = config["API_SECRET"]
        self.trade_symbol = config["TRADE_SYMBOL"]
    
    def get_api_key(self):
        return self.api_key

    def get_api_secret(self):
        return self.api_secret

    def get_trade_symbol(self):
        return self.trade_symbol

binance = Binance ("../config/binance.json")