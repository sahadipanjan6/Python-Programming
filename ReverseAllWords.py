''' Question: Write a Python program to reverse all the words which have even length.

Solution: '''

sample_text = "At the mouth of the river, the little group of half a dozen intermingled."

words = sample_text.split()
output_text = ""

for word in words:
    if len(word)%2 != 0:
        output_text += word
        output_text += " "
    else:
        output_text += word[::-1]
        output_text += " "
        
print("Output Text: {}".format(output_text))
