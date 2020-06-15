''' Question: Write a Python program to solve a quadratic equation.

Solution: '''

import cmath

def solve_quadratic(a, b, c):
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    print("1st root: ", x1)
    print("2nd root: ", x2)
    
#entry point of the program
if __name__ == '__main__':
    #getting the 3 coefficients from the user
    coefficient_a = int(input('Enter the value of a: '))
    coefficient_b = int(input('Enter the value of b: '))
    coefficient_c = int(input("Enter the value of c: "))
    
    #calling the function
    solve_quadratic(coefficient_a, coefficient_b, coefficient_c)
