''' Question: Write a Python program to print the number of prime numbers which are less than or equal to a given integer.

Solution: '''

def check_prime(number):
    output = False
    count = 0
    for i in range(1,number+1):
        if number%i == 0:
            count += 1
    if count == 2:
        output = True
    
    return output


if __name__ == '__main__':
    number = int(input('Enter any number: '))
    count_primes = 0
    for i in range(1, number+1):
        if check_prime(i) == True:
            count_primes += 1
            
    print("{} is the no. of prime numbers within 1 and {}".format(count_primes,number))
