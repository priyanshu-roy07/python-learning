#Student Performance Analyzer

students = [
    {"name": "Rahul", "marks": [80, 75, 90]},
    {"name": "Priyanshu", "marks": [95, 88, 92]},
    {"name": "Amit", "marks": [60, 65, 70]},
    {"name": "Neha", "marks": [85, 90, 88]},
    {"name": "Riya", "marks": [45, 0, 40]}
]

def calculate_average(*args):
    total = 0 
    for mark in args:
        total += mark
    return total/len(args)
avg = calculate_average(85, 75, 90)
print(avg)

def is_pass(average, passing_marks = 40):
    if average >= passing_marks:
        return "Pass"
    else:
        return "Fail"
print(is_pass(avg))

avgg = map(lambda student : calculate_average(*student["marks"]), students)
print(list(avgg))

passing_students = filter(lambda student : is_pass(calculate_average(*student["marks"])) == "Pass", students)
print(list(passing_students))