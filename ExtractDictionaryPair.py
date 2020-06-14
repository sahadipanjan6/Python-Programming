''' Question: Write a Python program to extract single key-value pair of a dictionary in variables.

Solution: '''

#taking a dictionary manually
dictionary = {}

dictionary['1'] = 1
dictionary['2'] = 4
dictionary['3'] = 9
dictionary['4'] = 16
dictionary['5'] = 25

search_key = int(input('Enter the search key: '))
for key in dictionary:
    if key == str(search_key):
        print("({},{}) is a key-value pair...".format(key, dictionary[key]))
        break
