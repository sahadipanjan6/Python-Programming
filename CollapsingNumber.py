'''Question: Write a Python program to collapse a given number. Collapsing of a number is to repeatedly add the digits
of the number and when it comes to a single digit sum then display it. For e.g. Input Number = 1234,
Output = 1 [since, 1+2+3+4 = 10, again, 1+0 = 1]

Solution:'''

#function definition to find the sum of digits of a number
def findSumOfDigits(number):
  string_number = str(number)
  total = 0
  for character in string_number:
    total += int(character)

  return total

#function definition to find the number of digits in a number
def countDigits(number):
  return len(str(number))


number = int(input('Enter any number: '))
copy = number

while True:
  summation = findSumOfDigits(copy)
  if countDigits(summation) == 1:
    print("Sum of Digits: {}".format(summation))
    break
  else:
    copy = summation
    continue    
