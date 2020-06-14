''' Question: Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2.

Solution: '''

get_string = input('Enter any string: ')
value_of_n = int(input('Enter the value of n: '))

if len(get_string) < 2:
    print("Output String: ", get_string*value_of_n)
elif len(get_string) > 2:
    print("Output String: ", get_string[:2]*value_of_n)
