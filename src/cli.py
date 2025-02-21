def optionSelect():
    optionList = ["Print List of meals", "Edit meal"]
    for option in optionList:
        optionIndex = (optionList.index(option)+1)
        print(f"[{optionIndex}]", option)
    selectedOption = int(input("Select an option \n"))
    selectedOption = selectedOption-1
    return(optionList[selectedOption])



print(f"\nYou have selected: {optionSelect()}\n")
