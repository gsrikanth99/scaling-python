#Function to find if a number is prime or not
def isPrime(n):
    i =1
    for i in range(2, int(n/2)+1):
        if n % i ==0:
            break
        else:
            return(i)


#Driver Program
n =7
if isPrime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
