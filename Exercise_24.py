#adding new dict to list
student_data= [{"name":"ram", 
                "roll_no":10, 
                "age":20, 
                "course":"python"},

              {"name":"mohan", 
               "roll_no":20, 
               "age":22, 
               "course":"Java"}]

def add_new_student(name,rollno,age,course_outline):
    new_student={}
    new_student['name'] = name
    new_student['roll_no'] = rollno
    new_student['age'] = age
    new_student['course'] = course_outline
    student_data.append(new_student)

add_new_student(name="shyam",rollno= 22,age=18,course_outline="C++")
print(student_data)