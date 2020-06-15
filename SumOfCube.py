''' Question: Write a Python function that takes a positive integer and returns the sum of the cube of all the 
positive integers smaller than the specified number.

Solution: '''

get_integer = int(input('Enter any integer: '))
sum_of_cubes = 0
for i in range(get_integer):
    sum_of_cubes += i**3
    
print("{} is the sum of all the cubes.".format(sum_of_cubes))
