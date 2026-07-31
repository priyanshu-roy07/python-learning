"""fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits[2])"""

"""numbers = [10, 20, 30, 40, 50]
numbers[2] = 300
print(numbers)"""

"""fruits = ["Apple", "Banana", "Mango", "Banana"]
fruits.remove("Banana")
print(fruits)"""

#Sort the list
"""marks = [85, 92, 78, 95, 88]
marks.sort()
print(marks)"""

#Reverse the list
"""marks = [85, 92, 78, 95, 88]
marks.reverse()
print(marks)"""

"""marks = [45,65,23]
marks.append(87)
marks.append(98)
marks.sort()
print(marks)"""

#Marks with index
"""marks = [45,65,23,76, 89, 12]
for i in range(len(marks)):
    print(i, marks[i])"""

#Total and average in a list
"""marks = [10, 20, 30]
total = 0
for mark in marks:
    total = total + mark
print(total)
average = total/len(marks)
print(average)"""

#Finding largest value
"""marks = [85, 92, 78, 95, 88]
largest = marks[0]
for mark in marks:
    if mark > largest:
        largest = mark
print(f"The largest number is {largest}")"""

#Count students who scored above 90
"""marks = [85, 92, 78, 95, 88, 99]
count = 0
for mark in marks:
    if mark > 90:
        count += 1
print(count)"""