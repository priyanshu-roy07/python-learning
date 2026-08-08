"""#Write in a file and new txt file is created
file = open("file.txt", "w")
file.write("Hello")

#Append in the file
file = open("file.txt", "a")
file.write("\nPriyanshu")

#Read the file
file = open("file.txt", "r")
print(file.read())
file.close()"""


"""file = open("file.txt", "w")
name = input("Enter your name: ")
file.write(name)

file = open("file.txt", "r")
print(file.read())
file.close()"""


#MINI CHALLENGE
"""Asks for 3 names
Saves each name on a new line
Reads the file
Prints all three names"""

with open("file.txt", "w") as file:
    for i in range(0,3):
        name = input("Enter your name: ")
        file.write(name + "\n")
    file.close()

with open("file.txt", "r") as file:
    print(file.read())