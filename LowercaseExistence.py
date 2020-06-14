''' Question: Write a Python program to check whether lowercase letters exist in a string.

Solution: '''

input_string = input('Enter any string: ')
flag = 0

for character in input_string:
    if character.islower() == True:
        flag = 1
        break
    else:
        continue
        
if flag == 1:
    print("Lowercase letters exists in {}.".format(input_string))
else:
    print("Lowercase letters does not exist in {}.".format(input_string))
