''' Question: Write a Python program to concatenate all elements in a list into a string and return it.

Solution: '''

value_of_n = int(input('Enter the value of n: '))
li = []
print("Enter the elements....")
for i in range(value_of_n):
    li.append(int(input()))
    
output_string = ""
for elements in li:
    output_string += str(elements)
print(output_string)
