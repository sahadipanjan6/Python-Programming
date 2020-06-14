''' Question: Write a Python program to take two lists (of strings) from the user. Find the longest word from both the lists 
and then finally display the common vowels present in them.

Solution: '''

number1 = int(input('Enter number of elements of list1: '))
number2 = int(input('Enter number of elements of list2: '))
list1, list2 = list(), list()

print("Enter elements of list1...")
for i in range(number1):
  list1.append(input())

print("Enter elements of list2...")
for j in range(number2):
  list2.append(input())

#finding longest word of list1
longestWord1 = list1[0].lower()
for i in range(1, len(list1)):
  if len(list1[i]) >= len(longestWord1):
    longestWord = list1[i].lower()

#finding longest word of list2
longestWord2 = list2[0].lower()
for j in range(1, len(list2)):
  if len(list2[j]) >= len(longestWord2):
    longestWord2 = list2[j].lower()

#finding the common vowels
commonVowels = list()
vowels = "aeiou"
for char in longestWord1:
  if char in vowels and char in longestWord2:
    if char not in commonVowels:
      commonVowels.append(char)
    else: continue
  else : continue

#displaying the common vowels
print("Common Vowels: {}".format(commonVowels))
