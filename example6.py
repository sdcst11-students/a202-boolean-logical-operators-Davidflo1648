#!python3

"""
We can use the ! symbol to check the negation or the 'not' value of a boolean
"""

isHungry = False

if not isHungry:
    print("1. You are not hungry")

print('=')

if isHungry != True:
    print("2. You are not hungry")

print("=")

if isHungry is not True:
    print("3. You are not hungry")

print("=")

if isHungry == False:
    print("4. You are not hungry")
'''
Note that these statements behave identically
'''