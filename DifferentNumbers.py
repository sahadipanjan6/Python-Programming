''' Question: Write a Python function that takes a sequence of numbers and determines whether all the numbers are 
different from each other.

Solution: '''

value_of_n = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(value_of_n):
    li.append(int(input()))
    

if len(li)==len(set(li)):
    print("Every element is different...")
else:
    print("Every element is not different...")
