lst = [2, 3, 4, 5, 7]

for num in lst:
    print(num)

print("Cheers")


# Access the indices while iterating over a list
# First variable holds the index and second one the value

for index, num in enumerate(lst):
    print(index)
    print(f"{index} - {num}")
