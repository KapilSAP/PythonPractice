balance = float(input("Please enter your bank balance : "))

if balance < 0:
    print(f"You are in debt, your balance is: {balance}")
elif balance > 2000:
    print("Your are not in debt")
    print(f"You can ask for loan, your balance is: {balance}")
else:
    print("you are not eligible for loan")
