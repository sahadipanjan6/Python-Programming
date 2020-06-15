''' Question: Write a Python program to replace all but the last five characters of a given string into "*" and returns the 
new masked string.

Solution: '''

string = input('Enter any string: ')

if len(string) < 5:
    print("The length of '{}' is less than 5.".format(string))
else:
    endmark = len(string) - 5
    replaceString = ""
    for i in range(endmark):
        replaceString += "*"
               
    string = string.replace(string[:len(string)-5], replaceString)
    print("Output String: {}".format(string))
