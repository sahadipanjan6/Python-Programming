''' Question: Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

Solution: '''

import math

get_x1 = int(input('Enter x1: '))
get_y1 = int(input('Enter y1: '))
get_x2 = int(input('Enter x2: '))
get_y2 = int(input('Enter y2: '))

#calculating distance
distance = math.sqrt((get_y2-get_y1)**2 + (get_x2-get_x1)**2)

print("Distance: ", distance)
