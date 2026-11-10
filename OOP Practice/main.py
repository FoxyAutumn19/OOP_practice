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


    def sell_on(self, item_name, quantity):
        """Sells items to a shopper and adds money to the store funds."""
        for item in self.inventory:
            if item.name == item_name:
                if item.quantity >= quantity:
                    # Subtract from stock, add to money
                    item.quantity -= quantity
                    revenue = item.sell_price * quantity
                    self.money += revenue
                    print(f"Sold {quantity}x {item_name} to a shopper for £{revenue:.2f}")
                    return
                else:
                    print(f"Not enough stock! Only {item.quantity} available.")
                    return
        print(f"Sorry, we don't sell {item_name}.")

    
    def check_profit(self):
        """Calculates and prints the profit at any given point."""
        # Profit is current money minus the money we started with
        profit = self.money - self.starting_money
        print(f"Financial Update for {self.name}")
        print(f"Current Cash: £{self.money:.2f}")
        print(f"Total Profit: £{profit:.2f}")



if __name__ == "__main__":
    # Create our supplier and our supermarket
    wholesale_supplier = Supplier("Mega Wholesale")
    my_shop = Supermarket("Friendly Grocer", starting_money=500.00)

    print("1. Buying Stock From Supplier")
    # Supermarket buys goods (specifying department, item name, retail price, and quantity)
    my_shop.buy_stock(wholesale_supplier, "frozen", "Frozen Pizza", sell_price=3.50, quantity=20)
    my_shop.buy_stock(wholesale_supplier, "fresh", "Apples", sell_price=0.80, quantity=50)
    my_shop.buy_stock(wholesale_supplier, "tinned", "Baked Beans", sell_price=0.60, quantity=100)
    my_shop.buy_stock(wholesale_supplier, "pharma", "Aspirin", sell_price=1.20, quantity=30)

    # Let's check our financials after buying stock
    my_shop.check_profit()

    print("2. Selling Stock To Shoppers")
    # Selling items to customers for a profit markup
    my_shop.sell_on("Frozen Pizza", quantity=10)
    my_shop.sell_on("Apples", quantity=40)
    my_shop.sell_on("Baked Beans", quantity=50)
    my_shop.sell_on("Aspirin", quantity=15)

    # Let's check our profit now that we have sold items!
    my_shop.check_profit()