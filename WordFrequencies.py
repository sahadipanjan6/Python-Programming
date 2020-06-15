''' Question: Write a Python program to print a long text, convert the string to a list and print all the words and 
their frequencies.

Solution: '''

import nltk
from nltk.tokenize import word_tokenize

long_text = "As they rounded a bend in the path that ran beside the river, \
Lara recognized the silhouette of a fig tree atop a nearby hill. \
The weather was hot and the days were long. The fig tree was in full leaf, but not yet bearing fruit. \
Soon Lara spotted other landmarks—an outcropping of limestone beside the path that had a silhouette like a \
man’s face, a marshy spot beside the river where the waterfowl were easily startled, a tall tree that \
looked like a man with his arms upraised. They were drawing near to the place where there was an island \
in the river. The island was a good spot to make camp. They would sleep on the island tonight."

words = word_tokenize(long_text)

#getting the unique words
unique_words = set(words)

#creating empty dictionary
word_freq = {}

for word1 in unique_words:
    count = 0
    for word2 in words:
        if word1 == word2:
            count += 1
    word_freq[word1] = count
    
#displaying the dictionary
print(word_freq)
