#for i in loop:

a = int(input("enter num:"))
if a == 2:
    print("Two")
else:
    print("No")

#while loop
#print name 10 time
name= input("enter ur name:")
x = 0
while x<=10:
    print(name)
    x += 1

#display number 1 to 5
num = 1
while num<=5:
    print(num)
    num += 1
print("end")

#printtable

number = int(input("enter a number from 1 to 10 :"))
x = 1
while x<=10:
    print(f"{number} * {x} = {number*x}")
    x+=1