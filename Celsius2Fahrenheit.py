''' Question: Write a Python program to convert Celsius to Fahrenheit.

Solution: '''

def convert_to_fahrenheit(celsius):
    print("In Fahrenheit: ", ((9*celsius)/5 + 32))
          
#entry point of the program
if __name__ == '__main__':
    celsius = int(input('Enter temperature in Celsius: '))
    convert_to_fahrenheit(celsius)
