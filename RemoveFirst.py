''' Question: Write a Python program to remove the first item from a specified list.

Solution: '''

value_of_n = int(input('Enter no. of elements: '))
li = []
print('Enter the elements....')
for i in range(value_of_n):
    li.append(int(input()))
    
print("Actual List: ", li)
li.pop(0)
print("Updated List: ", li)
