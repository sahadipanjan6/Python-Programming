''' Question: Write a Python program that accept a list of numbers and create a list to store the count of negative number 
in first element and store the sum of positive numbers in second element.

Solution: '''

value_of_n = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(value_of_n):
    li.append(int(input()))
    
outputList = []

#counting negative numbers
count = 0
for element in li:
    if element < 0:
        count += 1
        
#finding the sum of positive numbers
sum_total = 0
for element in li:
    if element > 0:
        sum_total += element
        
#appending the two values in the output list
outputList.append(count)
outputList.append(sum_total)

#displaying the output list
print("Output List: {}".format(outputList))
