''' Question: A dictionary of voters are given (to be taken from the user), where the keys are the names of the voters and 
their corresponding values are their email-ids. The email-ids are given in such a way that they contain the year of birth of 
the person under consideration, for e.g. sahadipanjan1990@gmail.com. Taking the base (or reference) year to be 1950, 
write a Python program to display the names of all persons from the given dictionary who are eligible to vote
(eligibility criteria: age should be greater than 21 years).

Solution: '''

import re

#function definition to extract the YOB from an email
def extractYOB(emailID):
  yearOfBirth = 0
  modifiedString = re.sub(r"[^0-9 ]", " ", emailID)
  arr = modifiedString.split()
  for element in arr:
    if element != " ":
      yearOfBirth = int(element)
    else : continue
  
  return yearOfBirth

number = int(input('Enter the number of elements: '))
input_dic = dict()
print("Enter the key-value pairs with space in between...")

for i in range(number):
  string = input()
  arr = string.split()
  input_dic[arr[0]] = arr[1]

#mentioning the reference year
reference_year = 1950

#traversing the input dictionary
print("Persons eligible to vote are: ")
for key in input_dic:
  email = input_dic[key]
  yob = extractYOB(email)
  age = yob - reference_year
  if age > 21:
    print(key)
