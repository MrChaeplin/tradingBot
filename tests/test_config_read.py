import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../exchanges')))

from config_read import Binance

class TestBinanceConfig(unittest.TestCase):
    def test_load_config(self):
        
        binance = Binance(os.path.join(os.path.dirname(__file__), "../config/binance.json"))
        self.assertEqual(binance.get_api_key(), "fake_api_key_123")
        self.assertEqual(binance.get_api_secret(), "fake_api_secret_123")
        self.assertEqual(binance.get_trade_symbol(), "BTCUSDT")

if __name__ == "__main__":
    unittest.main()
