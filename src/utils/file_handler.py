def read_stock_codes(file_path):
    stock_codes = set()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                stock_code = line.strip()
                if stock_code:  # Ensure the line is not empty
                    stock_codes.add(stock_code)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return stock_codes

def read_orders(file_path):
    orders = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                order = line.strip().split(',')
                if len(order) == 4:
                    action, stock_code, price, volume = order
                    price = float(price)
                    volume = int(volume)
                    # Use a tuple (stock_code, action, price) as the key
                    orders[(stock_code, action, price)] = volume
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except ValueError:
        print(f"Error: Invalid data format in file {file_path}.")
    return orders

def write_orders(file_path, orders):
    try:
        with open(file_path, 'w') as file:
            for (stock_code, action, price), volume in orders.items():
                # Convert price and volume to strings and format price to 2 decimal places
                file.write(f"{action},{stock_code},{price:.2f},{volume}\n")
    except Exception as e:
        print(f"Error: Could not write to file {file_path}. {e}")