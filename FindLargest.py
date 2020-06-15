''' Question: Write a Python program to find out the largest amongst three numbers.

Solution: '''

def find_largest(num1, num2, num3):
    print("Largest number: ", max(max(num1, num2), num3))
    
#entry point of the program
if __name__ == '__main__':
    number1 = int(input('Enter number1: '))
    number2 = int(input('Enter number2: '))
    number3 = int(input('Enter number3: '))
    find_largest(number1, number2, number3)
