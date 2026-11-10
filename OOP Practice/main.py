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


class Supermarket:
    """Manages the store's money, stock levels, and profits."""
    def __init__(self, name, starting_money):
        self.name = name
        self.money = starting_money
        self.starting_money = starting_money
        self.inventory = [] # A simple list to hold our FoodItem objects
        
    def buy_stock(self, supplier, department, item_name, sell_price, quantity):
        """Buys stock from a supplier and adds it to the inventory list."""
        # Find out how much the supplier charges per item
        cost_per_item = supplier.get_cost(item_name)
        total_cost = cost_per_item * quantity

        if self.money >= total_cost:
            # Deduct money from the supermarket's funds
            self.money -= total_cost
            
            # Check if we already have this item in stock
            found = False
            for item in self.inventory:
                if item.name == item_name:
                    item.quantity += quantity
                    found = True
                    break
            
            # If it's a completely new item, create it and add to list
            if not found:
                new_item = FoodItem(item_name, department, cost_per_item, sell_price, quantity)
                self.inventory.append(new_item)
                
            print(f"Bought {quantity}x {item_name} from {supplier.name} for £{total_cost:.2f}")
        else:
            print("Not enough money to buy this stock!")

