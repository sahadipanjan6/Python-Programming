''' Question: Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, 
leave it unchanged.

Solution: '''

string = input('Enter any string: ')
output_string = ""

if len(string) < 3:
    print("Output String: {}".format(string))
else:
    if string.endswith("ing"):
        output_string += string[:len(string)-3]
        output_string += "ly"
        print("Output String: {}".format(output_string))
    else:
        output_string += string
        output_string += "ing"
        print("Output String: {}".format(output_string))
