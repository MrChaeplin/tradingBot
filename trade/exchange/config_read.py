from binance_config import binance

class Binance:
    def __init__(self):
        apiKey, apiSecret = binance()
        self.api_key = apiKey
        self.api_secret = apiSecret
    
    def binance_api_key(self):
        return self.api_key

    def binance_secret(self):
        return self.api_secret

binance = Binance ()

print (binance.api_key
       ,binance.api_secret) 
