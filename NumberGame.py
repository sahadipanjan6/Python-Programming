''' Question: Write a Python program that accept a positive number and subtract from this number the sum of its digits 
and so on. Continue this operation until the number is positive.

Solution: '''

def find_digit_sum(number):
    copy = number
    sum_digit = 0
    while(copy!=0):
        sum_digit += (copy%10)
        copy //= 10
        
    return sum_digit


if __name__ == '__main__':
    number = int(input('Enter any number: '))
    copy = number
    
    while(copy > 0):
        print('Number: {}'.format(copy))
        difference = copy - find_digit_sum(copy)
        print('Difference: {}'.format(difference))
        copy = difference
