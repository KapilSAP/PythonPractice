balance = float(input("Kindly provide your balance: "))

if balance != 0:
    print(f"you have balance {balance}")
else:
    print("your balance is zero")

if balance > 0:
    print("You are not in debt")
    if balance > 2000:
        print(f"you are eligible for loan equals to {balance}")
    else:
        print(f"you are not eligible for loan")
