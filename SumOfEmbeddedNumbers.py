''' Question: Write a Python program to sum of all numerical values (positive integers) embedded in a sentence.

Solution: '''

text = input('Enter any sentence: ')
sum_total = 0

for character in text:
    if str.isdigit(character):
        sum_total += int(character)

print("{} is the sum of all numerical values.".format(sum_total))
