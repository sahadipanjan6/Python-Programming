''' Question: Write a Python program to find the list of words that are longer than n (integer to be taken from the user) 
from a given list of words (to be taken from the user). Concatenate the words altogether and then replace all the consonants
with its next alphabet from the alphabetical series and finally display the modified string.

Solution: '''

number = int(input('Enter number of elements: '))
input_list, output_list = list(), list()

print("Enter the elements...")
for i in range(number):
  input_list.append(input())

value_of_n = int(input('Enter the value of N: '))
for element in input_list:
  if len(element) > value_of_n:
    output_list.append(element.lower())

#concatenating all the words from the output list
output_string = ""
if len(output_list) == 0:
  print("There are no words which is greater than {} in length.".format(value_of_n))
else:
  for string in output_list:
    output_string += string

print(output_string)

#replacing the consonants
vowels = "aeiou"
alphabets = "abcdefghijklmnopqrstuvwxyz"
modified_string = ""

for character in output_string:
  if character not in vowels:
    for i in range(len(alphabets)):
      if alphabets[i]==character:
        modified_string += alphabets[i+1]

  else:
    modified_string += character

#displaying the modified string
print("Modified String: {}".format(modified_string))
