print("Enter the Grocery Items")

grocery_lst = []
user_input = None

while user_input != "end":
    user_input = input("Enter the item: ")
    if (
        user_input != "end" and user_input not in grocery_lst
    ):  # and condition to remove duplicates
        grocery_lst.append(user_input)

print("Here is your grocery items: ")
print(grocery_lst)  # Print all via print

# or print via iterators

i = 0
while i < len(grocery_lst):
    print(f"{grocery_lst[i]}")
    i = i + 1
