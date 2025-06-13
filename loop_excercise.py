#display 1 to 10
num = 1
while num<=10:
    print(num)
    num+=1

#Sum of the First N Natural Numbers
sum = 0
n = int(input("Enter N natural number:"))
while n>0 :
    sum =sum+n
    n = n-1
print("Sum of the N numbers :",sum)

#Count down
count_start = int(input("Pick a number:"))
print("Let's count together from",count_start)

while count_start>0:
    print(count_start)
    count_start=count_start-1
    if count_start==0:
        print("Happy new year 2024...!!!")