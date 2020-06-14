''' Question: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list 
and a tuple with those numbers.

Solution: '''

def generate_list(input_string):
    words = input_string.split(',')
    numbers = []
    for word in words:
        numbers.append(int(word))
        
    print("Generated List: ", numbers)
    
def generate_tuple(input_string):
    words = input_string.split(',')
    numbers = []
    for word in words:
        numbers.append(int(word))
        
    print("Generated Tuple: ", tuple(numbers))
    
if __name__ == '__main__':
    input_string = input('Enter the string: ')
    generate_list(input_string)
    generate_tuple(input_string)
