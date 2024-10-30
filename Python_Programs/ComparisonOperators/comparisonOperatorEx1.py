balance = float(input("Kindly provide your balance: "))  #Note: input is pythion function to drive intpu from the user

if balance != 0:
    print(f"you have balance {balance}")
else:
    print("your balance is zero")

if balance > 0:
    print("You are not in debt")
    if balance > 2000:
        print(f"you are eligible for loan equals to {balance}") #Note: f string is way to format strings in python
    else:
        print(f"you are not eligible for loan")
