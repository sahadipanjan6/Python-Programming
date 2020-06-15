''' Question: Write a Python program to count the number of each character of a given text of a text file.

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

#creating an empty dictionary
char_freq = {}

for character in long_text:
    #checking if the character is already present in the dictionary
    if character in char_freq:
        char_freq[character] += 1
    else:
        char_freq[character] = 1
        
#displaying the dictionary
print(char_freq)
