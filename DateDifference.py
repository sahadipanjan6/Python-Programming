''' Question: Write a Python program to calculate the number of days between two dates.

Solution: '''

import datetime

first_date = datetime.date(2020, 4, 14)
second_date = datetime.date(2020, 5, 14)
change = second_date - first_date
print("Number of days: ", change.days)
