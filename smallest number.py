'''
Author:job thomas cherian
Date:15/10/2024
program to determine the smallest number
'''
num1=int(input("enter first number:"))
num2=int(input("enter second number"))
num3=int(input("enter third number "))
if num1<num2 and num1<num3:
    print(num1,"is smallest")
elif num2<num3 and num2<num1:
    print(num2,"is smallest")
else:
    print(num3,"is the smallest")