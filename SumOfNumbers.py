''' Question: Write a Python program to calculate the sum of three given numbers, if the values are equal then return three 
times of their sum.

Solution: '''

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))

#checking for equality
if first_number==second_number and second_number==third_number:
    print("Output: ", 3*(first_number+second_number+third_number))
else:
    print("Output: ", (first_number+second_number+third_number))
