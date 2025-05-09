# Stockbroker Application

## Overview
The Stockbroker Application is a command-line tool designed to help stockbrokers manage trade orders from investors. It allows users to record trades, adjust existing trade volumes, and maintain a record of valid stock codes.

## Features
- Record incoming trade orders via command line.
- Adjust trade volumes for existing trade books.
- Create new trade books if none exist for a given stock code.
- Validate stock codes against a predefined list.
- Support for both interactive mode and file processing mode.

## Project Structure
```
stockbroker-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── config.py              # Initialize and load the config into application
│   ├── config.json            # Config the application
│   ├── utils
│   │   ├── file_handler.py     # Functions for file operations
│   │   └── validation.py       # Functions for input validation
│   ├── models
│   │   └── trade_book.py       # TradeBook class definition
│   └── commands
│       └── process_trade.py    # Trade processing logic
├── data
│   ├── stockcode.csv          # Valid stock codes
│   └── orders.csv             # Existing trade orders
├── tests
│   ├── test_file_handler.py    # Unit tests for file_handler.py
│   ├── test_validation.py      # Unit tests for validation.py
│   └── test_process_trade.py   # Unit tests for process_trade.py
├── stockbroker.sh              # Shell script for Linux execution
├── stockbroker.bat             # Batch file for Windows execution
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd hata
   ```

2. Create and activate a virtual environment
   Ubuntu/MacOS
   ```
   python3 -m venv .venv
   source .venv/bin/activate 
   ```
   Windows
   ```
   python3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Prepare the data files:
   - Ensure `stockcode.csv` contains valid stock codes.
   - Populate `orders.csv` with existing trade orders if needed.

7. Replace the config files path:
   ```
   {
      "orders_path": "{{orders_path}}",
      "stock_codes_path": "{{stock_codes_path}}"
   }
   ```

## Usage
### Interactive Mode
To run the application in interactive mode, execute:
Ubuntu/MacOS
```
sh ./stockbroker.sh
```
Windows
```
./stockbroker.bat
```
You will see a prompt (`$`) where you can enter trade commands. Type `exit` to quit.

### File Processing Mode
To process trade orders from a file, execute:
Ubuntu/MacOS
```
sh ./stockbroker.sh <path-to-orders-file>
```
Windows
Ubuntu/MacOS
```
./stockbroker.bat <path-to-orders-file>
```
Replace `<path-to-orders-file>` with the path to your text file containing trade orders.

## Example Commands
- To buy stocks:
```
$ buy AAPL 1000.00 100
```
- To sell stocks:
```
$ sell GOOGL 1500.50 50
```

## Running Tests
1. Execute the test suite:
```
pytest
```
