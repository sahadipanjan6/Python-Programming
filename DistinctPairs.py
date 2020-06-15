''' Question: Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of 
integer values.

Solution: '''

value_of_n = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(value_of_n):
    li.append(int(input()))

#finding all possible pairs
print("The pairs are:- ")
for i in range(value_of_n):
    for j in range(i+1, value_of_n):
        if (li[i]*li[j])%2 != 0:
            print("({},{})".format(li[i], li[j]))
