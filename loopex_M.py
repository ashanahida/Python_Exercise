#creating a timer
import time
timer = int(input("Set the timer : "))
while timer>0:
    print(timer)
    time.sleep(1)
    timer = timer-1
print("Timer is over!!!")

#Printing Even Numbers Up to N
num = int(input("Enter a number:"))
num_start = 2
while num<=num_start:
    if num_start % 2 == 0:
        print("Even numbers are: ",num_start)
    num_start += 1