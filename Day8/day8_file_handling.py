file = open("notes.txt", "w")
file.write("Python!")
file.close()

file = open("notes.txt", "a")
file.write("\nFile handling.")
file.close()

file = open("notes.txt", "r")
print(file.read())
file.close()