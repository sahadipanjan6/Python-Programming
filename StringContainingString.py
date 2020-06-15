''' Question: Write a Python program that accept two strings and test if the letters in the second string are present in the 
first string.

Solution: '''

string1 = input('Enter 1st string: ')
string2 = input('Enter 2nd string: ')

flag = 0
for letter in string2:
    if letter in string1:
        continue
    else:
        flag = 1
        break
        
if flag == 0:
    print("All the letters of '{}' are present in '{}'.".format(string2, string1))
else:
    print("All the letters of '{}' are not present in '{}'.".format(string2, string1))
