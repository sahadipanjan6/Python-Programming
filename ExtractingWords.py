''' Question: Internet search engine giant, such as Google accepts web pages around the world and classify them, creating a 
huge database. The search engines also analyze the search keywords entered by the user and create inquiries for database 
search. In both cases, complicated processing is carried out in order to realize efficient retrieval, but basics are all 
cutting out words from sentences. Write a Python program to cut out words of 3 to 6 characters length from a given sentence 
not more than 1024 characters.

Solution: '''

sample_text = "At the mouth of the river, the little group of half a dozen intermingled \
families gathered salt from the great salt beds beside the sea."

words = sample_text.split()
print("Words with length in between 3 and 6 are:- ")
for word in words:
    if len(word)>=3 and len(word)<=6:
        print(word)
