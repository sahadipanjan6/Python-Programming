''' Question: Write a Python program to compute cumulative sum of numbers of a given list.

Solution: '''

length = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(length):
    li.append(int(input()))
    
output_list = []
for i in range(0, len(li)):
    output_list.append(sum(li[0:i+1]))
    
print("{} is the cumulative_sum list of {}.".format(output_list, li))
