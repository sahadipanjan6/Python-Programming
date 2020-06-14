''' Question: Write a Python program to get the volume of a sphere with radius 6.

Solution: '''

import math

def find_volume(radius):
    print("Volume: ", (4/3)*math.pi*radius**3)
    
if __name__ == '__main__':
    radius = int(input('Enter the radius: '))
    find_volume(radius)
