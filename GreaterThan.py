''' Question: Write a Python program to test whether all numbers of a list is greater than a certain number.

Solution: '''

value_of_n = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")

for i in range(value_of_n):
    li.append(int(input()))
    
checking_number = int(input('Enter checking number: '))
flag = 0

for elements in li:
    if elements > checking_number:
        continue
    else:
        flag = 1
        break
        
if flag == 0:
    print("All the elements are greater than {}".format(checking_number))
else:
    print("All the elements are not greater than {}".format(checking_number))
