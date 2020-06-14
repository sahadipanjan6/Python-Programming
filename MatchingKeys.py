''' Question: Write a Python program to match key values in two dictionaries (which is to be taken from the user). 
If the keys are present, then form another dictionary where the values of the keys found will be the summation of their
corresponding values from the other dictionaries. For e.g. Input Dictionary1 = {1:1, 2:2, 3:3, 4:4}, 
Input Dictionary2 = {1:1, 3:9, 4:16, 5:25}, Output Dictionary = {1:2, 3:12, 4:20}.

Solution: '''

number1 = int(input('Enter number of elements of Dictionary1: '))
number2 = int(input('Enter number of elements of Dictionary2: '))
input_dic1, input_dic2 = dict(), dict()

print("Enter elements of dictionary1 in key-value pairs with space in between...")
for i in range(number1):
  input_string1 = input()
  arr1 = input_string1.split()
  input_dic1[int(arr1[0])] = int(arr1[1])

print("Enter elements of dictionary2 in key-value pairs with space in between...")
for j in range(number2):
  input_string2 = input()
  arr2 = input_string2.split()
  input_dic2[int(arr2[0])] = int(arr2[1])

#finding the common keys from the 2 dictionaries
output_dic = dict()
for key1 in input_dic1.keys():
  for key2 in input_dic2.keys():
    if key1 == key2:
      output_dic[key1] = input_dic1[key1] + input_dic2[key2]

#displaying the output dictionary
print("Output Dictionary: {}".format(output_dic))
