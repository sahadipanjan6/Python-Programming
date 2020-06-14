''' Question: Write a Python program to concatenate N strings.

Solution: '''

value_of_n = int(input('Enter the value of n: '))
strings = []
print("Enter the strings....")

for i in range(value_of_n):
    strings.append(input())
    
output_string = ""
for string in strings:
    output_string += string
    
print("Concatenated String: ", output_string)
