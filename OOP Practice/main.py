class FoodItem:
    """Represents any item sold in the store."""
    def __init__(self, name, department, buy_price, sell_price, quantity):
        self.name = name
        self.department = department  # e.g., "frozen", "fresh", "tinned", "pharma"
        self.buy_price = buy_price    # Cost to buy from supplier
        self.sell_price = sell_price  # Price sold to shoppers
        self.quantity = quantity      # How many are in stock

