student_marks ={'shaila':90,
        'Hasan':78,
        'Dimple':56,
        'Ramu':41,
        'Anike':99,
        'prema':34
}

student_grade= {}
for name in student_marks:
    marks = student_marks[name] #value will store here
    if marks>=90:
        student_grade[name] = "A+"
    elif marks>=80:
        student_grade[name] = "A"
    elif marks>=70:
        student_grade[name] = "B+"
    elif marks>=60:
        student_grade[name] = "B"
    elif marks>=50:
        student_grade[name] = "C+"
    elif marks>=40:
        student_grade[name] = "F"
    
print(student_grade)