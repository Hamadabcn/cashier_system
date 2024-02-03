# A simple shopping list reminder program

# Define a list of items to buy

items = ["milk", "eggs", "bread", "cheese", "butter"]

# Define a function to check if an item is in the list

def check_item(item):
  if item in items:
    print(f"You need to buy {item}.")
  else:
    print(f"You don't need to buy {item}.")

# Define a function to add an item to the list

def add_item(item):
  items.append(item)
  print(f"{item} has been added to the list.")

# Define a loop variable to control the program

loop = True

# Start the loop

while loop:
    
  # Ask the user to enter an item
  
  item = input("Enter an item: ")

  # Check if the user wants to quit
  
  if item.lower() == "quit":
      
    # Set the loop variable to False
    
    loop = False
    
    # Print a farewell message
    
    print("Thank you for using the shopping List App . Goodbye!")
  else:
      
    # Check if the item is already in the list
    
    if item in items:
        
      # Call the function to check the item
      
      check_item(item)
    else:
        
      # Ask the user if they want to add the item to the list
      
      answer = input(f"Do you want to add {item} to the list? (y/n) ")
      if answer.lower() == "y":
          
        # Call the function to add the item to the list
        
        add_item(item)
      else:
        print("Okay, Do you want to add anything else?")
        