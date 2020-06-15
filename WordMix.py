''' Question: Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. 
The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number 
of letters. NOTE: A word is a sequence of letters which is separated by the spaces.

Solution: '''

import nltk
from nltk.tokenize import word_tokenize

sample_text = "At the mouth of the river, the little group of half a dozen intermingled \
families gathered salt from the great salt beds beside the sea."

words = word_tokenize(sample_text)
max_length = 0
max_word = ""

#creating an empty dictionary
freq_word = {}

for word in words:
    if word in freq_word:
        freq_word[word] += 1
    else:
        freq_word[word] = 1

#iterating over the dictionary to find the most frequent word
first_word = ""
for i in sorted(freq_word.keys(), reverse=True):
    first_word = i
    break

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        max_word = word
        
second_word = max_word

#displaying the two words
print("The word '{}' has occurred the most.".format(first_word))
print("The word '{}' has the maximum number of letters.".format(second_word))
