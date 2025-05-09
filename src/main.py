import sys
import os
from .utils.file_handler import read_stock_codes, read_orders
from .commands.process_trade import process_trade
from .config import STOCK_CODES_PATH, ORDERS_PATH

def main():
    stock_codes = read_stock_codes(STOCK_CODES_PATH)
    trade_books = read_orders(ORDERS_PATH)
    
    if len(sys.argv) == 1:
        # Interactive mode
        print("$", end=" ")
        while True:
            command = input().strip()
            if command.lower() == "exit":
                break
            print(process_trade(command, trade_books, stock_codes))
            print("$", end=" ")
    elif len(sys.argv) == 2:
        # File processing mode
        file_path = sys.argv[1]
        if not os.path.isfile(file_path):
            print(f"Error: File '{file_path}' not found.")
            return
        
        with open(file_path, 'r') as file:
            for line in file:
                print(process_trade(line.strip(), trade_books, stock_codes))
    else:
        print("Usage: stockbroker.py [file_path]")

if __name__ == "__main__":
    main()