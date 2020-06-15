''' Question: Write a Python program to find the name of the oldest student from a given dictionary containing the names 
and ages of a group of students.

Solution: '''

length = int(input('Enter no. of elements: '))

#creating an empty dictionary
student_data = {}

for i in range(length):
    x, y = input('Enter name: '), int(input('Enter age: '))
    student_data[x] = y
    
oldest_age = 0
for j in sorted(student_data.values(), reverse=True):
    oldest_age = j
    break
    
for k in student_data.keys():
    if student_data[k] == oldest_age:
        print("Oldest Student is '{}'".format(k))
