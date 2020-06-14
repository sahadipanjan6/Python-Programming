''' Question: Write a Python program which accepts the radius of a circle from the user and compute the area.

Solution: '''

import math

def compute_area(radius):
    print("Area: ", math.pi*radius**2)
    
if __name__ == '__main__':
    radius = int(input('Enter the radius: '))
    compute_area(radius)
