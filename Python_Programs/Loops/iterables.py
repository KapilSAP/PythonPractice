# Iterables in Pythons are List, Tuple, Dictionary, Set and String
# Lets check how loop iterates items from Iterables

lst = [23, 45, 67]
i = 0


# While Loop Syntax
while i < len(lst):  # when i = len on list it exit the loop
    print(f"{i} element is {lst[i]}")  # Print element on the each index of the list
    i = i + 1  # increment index

print("Moving On!")

# For loop Syntax
for num in lst:
    print(num)

print("Cheers")


# Access the indices while iterating over a list in for loop

for index, num in enumerate(lst):
    print(index)  # this will print index
    print(f"{index}.{num}")  # this will print value on the index

# Dictionary Syntax
