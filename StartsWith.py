''' Question: Write a Python program to get a new string from a given string where "ls" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.

Solution: '''

get_string = input('Enter any string: ')
if get_string.startswith("ls"):
    print("Output: ", get_string)
else:
    print("Output: ", "ls"+get_string)
