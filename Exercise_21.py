import math

def number_of_can(height,width,coverge=7):
    can = (height*width)/coverge
    total_can =math.ceil(can)
    print(f"Total {total_can} cans are needed to paint the wall.")

h = int(input("Enter walls height in sq: "))
w = int(input("Enter walls width in sq: "))
number_of_can(height=h,width=w)