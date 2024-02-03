# Import the calendar and datetime modules

import calendar
import datetime

# Define a function to create a menu dictionary from a text file

def create_menu_dict(filename):
    
    # Open the file and read the lines
    
    with open(filename) as f:
        lines = f.readlines()

    # Initialize an empty dictionary
    
    menu_dict = {}

    # Loop through the lines
    
    for line in lines:
        # Split the line by comma
        
        items = line.split(",")

        # Get the date, name and price of the menu item
        
        date = items[0].strip()
        name = items[1].strip()
        price = float(items[2].strip())

        # Add the menu item to the dictionary with the date as the key
        
        menu_dict[date] = (name, price)

    # Return the menu dictionary
    
    return menu_dict

# Define a function to display the reminder calendar

def display_reminder_calendar():
    
    # Get the current year and month
    
    year = datetime.date.today().year
    month = datetime.date.today().month

    # Create a menu dictionary from a text file
    
    menu_dict = create_menu_dict("menu.txt")

    # Print the calendar for that month and year
    
    print(calendar.month(year, month))

    # Loop through the dates in the menu dictionary
    
    for date in menu_dict:
        # Convert the date string to a datetime object
        
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")

        # Check if the date is in the current month and year
        
        if date_obj.year == year and date_obj.month == month:
            
            # Get the name and price of the menu item
            
            name, price = menu_dict[date]

            # Print the reminder message
            
            print(f"On {date}, try our {name} for only ${price:.2f}!")
            