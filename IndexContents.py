''' Question: Write a Python program to check whether every even index contains an even number and every odd index contains 
odd number of a given list.

Solution: '''

length = int(input('Enter no. of elements: '))
li = []
print("Enter the elements...")
for i in range(length):
    li.append(int(input()))
    
flag_even = 0
flag_odd = 0

#checking for even indexes
for i in range(len(li)):
    if i%2 == 0:
        if li[i]%2 == 0:
            continue
        else:
            flag_even = 1
            break
            

#checking for odd indexes
for j in range(len(li)):
    if j%2 != 0:
        if li[j]%2 != 0:
            continue
        else:
            flag_odd = 1
            break
            
if flag_even==0 and flag_odd==0:
    print("Both the conditions are satisfied...")
elif flag_even==0 and flag_odd==1:
    print("Only even index condition is satisfied...")
elif flag_even==1 and flag_odd==0:
    print("Only odd index condition is satisfied...")
else:
    print("Both the conditions are not satisfied...")
