''' Question: Write a Python program to calculate the area of a triangle.

Solution: '''

import math

def calculate_area(side1, side2, side3):
    #calculating the semi-perimeter
    s = (side1 + side2 + side3)/2
    
    #calculating the differences of each sides from the semi-perimeter
    s_side1 = s - side1
    s_side2 = s - side2
    s_side3 = s - side3
    
    product = s_side1 * s_side2 * s_side3
    print("Area: ", math.sqrt(product))
    

#entry point of the program
if __name__ == '__main__':
    #getting all the sides of the triangle from the user
    side1 = int(input('Enter the first side: '))
    side2 = int(input('Enter the second side: '))
    side3 = int(input('Enter the third side: '))
    
    #calling the function with these 3 sides as its parameters
    calculate_area(side1, side2, side3)
