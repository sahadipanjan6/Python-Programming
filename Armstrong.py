''' Question: Write a Python program to check for an Armstrong number.

Solution: '''

def count_digits(number):
    count = 0
    copy = number
    while copy!=0:
        count = count+1
        copy = copy//10
        
    return count

def check_Armstrong(number):
    no_of_digits = count_digits(number)
    total_sum = 0
    copy = number
    while copy!= 0:
        total_sum += (copy%10)**no_of_digits
        copy //= 10
        
    if total_sum == number:
        print(str(number), " is an Armstrong Number...")
    else:
        print(str(number), " is not an Armstrong Number...")
        
#entry point of the program
if __name__ == '__main__':
    number = int(input('Enter any number: '))
    check_Armstrong(number)
