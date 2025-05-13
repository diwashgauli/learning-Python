# file=open('sample.txt','r')
# # content=file.read() #outputs whole content of the file 
# # print(content)

# line1=file.readline() #outputs line where the pointer last points 
# line2=file.readline()
# print(line1)
# print(line2)
# print(file.readlines()) #outputs all the lines starting from the pointer last points in the form of lists 

# file.close()
# file.read() #gives err because we already closed the file.


#context manager syntax. it automatically closes the file
# with open('sample.txt','r') as file:
#     print(file.readlines())

# file.read() #gives err because file is already closed.


with open('sample.txt','r') as file:
    for line in file:
        print(line.strip())



with open('newfile.txt','w') as file:
    # file.write("This is line 1.\nThis is line 2.")
    file.write("Hello.\nWorld.\n") #truncate the existing file and override the content if new content already exists in a file when opened in a write mode and written we can consecutively write in a opened file it wont override.
    data=["This is line1\n","This is line2"]
    file.writelines(data)

with open('newfile.txt','a') as file:
    file.write("\nThis is appended.")
    