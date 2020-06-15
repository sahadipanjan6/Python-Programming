''' Question: Write a Python program to swap two variables.

Solution: '''

def swap(a, b):
    temp = b
    b = a
    a = temp
    
    print("After swapping, value of a: ", a)
    print("After swapping, value of b: ", b)
    

#entry point of the program
if __name__ == '__main__':
    value_of_a = int(input('Enter the value of a: '))
    value_of_b = int(input('Enter the value of b: '))
    print("Before swapping, value of a: ", value_of_a)
    print("Before swapping, value of b: ", value_of_b)
    
    #calling the function
    swap(value_of_a, value_of_b)
