''' Question: Write a Python program to display the Fibonacci Sequence.

Solution: '''

def print_Fibonacci(value_of_n):
    a = 0
    b = 1
    print("Fibonacci Sequence is:- ")
    print(a)
    print(b)
    for i in range(3, value_of_n+1):
        c = a + b
        print(c)
        a = b
        b = c
        
#entry point of the program
if __name__ == '__main__':
    value_of_n = int(input('Enter the number of terms: '))
    print_Fibonacci(value_of_n)    
