''' Question: Write a Python program to compute the product of a list of integers (without using for loop).

Solution: '''

from functools import reduce

value_of_n = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(value_of_n):
    li.append(int(input()))
    
result = reduce((lambda x,y : x*y), li)
print("{} is the product.".format(result))
