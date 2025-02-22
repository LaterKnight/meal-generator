## Import libraries


import sqlite3



## Define functions

def optionSelect():
    optionList = ["Print List of meals", "Edit meal"]
    for option in optionList:
        optionIndex = (optionList.index(option)+1)
        print(f"[{optionIndex}]", option)
    selectedOption = int(input("Select an option \n"))
    selectedOption = selectedOption-1
    return(optionList[selectedOption])


## Main

con = sqlite3.connect("meals.db")
cur = con.cursor()

print(f"\nYou have selected: {optionSelect()}\n")
