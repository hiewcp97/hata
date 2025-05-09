import os
import json
import sys

# Load configuration from the config.json file
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    if not os.path.isfile(config_path):
        print(f"Error: Configuration file '{config_path}' not found.")
        sys.exit(1)
    
    with open(config_path, 'r') as config_file:
        try:
            config = json.load(config_file)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in configuration file.")
            sys.exit(1)
    
    # Validate paths in the config
    stock_codes_path = config.get("stock_codes_path")
    orders_path = config.get("orders_path")
    
    if not stock_codes_path or not os.path.isfile(stock_codes_path):
        print(f"Error: Invalid or missing stock codes file path: {stock_codes_path}")
        sys.exit(1)
    
    if not orders_path or not os.path.isfile(orders_path):
        print(f"Error: Invalid or missing orders file path: {orders_path}")
        sys.exit(1)
    
    return stock_codes_path, orders_path

# Load the paths as constants
STOCK_CODES_PATH, ORDERS_PATH = load_config()