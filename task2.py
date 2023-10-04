#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and divisible by 2.

Note:  Many languages have a problem when dealing with floating point
decimals, and python is no exception.
Sometimes, when finding the cube root of large numbers, like 729,
you may get 8.9999999999999999999998 instead of 9
To get around this, we can use the round() command
round() accepts 2 parameters, the number to be rounded, and how many decimals
a = round(3.999999999999998, 8) would round at the 8th decimal place, for example.
You don't want to round too early (ie to the nearest whole number) because that
might be too inaccurate.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a divisible by 2.
xx is only a perfect square.
xx is only divisible by 2.

Example:
Enter a number: 8
8 is only divisible by 2.

Enter a number: 64
64 is both a perfect square and divisible by 2.
"""
def is_perfect_square_and_divisible_by_2(number):
    if number <= 0:
        return False

    sqrt_number = int(number ** 0.5)

    if sqrt_number * sqrt_number == number:
        if number % 2 == 0:
            return True
        else:
            return False
    else:
        return False

def is_perfect_square(number):
    if number <= 0:
        return False

    sqrt_number = int(number ** 0.5)

    if sqrt_number * sqrt_number == number:
        return True
    else:
        return False

def is_only_divisible_by_2(number):
    if number <= 0:
        return False

    if number % 2 == 0:
            return True
    else:
            return False

try:
    user_input = int(input("Enter a number: "))
    result = is_perfect_square_and_divisible_by_2(user_input)
    result1 = is_perfect_square(user_input)
    result2 = is_only_divisible_by_2
    if result:
        print(f"{user_input} is both a perfect square and divisible by 2.")
    elif result1:
        print(f"{user_input} is only a perfect square")
    elif result2:
        print(f"{user_input} is only divisible by 2")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
