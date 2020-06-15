''' Question: Write a Python program to find out the Factorial of a number.

Solution: '''

def find_factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    
    print("Factorial of ", str(number), " is: ", fact)
    
#entry point of the program
if __name__ == '__main__':
    number = int(input('Enter any number: '))
    find_factorial(number)
