balance = float(
    input("Kindly provide account balance? : ")
)  # This will ask balance as input from terminal

if balance:  # if balance in non-zero  -ve or +ve, it will return true
    print("Congratulation, you have some money")
    print(f"Your balance is: {balance} Rs.")
else:  # if equal to  zero, it will return true
    print("Oops, you don't have money")
