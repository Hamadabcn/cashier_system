# Define a class for products
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price} x {self.quantity}"

# Define a class for inventory
class Inventory:
    def __init__(self):
        self.products = {} # A dictionary of products

    def add_product(self, product):
        # Add a product to the inventory or update its quantity if it already exists
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def remove_product(self, product):
        # Remove a product from the inventory or reduce its quantity if it exists
        if product.name in self.products:
            if self.products[product.name].quantity >= product.quantity:
                self.products[product.name].quantity -= product.quantity
                if self.products[product.name].quantity == 0:
                    del self.products[product.name]
            else:
                print(f"Cannot remove {product}. Not enough in stock.")
        else:
            print(f"Cannot remove {product}. Product not found.")

    def total_value(self):
        # Calculate the total value of the inventory
        value = 0
        for product in self.products.values():
            value += product.price * product.quantity
        return value

    def missing_products(self):
        # Return a list of products that have zero quantity in the inventory
        missing = []
        for product in self.products.values():
            if product.quantity == 0:
                missing.append(product)
        return missing

    def __str__(self):
        # Return a string representation of the inventory
        output = "Inventory:\n"
        for product in self.products.values():
            output += str(product) + "\n"
        output += f"Total value: €{self.total_value()}"
        return output

# Define a function to get user input and validate it
def get_input(prompt, type_):
    # Loop until the user enters a valid input of the specified type
    while True:
        try:
            input_ = type_(input(prompt))
            return input_
        except ValueError:
            print(f"Invalid input. Please enter a {type_.__name__}.")

# Create an inventory object
inventory = Inventory()

# Create a loop for the workers to interact with the inventory
while True:
    # Print a menu of options
    print("What do you want to do?")
    print("1. Add a product")
    print("2. Remove a product")
    print("3. View the inventory")
    print("4. View the missing products")
    print("5. Quit")

    # Get the user's choice and validate it
    choice = get_input("Enter your choice: ", int)
    while choice not in [1, 2, 3, 4, 5]:
        print("Invalid choice. Please enter a number between 1 and 5.")
        choice = get_input("Enter your choice: ", int)

    # Perform the corresponding action based on the user's choice
    if choice == 1:
        # Add a product to the inventory
        name = input("Enter the name of the product: ")
        price = get_input("Enter the price of the product: ", float)
        quantity = get_input("Enter the quantity of the product: ", int)
        product = Product(name, price, quantity)
        inventory.add_product(product)
        print(f"Added {product} to the inventory.")
    elif choice == 2:
        # Remove a product from the inventory
        name = input("Enter the name of the product: ")
        quantity = get_input("Enter the quantity of the product: ", int)
        product = Product(name, 0, quantity) # Price is not relevant for removal
        inventory.remove_product(product)
        print(f"Removed {product} from the inventory.")
    elif choice == 3:
        # View the inventory
        print(inventory)
    elif choice == 4:
        # View the missing products
        missing = inventory.missing_products()
        if missing:
            print("The following products are missing:")
            for product in missing:
                print(product)
        else:
            print("No products are missing.")
    else:
        # Quit the program
        break

# Print a farewell message
print("Thank you for using the inventory program.")
