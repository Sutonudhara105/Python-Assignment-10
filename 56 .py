#Write a program to print each line of a file in reverse order.


file = input("Enter the name of the file: ")
fhand = open(file,"r")
for line in fhand:
    line = line[::-1]
    print(line)
