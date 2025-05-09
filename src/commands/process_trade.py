from ..utils.file_handler import write_orders
from ..utils.validation import *
from ..config import ORDERS_PATH

def process_trade(trade_command, trade_books, stock_codes):
    """
    Processes a trade command and updates the trade books accordingly.

    Args:
        trade_command (str): The trade command in the format "action stock_code price volume".
        trade_books (dict): A dictionary to store trade books.
        stock_codes (set): A set of valid stock codes.

    Returns:
        str: A message indicating the result of the operation.
    """
    try:
        # Parse the trade command
        action, order_stock_code, trade_price, volume = trade_command.split()
        trade_price = float(trade_price)
        volume = int(volume)

        # Validate the trade inputs
        if not is_valid_action(action):
            return "Invalid action. Use 'buy' or 'sell'."

        if not is_valid_stock_code(order_stock_code, stock_codes):
            return "Invalid stock code."

        if not is_valid_trade_price(trade_price):
            return "Invalid trade price."

        if not is_valid_trade_volume(volume):
            return "Invalid trade volume."
        
        if not is_valid_trade_command(trade_command):
            return "Invalid command format. Expected format: 'action stock_code price volume'."

        # Create a unique key for the trade
        trade_key = (order_stock_code, action, trade_price)

        # Update or add the trade book entry
        if trade_key in trade_books:
            trade_books[trade_key] += volume
            result_message = "Trade book updated."
        else:
            trade_books[trade_key] = volume
            result_message = "Trade book added."

        # Update the CSV file
        write_orders(ORDERS_PATH, trade_books)

        return result_message

    except ValueError:
        return "Invalid command format. Expected format: 'action stock_code price volume'."
