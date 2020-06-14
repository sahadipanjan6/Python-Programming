''' Question: Write a Python program to check whether a list of integers (to be taken from the user) is Increasing or not. 
An increasing list is a list of integers where all the integers present is itself an increasing number and they are in 
ascending order in the list. An increasing number is a number in which all the digits are present in an increasing order 
(from left to right).

Solution: '''

#function definition to check whether a number is Increasing or not
def isIncreasing(number):
  string = str(number)
  flag = True
  for i in range(len(string)-1):
    if int(string[i]) < int(string[i+1]):
      continue
    else:
      flag = False
      break

  return flag

number = int(input('Enter the number of elements: '))
input_list = list()
print("Enter the elements...")
for i in range(number):
  input_list.append(int(input()))

#declaring the conditions
condition1 = True
condition2 = True

#checking for condition1
for i in range(len(input_list)-1):
  if input_list[i] <= input_list[i+1]:
    continue
  else:
    condition = False
    break

#checking for condition2
for element in input_list:
  if isIncreasing(element) == True:
    continue
  else:
    condition2 = False
    break

#checking both the conditions and deciding
if condition1==True and condition2==True:
  print("{} is an Increasing List...".format(input_list))
else:
  print("{} is not an Increasing List...".format(input_list))
