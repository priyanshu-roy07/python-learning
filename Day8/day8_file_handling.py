"""file = open("notes.txt", "w")
file.write("Python!")
file.close()

file = open("notes.txt", "a")
file.write("\nFile handling.")
file.close()
"""
"""file = open("notes.txt", "r")
print(file.read())
file.close()"""

"""with open("notes.txt", "r") as file:
    #print(file.readline())
    print(file.readlines())
    #print(file.read())
"""
with open("notes.txt", "r") as file:
    lines = file.readlines()
print(lines[0])
#for line in lines:
 #   print(line)