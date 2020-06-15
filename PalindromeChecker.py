''' Question: Write a Python program to check whether a given integer is a palindrome or not.

Solution: '''

number = int(input('Enter any number: '))
string = str(number)
if string == string[::-1]:
    print("{} is a Palindrome.".format(string))
else:
    print("{} is not a Palindrome.".format(string))
