''' Question: Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

Solution: '''

# Function to find GCD
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

gcd = compute_gcd(300, 400)
print("The GCD is", gcd)
