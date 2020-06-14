''' Question: Write a Python program which accepts the user’s first name and last name and print them in reverse order 
with a space between them.

Solution: '''

def print_name(name):
    words = name.split()
    print("Output: ", ' '.join(words[::-1]))
    
if __name__ == '__main__':
    full_name = input('Enter your full name: ')
    print_name(full_name)
