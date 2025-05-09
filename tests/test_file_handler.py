import unittest
import os
from src.utils.file_handler import read_stock_codes, read_orders, write_orders

class TestFileHandler(unittest.TestCase):

    def setUp(self):
        # Create test files
        self.stockcode_file = 'tests/mock_stockcode.csv'
        self.orders_file = 'tests/mock_orders.csv'
        self.test_orders_file = 'tests/mock_test_orders.csv'

        with open(self.stockcode_file, 'w') as f:
            f.write("AAPL\nGOOGL\nMSFT\n")

        with open(self.orders_file, 'w') as f:
            f.write("buy,AAPL,1000.00,100\nsell,GOOGL,1500.50,50\n")

    def tearDown(self):
        # Remove test files after tests
        if os.path.exists(self.stockcode_file):
            os.remove(self.stockcode_file)
        if os.path.exists(self.orders_file):
            os.remove(self.orders_file)
        if os.path.exists(self.test_orders_file):
            os.remove(self.test_orders_file)

    def test_read_stock_codes(self):
        stock_codes = read_stock_codes(self.stockcode_file)
        self.assertEqual(stock_codes, {"AAPL", "GOOGL", "MSFT"})

    def test_read_orders(self):
        orders = read_orders(self.orders_file)
        expected_orders = {
            ("AAPL", "buy", 1000.00): 100,
            ("GOOGL", "sell", 1500.50): 50
        }
        self.assertEqual(orders, expected_orders)

    def test_write_orders(self):
        orders = {
            ("AAPL", "buy", 1000.00): 150,
            ("MSFT", "sell", 2000.00): 75
        }
        write_orders(self.test_orders_file, orders)

        with open(self.test_orders_file, 'r') as f:
            content = f.read().strip()

        expected_content = "buy,AAPL,1000.00,150\nsell,MSFT,2000.00,75"
        self.assertEqual(content, expected_content)

if __name__ == "__main__":
    unittest.main()