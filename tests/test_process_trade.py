import unittest
from unittest.mock import patch
from src.commands.process_trade import process_trade

class TestProcessTrade(unittest.TestCase):

    def setUp(self):
        # Mock stock codes and trade books
        self.stock_codes = {"AAPL", "GOOGL", "MSFT"}
        self.trade_books = {
            ("AAPL", "buy", 1000.00): 100,
            ("GOOGL", "sell", 1500.50): 50
        }

    @patch("src.commands.process_trade.ORDERS_PATH", "mock_orders.csv")
    @patch("src.commands.process_trade.write_orders")
    def test_valid_buy_trade(self, mock_write_orders):
        command = "buy AAPL 1000.00 50"
        result = process_trade(command, self.trade_books, self.stock_codes)
        self.assertEqual(result, "Trade book updated.")
        self.assertEqual(self.trade_books[("AAPL", "buy", 1000.00)], 150)
        mock_write_orders.assert_called_once_with("mock_orders.csv", self.trade_books)

    @patch("src.commands.process_trade.ORDERS_PATH", "mock_orders.csv")
    @patch("src.commands.process_trade.write_orders")
    def test_valid_sell_trade(self, mock_write_orders):
        command = "sell GOOGL 1500.50 50"
        result = process_trade(command, self.trade_books, self.stock_codes)
        self.assertEqual(result, "Trade book updated.")
        self.assertEqual(self.trade_books[("GOOGL", "sell", 1500.50)], 100)
        mock_write_orders.assert_called_once_with("mock_orders.csv", self.trade_books)

    @patch("src.commands.process_trade.ORDERS_PATH", "mock_orders.csv")
    @patch("src.commands.process_trade.write_orders")
    def test_add_new_trade(self, mock_write_orders):
        command = "buy MSFT 2000.00 100"
        result = process_trade(command, self.trade_books, self.stock_codes)
        self.assertEqual(result, "Trade book added.")
        self.assertIn(("MSFT", "buy", 2000.00), self.trade_books)
        self.assertEqual(self.trade_books[("MSFT", "buy", 2000.00)], 100)
        mock_write_orders.assert_called_once_with("mock_orders.csv", self.trade_books)

    def test_invalid_action(self):
        command = "hold AAPL 1000.00 50"
        result = process_trade(command, self.trade_books, self.stock_codes)
        self.assertEqual(result, "Invalid action. Use 'buy' or 'sell'.")

    def test_invalid_stock_code(self):
        command = "buy XYZ 1000.00 50"
        result = process_trade(command, self.trade_books, self.stock_codes)
        self.assertEqual(result, "Invalid stock code.")

    def test_invalid_trade_price(self):
        command = "buy AAPL 0.40 50"
        result = process_trade(command, self.trade_books, self.stock_codes)
        self.assertEqual(result, "Invalid trade price.")

    def test_invalid_trade_volume(self):
        command = "buy AAPL 1000.00 1000001"
        result = process_trade(command, self.trade_books, self.stock_codes)
        self.assertEqual(result, "Invalid trade volume.")

    def test_invalid_command_format(self):
        command = "buy AAPL 1000.00"
        result = process_trade(command, self.trade_books, self.stock_codes)
        self.assertEqual(result, "Invalid command format. Expected format: 'action stock_code price volume'.")

if __name__ == "__main__":
    unittest.main()