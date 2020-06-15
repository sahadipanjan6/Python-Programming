''' Question: Write a Python function to check whether a number is divisible by another number. 
Accept two integers values form the user.

Solution: '''

integer1 = int(input('Enter first integer: '))
integer2 = int(input('Enter second integer: '))

if integer1 > integer2:
    if integer1%integer2 == 0:
        print("{} is divisible by {}".format(integer1, integer2))
    else:
        print("{} is not divisible by {}".format(integer1, integer2))
        
elif integer2 > integer1:
    if integer2%integer1 == 0.0:
        print("{} is divisible by {}".format(integer2, integer1))
    else:
        print("{} is not divisible by {}".format(integer2, integer1))
