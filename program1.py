#Ask for a sentence
#print length of the sentence
# Ask for a file name
#Write the sentence to the file
#run the program from the command line
sentence=input("Enter a sentence")
print(len(sentence))
sentence_length= len(sentence)
file_name = input("Enter a file name")
file_name = f"{file_name}.txt"
with open(file_name , "w") as f:
	f.write(sentence)
	f.close()
print(f"You have written {sentence_length} characters to {file_name}")
