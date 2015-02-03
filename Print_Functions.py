#open a file to write the output
ans=open("output.txt", "w+") 

ans.write("List of function names found: ")
#Iterate through the entire program file and search for functions
#Print the name of the function into the output file.
with open('program.py') as f:
	for line in f:
		if 'def:' in line:
			ans.write(line)


ans.close()
#close the file

