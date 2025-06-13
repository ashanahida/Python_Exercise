import math

def prime_checker(number):
    is_prime = True
    if number == 1:
        is_prime = False

    for i in range(2,math.ceil(number/2)+1): #i= 2,3,4,n-1
        if number % i == 0:
            is_prime = False

    if is_prime == True:
        print("Number is prime")
    else:
        print("Number is not prime")

number = int(input("Enter a number:\n"))
prime_checker(number)