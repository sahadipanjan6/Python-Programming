''' Question: Write a Python program to remove the characters which have odd index values of a given string.

Solution: '''

string = input('Enter any string: ')
output_string = ""

for i in range(len(string)):
    if i%2 == 0:
        output_string += string[i]
    else:
        continue
        
print("Output String: {}".format(output_string))
