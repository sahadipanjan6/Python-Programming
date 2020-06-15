''' Question: Write a Python program to create two strings from a given string. Create the first string using those character 
which occurs only once and create the second string which consists of multi-time occurring characters in the said string.

Solution: '''

string = input('Enter any string: ')

#creating an empty dictionary
char_freq = {}

for character in string:
    if character in char_freq:
        char_freq[character] += 1
    else:
        char_freq[character] = 1
        
first_string = ""
second_string = ""
        
#iterating over the dictionary
for key in char_freq.keys():
    if char_freq[key] == 1:
        first_string += key
    elif char_freq[key] > 1:
        second_string += key
        
#displaying both the strings
print("First String: {}".format(first_string))
print("Second String: {}".format(second_string))
