# usually loop break when condition becomes false
# but we can break the loop before condition is false 
# using break keyword and statement 
# continue is also a keyword to skip the iteration - check it out by your self.

print("Grocery list program")

grocery_list = []

while True: #infinite loop
    user_input = input ("Enter the grocery Item, Type End to Finish:")
    if user_input == "end":
        break #break the loop once user input end
    grocery_list.append(user_input)

print("Here is the grocery list")
for item in grocery_list:
    print(item)
