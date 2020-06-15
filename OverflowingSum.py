''' Question: Write a Python program to compute and print sum of two given integers (more than or equal to zero). 
If given integers or the sum have more than 80 digits, print "overflow".

Solution: '''

def count_digits(number):
    copy = number
    count = 0
    while(copy!=0):
        count += 1
        copy //= 10
    return count

if __name__ == '__main__':
    number1 = int(input('Enter first integer: '))
    number2 = int(input('Enter second integer: '))
    sum_total = number1 + number2
    if count_digits(sum_total) > 80:
        print("Overflow...")
    else:
        print("Not Overflow...")
