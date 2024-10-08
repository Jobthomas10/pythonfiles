'''
Author:Job Thomas Cherian
Date:08/10/2024
program of date and time
'''

from datetime import datetime
current=datetime.now()
print(current)
currenttime=datetime.now()
print(currenttime)
format1=currenttime.strftime("%Y-%m-%d")
print(format1)
format2=currenttime.strftime("%d-%b-%Y")
print(format2)
format3=currenttime.strftime("%H:%M:%S:%p")
print(format3)
