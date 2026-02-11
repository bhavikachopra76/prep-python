import os  # used for file and directory operations

# Reading a File

f = open("demo.txt", "r")  # open file in read mode
print(f.read())  # read entire file content

line = f.readline()  # read one line at a time
print(line)
f.close()  # close file to free resources


# Writing to a file

f = open("demo.txt", "w")  # open file in write mode (overwrites existing content)
f.write("Hello World")  # write text into file
f.close()

f = open("demo.txt", "r")
print(f.read())  # verify written content
f.close()


# Appending to a file

f = open("demo.txt", "a")  # open file in append mode
f.write("\nHi my name is bhavika")  # add content without overwriting
f.close()

f = open("demo.txt", "r")
print(f.read())  # verify appended content
f.close()


# Using 'with' Statement

with open("demo.txt", "r") as f:  # automatically handles closing
    data = f.read()
    print(data)


# Deleting a File

os.remove("sample.txt")  # deletes file named 'sample.txt' from current directory
