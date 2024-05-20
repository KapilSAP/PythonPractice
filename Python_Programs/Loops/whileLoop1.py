bool_var = True

while bool_var:  # infinite loop
    print("it is true")  # exp1 within loop
    user_input = input("Enter boolean input:")
    if user_input == "False":
        bool_var = False
        print("You can go out of the Loop")
    else:
        print("You are stil in the Loop")
    print("It is really True")  # exp2 within loop

print(
    "Move On!"
)  # exp outside the loop. will never print since we are running infinite loop
