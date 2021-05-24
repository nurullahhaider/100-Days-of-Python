# write a program to convert student scores to grades V2
# store student_scores as dictionary using key:value pair
student_scores = {  "John": 82, "Ron": 78, "Hermione": 99, "Dan": 73, "Neville": 62,}
student_grades = {}
for key,value in student_scores.items(): 
    if value > 90: 
        student_grades[key] = "Outstanding" 
    elif value > 80: 
        student_grades[key] = "Exceeds Expectations" 
    elif value > 70: 
        student_grades[key] = "Acceptable" 
    else: student_grades[key] = "Fail"

print(student_grades)
