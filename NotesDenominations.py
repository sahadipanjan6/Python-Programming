''' Question: Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) 
against a given amount.

Solution: '''

total_amount = int(input('Enter the total amount: '))

c500 = total_amount//500
c200 = (total_amount - c500*500)//200
c100 = (total_amount - c500*500 - c200*200)//100
c50 = (total_amount-c500*500-c200*200-c100*100)//50
c20 = (total_amount-c500*500-c200*200-c100*100-c50*50)//20
c10 = (total_amount-c500*500-c200*200-c100*100-c50*50-c20*20)//10

#displaying the quantities
print("No. of 500 notes: {}".format(c500))
print("No. of 200 notes: {}".format(c200))
print("No. of 100 notes: {}".format(c100))
print("No. of 50 notes: {}".format(c50))
print("No. of 20 notes: {}".format(c20))
print("No. of 10 notes: {}".format(c10))
