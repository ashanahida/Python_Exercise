def greet():
    name = input("Enter name: ")
    print("Hi, ",name)

greet()

def Gmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isgreater(a,b):
    if (a>b):
        print("1st number is greater")
    else:
        print("2nd number is greater or equal")

def islesser(a,b):
    if(a<b):
        print("1st number is lesser")
    else:
        print("2nd number is lesser or equal")

def isSum(a,b):
    pass   #you can write this function later 

a = 3
b = 5
isgreater(a,b)
islesser(a,b)
Gmean(a,b)
c = 10
d = 8
isgreater(c,d)
islesser(c,d)