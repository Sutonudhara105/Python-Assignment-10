#Write a program to copy one Python script into another in such a way that all comment lines are skipped and not copied in the destination file.

file1 = input("Enter the name of first file: ")
file2 = input("Enter the name of second file: ")

f1 = open(file1, "r")
f2 = open(file2, "w")

for line in f1:
    if line.startswith("#"):
        continue
    f2.write(line)

f2 = open(file2, "r")
for line in f2:
    print(line)
