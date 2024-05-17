balance = float(input("Please enter your account balance: "))
age = int(input("Please enter your age: "))
have_job_input = input("Please enter 'Y' if you have job: ")

if have_job_input == "Y" or have_job_input == "yes":
    have_job = True
else:
    have_job = False

if age > 18 and age < 80:
    print("You can have special discount")

if balance < 20:
    print("You are in debt")
else:
    print("you are not in debt")
    if balance < 2000 or age > 60 or age < 18 or not have_job:
        print("You can not have loan")
    else:
        print("You can ask for loan")
