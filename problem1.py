#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""
def is_frue(number):
    if number % 6 == 0 and number % 8 != 0:
        return True
    else:
        return False

numb = int(input("Enter a number: "))
if is_frue(numb):
    print(f"{numb} is frue")
else:
    print(f"{numb} is not frue")

