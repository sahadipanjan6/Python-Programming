''' Question: Write a Python program to compute the sum of all items of a given array of integers where each integer is 
multiplied by its index. Return 0 if there is no number.

Solution: '''

length = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(length):
    li.append(int(input()))
    
    
sum_total = 0
for j in range(len(li)):
    sum_total += li[j]*j
    
print('Sum is {}'.format(sum_total))
