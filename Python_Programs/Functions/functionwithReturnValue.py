# Write a program to get prepare a grocery list to have item and price together
# print list of items and price
# calculate total of grocery items

def splitter():
   print(80*"-") 

print("Prepare your the grocery list: ")
splitter()
grocery_list = {} # define dictionary similar to collection in JAVA

def put_item_and_price_in_the_list():
    while True:
     item = input("Enter the item (Type 'end' to final the list): ")
     if item == "end":
        break
     item_price = input("Enter the item price : ")
     grocery_list[item] = float(item_price) # set item as key and price as value in dictionary

put_item_and_price_in_the_list()

splitter()
print("here is your grocery list")
for item, price in grocery_list.items(): # get items as key and value from dictionary
    print(f"{item} : {price}") 

def find_item_in_list(some_list, *item_names):  #Variadic function which is taking arbitrary args
   for item_name in item_names:
       for item in some_list:
           if item == item_name:
             print(f"{item_name} is in the list")
             break
       else:
        print(f"{item_name} is not in the list !")

find_item_in_list(grocery_list, "potato", "milk","bread") #one function to take multiple params

splitter()
def groceries_total_cost(grocery_list): 
   total_cost = 0
   for item_price in grocery_list.values(): # get only values from dictionary, for key function is grocery_list.keys()
      total_cost += item_price
   return total_cost    #return value

total_amount = groceries_total_cost(grocery_list)
print(f"Total Amount: {total_amount}")