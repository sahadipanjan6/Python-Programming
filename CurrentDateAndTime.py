''' Question: Write a Python program to display the current date and time.

Solution: '''

from datetime import date
import datetime

print("Today's Date: ", date.today())
time = datetime.datetime.now()
print("Time now: ", time.hour, "hrs ", time.minute, "mins ", time.second, "seconds")
