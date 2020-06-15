''' Question: Write a Python program to check for a Prime Number.

Solution: '''

def check_prime(number):
    count = 0
    for i in range(1,number+1):
        if number%i == 0:
            count += 1
    
    if count == 2:
        print(str(number) + " is a Prime Number...")
    else:
        print(str(number) + " is not a Prime Number...")

#entry point of the program
if __name__ == '__main__':
    number = int(input('Enter any number: '))
    check_prime(number)
