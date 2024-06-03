# for Else and while Else  combination,
# though not frequently used  but use full to know. 

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

#let's find out if bread is on the list or not, without for else 
bread_on_list = False
for item in grocery_list:
    if item.strip() == "Bread" or item.strip() == "bread": 
        bread_on_list = True
        print(item)
        break
    print(item)

if not bread_on_list:
    print ("Bread not in the list")


#let's find out if bread is on the list or not, with for else 
bread_on_list = False
for item in grocery_list:
    if item.strip() == "Bread" or item.strip() == "bread": 
        print("Bread is in the list")
        break
else: # this will execute  after full iteration, hence mind the execution time.
    print("Bread is not in the list")   