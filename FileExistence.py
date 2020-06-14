''' Question: Write a Python program to check whether a file exists.

Solution: '''

import os
from os import path

filepath = "/home/dipanjan/Documents/AU_Research_Community/Python_programming_questions.pdf"

if path.exists(filepath):
    print("The file exists...")
else:
    print("The file does not exists...")
