''' Question: Write a Python program to check whether a year is Leap year or not.

Solution: '''

def check_leap_year(year):
    if (year%4==0 and year%100!=0 or year%400==0):
        print(str(year) + " is a Leap Year...")
    else:
        print(str(year) + " is not a Leap Year...")
        
#entry point of the program
if __name__ == '__main__':
    year = int(input('Enter any year: '))
    check_leap_year(year)
