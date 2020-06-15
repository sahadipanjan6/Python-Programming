''' Question: Write a Python program that takes three integers and check whether the last digit of first number * the 
last digit of second number = the last digit of third number.

Solution: '''

integer1 = input('Enter 1st integer: ')
integer2 = input('Enter 2nd integer: ')
integer3 = input('Enter 3rd integer: ')

integer1_last = int(integer1[len(integer1)-1])
integer2_last = int(integer2[len(integer2)-1])
integer3_last = int(integer3[len(integer3)-1])

if (integer1_last*integer2_last) == integer3_last:
    print("Condition is satisfied...")
else:
    print("Condition is not satisfied...")
