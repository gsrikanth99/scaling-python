def factorial(n):
    return 1 if (n==0 or n<0) else n * factorial(n-1)

num= 5
fact =factorial(num)
print(fact)
