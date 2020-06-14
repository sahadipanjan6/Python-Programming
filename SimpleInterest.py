''' Question: Write a Python program to compute the future value of a specified principal amount, rate of interest, 
and a number of years.

Solution: '''

get_principal = int(input('Enter principal amount: '))
get_rate = int(input('Enter rate of interest: '))
get_time = int(input('Enter time in years: '))
simple_interest = (get_principal*get_rate*get_time) / 100
print("Total Amount: ", (get_principal+simple_interest))
