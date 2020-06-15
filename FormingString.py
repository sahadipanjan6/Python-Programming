''' Question: Write a Python function to get a string made of 4 copies of the last two characters of a specified string 
(length must be at least 2).

Solution: '''

string = input('Enter any string: ')
print("Output String: {}".format(string[len(string)-2:]*4))
