#4 types arguments
#1 positional
def greet(name,dept):
    print(f"Welcome...{name}")
    print(f"Your department is {dept}")
greet("Asha","Data science")

#2 keyword
def sons(son1,son2):
    print(f"His elder son's name is {son1}")
    print(f"His younger son's name is {son2}")
sons(son2="chris",son1="messi")

#mix of positional and keyword
def student(name,score):
    print(f"{name} score is {score}")
student("Towfiq",score=90)

#3 Default
def father(name,age,job="employee"):
    #here job is default arguments
    print(f"Her father's name is {name}")
    print(f"His age is {age}")
    print(f"His occupation is {job}")
father("Mofijur Rahman",56)

def name(a1,a2="asha"):
    print(f"your full name is {a1} {a2}")
name("Nahida")

#4 Arbitray
def add(*numbers):
    c = 0
    for i in numbers:
        c = c+i
    print(f"sum is {c}")
add(22,5,3)
add(2,6,43,3)

