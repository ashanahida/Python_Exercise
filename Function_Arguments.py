def geet(name):
    print(f"Hi {name}")
    print("Are you from CSE department?")
geet("Asha")

#without argument
def studentAge():
    birthYear = int(input("Enter your birth year: "))
    age = int(2024 - birthYear)
    print(f"How old are you? {age}")
studentAge()

#with argument
def teacherAge(age):
    print(f"Your teacher age is: {age}")
teacherAge(45)

#sum of 2 numbers
def sum(a,b):
    sum = a+b
    print(f"summation of two numbers is: {sum}")
sum(2,3)
sum(12,10)