def calculate_average(marks):
    return sum(marks)/len(marks)

def is_pass(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"