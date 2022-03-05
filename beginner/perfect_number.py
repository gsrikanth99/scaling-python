# A perfect number is the one whose
# sum of divisors are equal to the number
# Author Srikanth
# Date Mar 5,2022

def isperfectnum(n):
    # number is always divisible by 1
    sum=1
    i =2
    while i * i < n:
        if n % i ==0:
            sum = sum + i + n/i  # sum is sum of the iterator i and also n/i
        i = i +1 # increment for the while loop
    return sum if n == sum and n != 1 else False

#Driver program
n =2
for n in range(10000):
    if isperfectnum(n):
        print(f"{n} is a perfect number") 
