#AIM: Develop classes for products, customers, and shopping carts. Include methods for adding items
# to the cart, calculating total costs, processing orders, and managing inventory
print("UIN: 251P102, NAME: Harsh Vernekar")


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


    def update_stock(self, quantity):
        self.stock -= quantity


class Customer:
    def __init__(self, name):
        self.name = name


class ShoppingCart:
    def __init__(self):
        self.items = []


    # Add item to cart
    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.update_stock(quantity)
            print(f"{quantity} {product.name} added to cart")
        else:
            print(f"Not enough stock for {product.name}")


    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

    def checkout(self):
        total = self.calculate_total()
        print("\nOrder Summary:")
        for product, quantity in self.items:
            print(f"{product.name} x {quantity}")
        print("Total Amount:", total)
        print("Order Placed Successfully!")


p1 = Product("Laptop", 50000, 5)
p2 = Product("Mouse", 500, 10)

c1 = Customer("Mansi")

cart = ShoppingCart()

cart.add_item(p1, 1)
cart.add_item(p2, 2)

cart.checkout()

