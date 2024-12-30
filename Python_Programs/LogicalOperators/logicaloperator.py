# there are three logical operators
# and, or, not, 
# and operator check if both the expressions are true
# or operator check if either expression is true
# not operator check if the expression is false

num = int(input("Please enter a number in between 1-100: ")) # input is used to take input from user in integer

if num > 20 and num < 50:  # and operator check if both the expressions are true
    print("AND condition is true")
elif num > 20 or num < 50:  # or operator check if either expression is true
    print("Or Condition is true")

if num == 20 or num == 50: # check if num is equals to 20 or 50
    print("Equals Condition is true")
elif num != 20 or num != 50: #  check if num is not equals to 20 or 50
    print("Not Equals Condition is true")

if not num != 30:  # not operator check if the expression is false    
    print("Num is equals to 30")
