## Import libraries

import sqlite3


## Define functions

def optionSelect():
    # List options
    optionList = ["Add Meal", "Remove Meal"]
    # Print available options
    for option in optionList:
        optionIndex = (optionList.index(option)+1)
        print(f"[{optionIndex}]", option)
    # Select Option
    selectedOption = int(input("Select an option \n"))
    # Purely for display!!! So if user selects 1 it is actually index 0, as options start from 1
    displayOption = selectedOption-1
    print(f"\nYou have selected: {optionList[displayOption]}\n")
    # Returns the actual selectedOption which is used in later decision making
    return(selectedOption)


def optionRouter(option):
    # Checks if input is correct type
    if type(option) != int:
        print("Please enter a number")
        optionSelect()
    # Checks if input is in correct range
    if option > 1 and option > 0:
        print("Please select a number specified")
        optionSelect()
    # Sends user to addMeal function
    elif option == 1:
        addMeal()
    else:
        pass


def addMeal():
    meal_name = input("Meal name: ")
    meal_cook_time = input("How long does it take to cook? (Not including prep time, just time to cook!): ")
    meal_prep_time = input("How long does it take to prep?: ")
    meal_complexity = input("How complex is the meal? (Easy, Medium, Hard): ")

    cur.execute(f"""
        INSERT INTO meals (meal_name, meal_cook_time, meal_prep_time, meal_complexity)
        VALUES ('{meal_name}', '{meal_cook_time}', '{meal_prep_time}', '{meal_complexity}') 
                """)
    con.commit()



## Main

# Connecting to DB
con = sqlite3.connect("meals.db")
cur = con.cursor()

# Getting option from input
option = optionSelect()


# Routing to function depending on input
optionRouter(option)