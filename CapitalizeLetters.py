''' Question: Write a Python program to capitalize first and last letters of each word of a given string.

Solution: '''

sample_text = "At the mouth of the river, the little group of half a dozen intermingled"
words = sample_text.split()

output_text = ""
for word in words:
    if len(word) > 1:
        new_word = word[0].upper() + word[1:len(word)-1] + word[len(word)-1].upper()
        output_text += new_word
        output_text += " "
    else:
        output_text += word
        output_text += " "
    
print("Output Text: {}".format(output_text))
