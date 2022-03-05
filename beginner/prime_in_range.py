# This function is to list all the prime numbers in a range, do not include the last number
def printPrime(x,y):
    prime_list=[] #initializing a list to store prime values
    for i in range(x,y): # Iterator to loop thru x and y range
        if i ==0 or i==1:
            continue
        else:
            for j in range(2, int(i/2)+1): #Looping thru half value of the number is enough
                if i % j ==0: # If i is divisible by the iterator j then break
                    break
            else:
                prime_list.append(i)
    return(prime_list)

# Driver Prorgam
x=1
y=50
prime_list= printPrime(x,y)
print(f"{prime_list}")
