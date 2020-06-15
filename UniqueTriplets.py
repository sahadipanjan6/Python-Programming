''' Question: Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n 
integers.

Solution: '''

value_of_n = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(value_of_n):
    li.append(int(input()))
    
#finding all triplets
print("Triplets are: ")
for i in range(len(li)):
    for j in range(i+1, len(li)):
        for k in range(j+1, len(li)):
            if (li[i]+li[j]+li[k])==0:
                print("({},{},{})".format(li[i], li[j], li[k]))
