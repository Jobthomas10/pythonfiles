from colorsys import yiq_to_rgb
'''Author:job thomas cherian
Date:01-10-2024
Python programme to get the student details'''
name=input("Enter the name of the student:")
Roll_number=int(input("Enter your Roll_number:"))
cgp=float(input("Enter your cgp:"))
print("name of the student:",name)
print("Roll_number:",Roll_number)
print("CGP of the student in percentage:",cgp*10,"%")