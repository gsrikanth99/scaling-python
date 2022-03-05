#This function calculates the sum of elements in an array
# Author Srikanth
#Date Mar 5,2022
def sumArray(mylist):
    sum=0
    for i in mylist:
        sum = sum+i
    return sum


#Driver Program
lst =[2,5,10, 83, 7]
final_sum = sumArray(lst)
print(f"The sum of array is {final_sum}")
