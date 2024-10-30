#This program will help to understand looping over the dictionary

bank_account = {
    "name" : "jack",
    "number" : "098849-09940",
    "balance" : 40000
}

# print keys of dictionary
print("Keys are:")
for key in bank_account.keys():
    print(key)

# print values of dictionary
print("Values are:")
for value in bank_account.values():
    print(value)

# print key and values of dictionary
print("Key and Values are:")
for key, value in bank_account.items():
    print(f"{key} - {value}")
