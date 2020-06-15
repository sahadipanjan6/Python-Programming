''' Question: Write a Python function to find the maximum and minimum numbers from a sequence of numbers.

Solution: '''

value_of_n = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(value_of_n):
    li.append(int(input()))
    
maxElement = max(li)
minElement = min(li)

print("{} is the maximum and {} is the minimum element.".format(maxElement, minElement))
