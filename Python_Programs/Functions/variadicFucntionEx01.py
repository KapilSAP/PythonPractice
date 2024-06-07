print("here is the grocery list: ")

grocery_list = []

def put_item_in_the_list():
    while True:
     item = input("Enter the item (Type 'end' to final the list): ")
     if item == "end":
        break
     else:
         grocery_list.append(item)

put_item_in_the_list()

def find_item_in_list(some_list, *item_names):  #Variadic function which is taking arbitrary args
   for item_name in item_names:
       for item in some_list:
           if item == item_name:
             print(f"{item_name} is in the list")
             break
       else:
        print(f"{item_name} is not in the list !")

find_item_in_list(grocery_list, "potato", "milk","bread") #one function to take multiple params
    