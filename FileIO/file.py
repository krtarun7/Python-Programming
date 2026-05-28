#This is used to create txt file and write data into it and read data from it
#1. Create a text file
f=open("sample.txt","w")
f.close()

#2. Write data into the text file
f=open("sample.txt","w")
f.write("Hello World")
f.close()

#3. Read data from the text file
f=open("sample.txt","r")
print(f.read())
f.close()

#4. Append data to the text file
f=open("sample.txt","a")
f.write("\nWelcome to Python")  
f.close()

