''' Question: Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.

Solution: '''

string = input('Enter any string: ')
output_string = ""

if len(string) < 2:
    print("Length of input string is less than 2!!!")
else:
    output_string += string[:2]
    output_string += string[len(string)-2:]
    print("Output String: {}".format(output_string))  
