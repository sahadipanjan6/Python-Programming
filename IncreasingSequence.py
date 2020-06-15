''' Question: Write a Python program to check whether a sequence of numbers has an increasing trend or not.

Solution: '''

length = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(length):
    li.append(int(input()))
    
flag = 0
for i in range(len(li)-1):
    if li[i] <= li[i+1]:
        continue
    else:
        flag = 1
        break
        
if flag == 0:
    print("Increasing Trend of numbers is maintained...")
else:
    print("Increasing Trend of numbers is not maintained...")
