''' Question: Write a Python program to get the difference between a given number and 17, if the number is greater than 17 
then return the double of the absolute difference.

Solution: '''

given_number = 17
user_given_number = int(input('Enter any number: '))

if user_given_number > given_number:
    print("Result: ", abs(user_given_number - given_number)*2)
elif given_number > user_given_number:
    print("Result: ", (given_number - user_given_number))
