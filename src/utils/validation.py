def is_valid_action(action):
    """
    Validates if the action is either 'buy' or 'sell'.

    Args:
        action (str): The action to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return action in ["buy", "sell"]

def is_valid_stock_code(stock_code, stock_codes):
    """
    Validates if the stock code exists in the list of valid stock codes.

    Args:
        stock_code (str): The stock code to validate.
        stock_codes (set): A set of valid stock codes.

    Returns:
        bool: True if valid, False otherwise.
    """
    return stock_code in stock_codes

def is_valid_trade_price(trade_price):
    """
    Validates if the trade price is greater than or equal to 0.50.

    Args:
        trade_price (float): The trade price to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return trade_price >= 0.50

def is_valid_trade_volume(volume):
    """
    Validates if the trade volume is within the range 1 to 1,000,000.

    Args:
        volume (int): The trade volume to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return 1 <= volume <= 1000000

def is_valid_trade_command(trade_command):
    """
    Validates the format of the trade command.

    Args:
        trade_command (str): The trade command to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    parts = trade_command.split()
    return len(parts) == 4 and parts[0] in ["buy", "sell"] and parts[1].isalpha() and parts[2].replace('.', '', 1).isdigit() and parts[3].isdigit()