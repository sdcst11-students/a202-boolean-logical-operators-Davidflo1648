
#! python3
"""
The Earth maintains an orbit where it's closest distance to  
the sun is 0.9759 AU and it's furthest distance to the sun is 
1.016 AU. 
Mars maintans an orbit that has a minimum value of 1.524 AU and
a maximum value of 1.666 AU
Ask the user to enter a number. 
Tell them if the number is within Earth or Mars orbits
(2 points)

Inputs:
a number (float)

Outputs:
That is within normal Earth or Mars orbit.
That is not within normal Earth or Mars orbit.


Example:
Enter the distance from the sun in AU: 9.4
That is not within normal Earth or Mars orbit.

Enter the distance from the sun in AU: 1.011
That is within normal Earth or Mars orbit.

Enter the distance from the sun in AU: 1.6
That is within normal Earth or Mars orbit.

Enter the distance from the sun in AU: 2
That is not within normal Earth or Mars orbit.

"""
def check_orbit(number):

    earth_min = 0.9759
    earth_max = 1.016
    mars_min = 1.524
    mars_max = 1.666
    
    if earth_min <= number <= earth_max:
        return "The number falls within Earth's orbit."
    elif mars_min <= number <= mars_max:
        return "The number falls within Mars' orbit."
    else:
        return "The number is outside both Earth's and Mars' orbits."

user_input = float(input("Enter a number (AU): "))
result = check_orbit(user_input)
print(result)