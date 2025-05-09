class TradeBook:
    def __init__(self, action, stock_code, trade_price, volume):
        self.action = action
        self.stock_code = stock_code
        self.trade_price = trade_price
        self.volume = volume

    def adjust_volume(self, incoming_action, incoming_volume):
        if self.action == incoming_action:
            self.volume += incoming_volume
        else:
            self.volume -= incoming_volume

        if self.volume < 0:
            self.volume = 0  # Ensure volume does not go negative

    def __str__(self):
        return f"{self.action},{self.stock_code},{self.trade_price:.2f},{self.volume}"