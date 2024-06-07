# Program to demonstrate how to use functions in python 
# 1. Starts with def key words which holds the function definitions
# 2. In Python, keywords arguments can be passed to avoid positioning error - line 27
# 3. In Python default argument as optional parameter - line 18 and 30

print("Grocery list program")

grocery_list = []

while True: 
    user_input = input("Enter the grocery item, type ed to end the list: ")
    if user_input == "end":
        break
    grocery_list.append(user_input)

print(grocery_list)

def find_in_list(lst, item="bread"):  #Optional parameter with default value is bread, always define after the normal arguments
    for itm in lst:
        if item.strip() == itm.strip():
            print(f"{item} found in the list")
            break
    else:
          print(f"{item} not found in the list")


find_in_list(item="milk", lst=grocery_list) #map the variable to keywords argument to avoid position errors
find_in_list(grocery_list, "bread")
find_in_list(grocery_list, "butter")
find_in_list(grocery_list) # function without arguments
#def find_in_list_error(item="bread", lst): # This line will give an error as default args is first.