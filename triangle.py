"""
Author:job thomas cherian
Date:30/11/24
"""
def right_triangle(a,b,c):
    if a^2+b^2==c^2:
        print("right triangle")
    else:
        print("not a right triangle")

one_side= int(input("Enter the length of the first side"))
sec_side=int(input("Enter the length of the second side"))
third_side=int(input("Enter the length of the third side"))
right_triangle(one_side,sec_side,third_side)


