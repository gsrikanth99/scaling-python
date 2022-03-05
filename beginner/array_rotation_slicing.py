#This function is to rotate an array using slicing
# Author Srikanth
#Date Mar 5,2022
# 1,2,3,4,5,6 , rotate by 2 -> output 3,4,5,6,1,2
def rotateArrayleftBySlice(myArr):
    n = len(myArr)
    myArr[:]=myArr[1:n]+myArr[0:1]
    return myArr[:]

#Driver Program
arr=[1,2,3,4,5,6,7]
n =4
for i in range(n):
    new_arr=rotateArrayleftBySlice(arr)
print(new_arr)
