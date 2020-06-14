''' Question: Write a Python program to count the number occurrence of a specific character in a string.

Solution: '''

input_string = input('Enter any string: ')
character = input('Enter the specific character: ')
count = 0

for characters in input_string:
    if characters == character:
        count += 1

print("{} has occurred {} times in {}".format(character, count, input_string))
