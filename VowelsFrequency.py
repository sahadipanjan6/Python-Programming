''' Question: Write a Python program to find the count of each vowel present in a string (to be taken from the user) and 
display them.

Solution: '''

input_string = input("Enter any string: ")
vowels = "aeiou"

vowelsList = list()
for char in input_string.lower():
  if char in vowels and char not in vowelsList:
    vowelsList.append(char)

#finding the count of each vowels present
if len(vowelsList) == 0:
  print("No vowels are present in the input string...")
else:
  count_dic = dict()
  for vowel in vowelsList:
    count = 0
    for character in input_string.lower():
      if vowel == character:
        count += 1

    #putting in the dictionary
    count_dic[vowel] = count

  #displaying the vowels_count dictionary
  print("Count of vowels: {}".format(count_dic))
