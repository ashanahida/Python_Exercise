#Arbitray positional(*args)

def average(*numbers):
    c = 0
    print(numbers[1])
    for i in numbers:
        c += i
    print("sum is: ",c)
    print("average is: ",c/len(numbers))

average(2,3)
average(4,5,6)
average(34,22,54,32,453,223)

#Arbitray keyword(**kwargs)

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
student_info(name= "Ram",age = 25,dept = "Data science")
student_info(name = "Maya", dept = "CSE", major ="Software")

#args & kwargs
def employee(*args,**kwargs):
    print(args)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
employee(1,name="jamal",position="faculty")
employee(2,name="jastin",postion="Teacher Assistant")


#exercise
def multiply(*args):
    c = 1
    for i in args:
        c = c*i
    print("multipication is:",c)
multiply(2,3,-6,8)
multiply(2,5,8,9,4,6)