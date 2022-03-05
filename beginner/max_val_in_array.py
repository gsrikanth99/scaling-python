#This function is to calculate the maximum value in an array
# Author Srikanth
#Date Mar 5,2022
def max_val_in_array(myarr):
    maxVal=myarr[0]
    for i in myarr:
        if i > maxVal:
            maxVal=i
    return maxVal


#Driver Program
lst=[3,81,90,43,5]
maxVal=max_val_in_array(lst)
print(f"Maximum value in array is {maxVal}")
