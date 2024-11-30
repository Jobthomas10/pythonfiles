"""
   Author :Job thoomas cherian
   Date :30/11/24
"""

def count(sentc):
    uppercase=0
    lowercase=0
    space=0
    digits=0
    for ltr in sentc:
        if ltr.isupper():
            uppercase+=1
        elif ltr.isspace():
            space+=1
        elif ltr.isdigit():
            digits+=1
        else:
            lowercase+=1
    print("no of uppercase:",uppercase)
    print("no of lowercase:",lowercase)
    print("no of spaces:",space)
    print("no of digits:",digits)
sentc=input("Enter the string:")
count(sentc)