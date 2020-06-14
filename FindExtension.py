''' Question: Write a Python program to accept a filename from the user and print the extension of that.

Solution: '''

def print_extension(filename):
    print("Extension: ", filename.split('.')[1])
    
if __name__ == '__main__':
    filename = input('Enter full filename: ')
    print_extension(filename)
