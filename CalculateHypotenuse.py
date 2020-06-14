''' Question: Write a Python program to calculate the hypotenuse of a right angled triangle.

Solution: '''

get_base = int(input('Enter the base: '))
get_height = int(input('Enter the height: '))
print("Hypotenuse: ", math.sqrt((get_base**2 + get_height**2)))
