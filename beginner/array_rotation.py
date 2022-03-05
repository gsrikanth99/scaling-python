#This function is to rotate an array
# Author Srikanth
#Date Mar 5,2022
# 1,2,3,4,5,6 , rotate by 2 -> output 3,4,5,6,1,2
def rotateArrayleft(myArr):
    x=myArr[0]
    for i in range(len(myArr)-1):
        myArr[i]=myArr[i+1]
    myArr[len(myArr)-1]=x
    return myArr

def rotateArrayright(myArr):
    x=myArr[len(myArr)-1]
    for i in range(len(myArr)-1,0,-1):
        myArr[i]=myArr[i-1]
    myArr[0]=x
    return myArr

arr=[1,2,3,4,5,6,7]
#new_arr=rotateArrayleft(arr)
n=1
for i in range(n):
    new_arr=rotateArrayright(arr)
print(new_arr)
