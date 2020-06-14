''' Question: Write a Python program that accepts an integer(n) and computes the value of n+nn+nnn.

Solution: '''

def compute_value(n):
    first_number = n
    second_number = n + 10*n
    third_number = n + 10*n + 100*n
    print("Final value: ", (first_number+second_number+third_number))
    
if __name__ == '__main__':
    value_of_n = int(input('Enter the value of n: '))
    compute_value(value_of_n)
