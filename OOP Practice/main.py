class FoodItem:
    """Represents any item sold in the store."""
    def __init__(self, name, department, buy_price, sell_price, quantity):
        self.name = name
        self.department = department  # e.g., "frozen", "fresh", "tinned", "pharma"
        self.buy_price = buy_price    # Cost to buy from supplier
        self.sell_price = sell_price  # Price sold to shoppers
        self.quantity = quantity      # How many are in stock

class FoodItem:
    """Represents any item sold in the store."""
    def __init__(self, name, department, buy_price, sell_price, quantity):
        self.name = name
        self.department = department  # e.g., "frozen", "fresh", "tinned", "pharma"
        self.buy_price = buy_price    # Cost to buy from supplier
        self.sell_price = sell_price  # Price sold to shoppers
        self.quantity = quantity      # How many are in stock

class Supplier:
    """Represents a simple supplier that sells items to the supermarket."""
    def __init__(self, name):
        self.name = name

    def get_cost(self, item_name):
        """Returns the wholesale price of an item."""
        if item_name == "Frozen Pizza": return 1.50
        if item_name == "Apples":       return 0.30
        if item_name == "Baked Beans":  return 0.25
        if item_name == "Aspirin":      return 0.50
        return 0.00 # Default if item not found
