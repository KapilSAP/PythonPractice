print("Grocery List Program")
grocery_list = []
user_input = None

while user_input != "end":  # Run the loop until user input the end
    user_input = input("Enter Grocery Item: ")  # User Input of grocery list
    if user_input != "end":
        grocery_list.append(user_input)  # Add grocery item into the list

print("Here is your grocery list")
print(grocery_list)  # Once user input the end the print the while list of the items.
