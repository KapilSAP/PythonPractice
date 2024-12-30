# logical operator example
# This program will ask user to enter job, account balance, age  
# which will be checked against some conditions to determine
# if he/she is eligible for loan or not.
#

balance = float(input("Please enter your account balance: ")) # float is used to convert input to float
age = int(input("Please enter your age: ")) # int is used to convert input to integer
have_job_input = input("Please enter 'Y' if you have job: ") # input is used to take input from user

if have_job_input == "Y" or have_job_input == "yes": # check if user has job
    have_job = True     # if user has job then set have_job to True
else:
    have_job = False     #  if user does not have job then set have_job to False

if age > 18 and age < 80: # check if age is in between 18 and 80
    print("You can have special discount") # if age is in between 18 and 80 then print this message

if balance < 20: # check if balance is less than 20
    print("You are in debt") # if balance is less than 20 then print this message
else:
    print("you are not in debt") #  if balance is not less than 20 then print this message
    if balance < 2000 or age > 60 or age < 18 or not have_job: #    check if balance is less than 2000 or age is greater than 60 or age is less than 18 or user does not have job
        print("You can not have loan") #    if any of the above condition is true then print this message
    else:
        print("You can ask for loan") #   if none of the above condition is true then print this message
