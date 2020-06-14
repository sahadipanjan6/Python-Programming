''' Question: Write a Python program to list all files in a directory in Python.

Solution: '''

import os

directory = "/home/dipanjan/Documents/AU_Research_Community"
print("List of files: ", os.listdir(directory))
