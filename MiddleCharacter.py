''' Question: Write a Python program to find the middle character(s) of a given string. If the length of the string is 
odd return the middle character and return the middle two characters if the string length is even.

Solution: '''

string = input('Enter any string: ')

if len(string)%2 != 0:
    print("Middle Character: {}".format(string[len(string)//2]))
else:
    character1 = string[len(string)//2-1]
    character2 = string[len(string)//2]
    print("Middle Characters: ({},{})".format(character1, character2))
