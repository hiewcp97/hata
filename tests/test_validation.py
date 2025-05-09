import unittest

from src.utils.validation import (
    is_valid_action,
    is_valid_stock_code,
    is_valid_trade_price,
    is_valid_trade_volume,
    is_valid_trade_command,
)

class TestValidation(unittest.TestCase):

    def test_is_valid_action(self):
        self.assertTrue(is_valid_action("buy"))
        self.assertTrue(is_valid_action("sell"))
        self.assertFalse(is_valid_action("hold"))
        self.assertFalse(is_valid_action(""))

    def test_is_valid_stock_code(self):
        stock_codes = {"AAPL", "GOOGL", "MSFT"}
        self.assertTrue(is_valid_stock_code("AAPL", stock_codes))
        self.assertTrue(is_valid_stock_code("GOOGL", stock_codes))
        self.assertFalse(is_valid_stock_code("XYZ", stock_codes))
        self.assertFalse(is_valid_stock_code("", stock_codes))

    def test_is_valid_trade_price(self):
        self.assertTrue(is_valid_trade_price(0.50))
        self.assertTrue(is_valid_trade_price(1000.00))
        self.assertFalse(is_valid_trade_price(0.49))
        self.assertFalse(is_valid_trade_price(-10.00))

    def test_is_valid_trade_volume(self):
        self.assertTrue(is_valid_trade_volume(1))
        self.assertTrue(is_valid_trade_volume(1000000))
        self.assertFalse(is_valid_trade_volume(0))
        self.assertFalse(is_valid_trade_volume(1000001))
        self.assertFalse(is_valid_trade_volume(-5))

    def test_is_valid_trade_command(self):
        self.assertTrue(is_valid_trade_command("buy AAPL 1000.00 100"))
        self.assertTrue(is_valid_trade_command("sell GOOGL 1500.50 200"))
        self.assertFalse(is_valid_trade_command("buy AAPL 1000.00"))
        self.assertFalse(is_valid_trade_command("buy AAPL 1000.00 abc"))
        self.assertFalse(is_valid_trade_command("hold AAPL 1000.00 100"))
        self.assertFalse(is_valid_trade_command(""))

if __name__ == '__main__':
    unittest.main()