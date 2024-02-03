# A global variable to store the name of the coffee shop
name = "Hot Choco"

# A list of items and their prices
items = {"cafe solo": 1.20, "cortado": 1.50, "cafe con leche": 1.60, "sandwich": 4.5, "cake": 3.5, 
        "ensalada": 5.0, "tea": 1.20, "coca cola": 2.90,"beer": 2.30, "menu del dia": 14.50, 
        "fanta": 2.90, "agua": 1.80, "cheese burger": 9.99,"bikini": 5.50, "empanada": 3.50,
        "tarta de la casa": 6.60, "master burger": 12.50, "bolonesa": 9.99}

# A function to calculate the total cost of an order
# It takes a dictionary of items and quantities as a parameter
# It returns a float value representing the cost
def total_cost(order):
    cost = 0
    for item, quantity in order.items():
        if item in items:
            cost += items[item] * quantity
        else:
            print(f"Sorry, we don't have {item}.")
    return cost

# A function to display the menu and take the user's order
# It returns a dictionary of items and quantities
def take_order():
    print(f"{name}! Welcome, to The Good Coffee! ")
    print("Menu")
    for item, price in items.items():
        print(f"{item}: €{price:.2f}")
    print("Please enter your order, one item per line. Enter 'done' when you are finished.")
    order = {}
    while True:
        item = input()
        if item.lower() == "done":
            break
        else:
            # Check if the item is already in the order
            if item.lower() in order:
                # Increment the quantity by one
                order[item.lower()] += 1
            else:
                # Add the item with quantity one
                order[item.lower()] = 1
    return order

# A function to process the payment and give change
# It takes a float value representing the cost as a parameter
def process_payment(cost):
    print(f"Your total is €{cost:.2f}.")
    print("Please enter the amount of money you are paying.")
    # Use a try and except block to handle errors
    try:
        paid = float(input())
        while paid < cost:
            print(f"That is not enough. You still owe €{cost - paid:.2f}.")
            paid += float(input())
        if paid > cost:
            print(f"Here is your change: €{paid - cost:.2f}.")
        print("Thank you for your visit!")
    except:
        print("Invalid input. Please enter a number.")

# The main program
while True:
    order = take_order()
    cost = total_cost(order)
    process_payment(cost)
    print("Do you want to take another order? Enter 'yes' or 'no'.")
    answer = input()
    if answer.lower() == "no":
        break
print("Goodbye! Thank you for your visit!")
