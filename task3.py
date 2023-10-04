#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer

Enter a number: 2.4
2.4 is not a positive integer

Enter a number: 5
5 is a positive integer

Enter a number: 4.0
4.0 is a positive integer
"""
def is_positive_integer(number):
    try:
        num = int(number)
        if num > 0:
            return True
        else:
            return False
    except ValueError:
        return False

user_input = input("Enter a number: ")
if is_positive_integer(user_input):
    print(f"{user_input} is a positive integer.")
else:
    print(f"{user_input} is not a positive integer.")
