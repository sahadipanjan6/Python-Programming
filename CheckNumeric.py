''' Question: Write a Python program to check whether a string is numeric.

Solution: '''

input_string = input('Enter any string: ')
flag = 0

for character in input_string:
    if str.isdigit(character):
        continue
    else:
        flag = 1
        break

if flag == 0:
    print("{} is a numeric string...".format(input_string))
else:
    print("{} is not a numeric string...".format(input_string))
