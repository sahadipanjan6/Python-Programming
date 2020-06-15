''' Question: Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to 
a target value. Print all those three-element combinations.

Solution: '''

n1 = int(input('Enter no. of elements of 1st list: '))
n2 = int(input('Enter no. of elements of 2nd list: '))
n3 = int(input('Enter no. of elements of 3rd list: '))

list1, list2, list3 = [], [], []
print("Enter elements of 1st list...")
for i in range(n1):
    list1.append(int(input()))
    
print("Enter elements of 2nd list...")
for j in range(n2):
    list2.append(int(input()))
    
print("Enter elements of 3rd list...")
for k in range(n3):
    list3.append(int(input()))

target = int(input('Enter the target value: '))

#getting all possible combinations
print("Triplets are: ")
for i in range(len(list1)):
    for j in range(len(list2)):
        for k in range(len(list3)):
            if (list1[i]+list2[j]+list3[k]) == target:
                print("({},{},{})".format(list1[i], list2[j], list3[k]))
