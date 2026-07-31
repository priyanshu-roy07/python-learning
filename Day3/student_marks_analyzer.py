"""Highest Mark : 95
Lowest Mark  : 78
Average      : 87.6
Students > 90 : 2
Even marks : 92, 78, 88"""

marks = [85, 92, 78, 95, 88]
total = 0
highest = marks[0]
lowest = marks[0]
count = 0
even = []

for mark in marks:
    if mark > highest:
        highest = mark
    elif mark < lowest:
        lowest = mark
    if mark > 90:
        count += 1
    total += mark
    if mark % 2 == 0:
        even.append(mark)

Average = total/len(marks)
print(f"Highest marks : {highest}")
print(f"Lowest marks : {lowest}")
print(f"total : {total}")
print(f"Average marks : {Average}")
print(f"Students with 90+ marks : {count}")
print(f"Even marks : {even}")
