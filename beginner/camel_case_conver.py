#Definition of a function to find the ascii value of a char
# Author Srikanth
#Date Mar 5,2022
def findAscii(x):
    return ord(x)
#This function checks the ascii value of the letter and appends space if needed
def camelCaseWords(word):
    newwordList=[]
    for i in word:
        if findAscii(i)<97 and findAscii(i)>64:
            i= " "+i
        newwordList.append(i)
    newword=''.join(newwordList)
    return newword

#Driver Program
#ascii_val=findAscii('a')
#print(f"The ascii value is {ascii_val}")
final_word= camelCaseWords("CamelCaseWordsAreAppropriateInVariableDeclaration")
print(final_word)
