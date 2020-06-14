''' Question:  Write a Python program to calculate the sum of the digits in an integer.

Solution: '''

get_number = int(input('Enter any number: '))
copy = get_number
sum_digits = 0

while(copy != 0):
    sum_digits += copy%10
    copy //= 10
    
print("Sum of digits of {} is {}".format(get_number, sum_digits))
