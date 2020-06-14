'''Question: Write a Python program to find the maximum and minimum value from a user given dictionary and then display the 
sum of the digits of their absolute difference.

Solution: '''

number = int(input('Enter the number of elements: '))
input_dic = dict()
print('Enter the elements (key-value) with a space in between...')
for i in range(number):
  string = input()
  arr = string.split()
  input_dic[int(arr[0])] = int(arr[1])

#finding the maximum value
values = list()
for key in input_dic.keys():
  values.append(input_dic[key])

maximum = values[0]
for i in range(1, len(values)):
  if values[i] >= maximum:
    maximum = values[i]

#finding the minimum value
minimum = values[0]
for j in range(1, len(values)):
  if values[j] <= minimum:
    minimum = values[j]

#finding the absolute difference
difference = maximum - minimum

#finding the sum of the digits of the difference
string_number = str(difference)
total = 0
for character in string_number:
  total += int(character)

print("Sum of Digits: {}".format(total))
