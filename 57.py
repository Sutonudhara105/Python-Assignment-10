#Write a program to copy the content of the text file to another file by converting all lowercase characters to uppercase.


file1 = input("Enter the name of first file: ")
file2 = input("Enter the name of second file: ")

f1 = open(file1, "r")
f2 = open(file2, "w")

for line in f1:
    line = line.upper()
    f2.write(line)

f2 = open(file2, "r")
for line in f2:
    print(line)
