''' Question: Write a Python program to create a histogram from a given list of integers.

Solution: '''

import matplotlib.pyplot as plt

value_of_n = int(input('Enter the number of elements: '))
li = []
print("Enter the elements....")
for i in range(value_of_n):
    li.append(int(input()))
    
#forming the histogram
plt.hist(li, bins=10)
plt.show()
