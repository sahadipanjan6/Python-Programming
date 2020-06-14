''' Question: Write a Python program to get the least common multiple (LCM) of two positive integers.

Solution: '''

def compute_GCD(number1, number2):
    while(number2):
        number1, number2 = number2, (number1 % number2)
    return number1

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
product = number1 * number2
print("LCM of ", number1, " and ", number2, " is: ", (product/compute_GCD(number1, number2)))
