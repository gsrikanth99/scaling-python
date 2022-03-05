#This function is to rotate an array using slicing
# Author Srikanth
#Date Mar 5,2022
# all keyword results true if all the values are True
def isMonotonic(arr):
    n = len(arr)
    if n ==1:
        return true
    else:
        if all(arr[i]>arr[i+1] for i in range(0,n-1) or arr[i]<=arr[i+1] for i in range(0, n-1)):
            return True
        else:
            return False
A=[6,4,2,1]
print(isMonotonic(A))
B=[81,9,24,5]
print(isMonotonic(B))
