#Function definition using recursive method
# Author Srikanth
#Date Mar 5,2022
def factorial(n):
    return 1 if (n==0 or n<0) else n * factorial(n-1)

num= 5
fact =factorial(num)
print(fact)
