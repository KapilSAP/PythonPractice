# there are three logical operators
# and, or, not,

num = int(input("Please enter a number in between 1-100: "))

if num > 20 and num < 50:  # and operator check if both the expressions are true
    print("AND condition is true")
elif num > 20 or num < 50:  # or operator check if either expression is true
    print("Or Condition is true")

if num == 20 or num == 50:
    print("Equals Condition is true")
elif num != 20 or num != 50:
    print("Not Equals Condition is true")

if not num != 30:
    print("Num is equals to 30")
