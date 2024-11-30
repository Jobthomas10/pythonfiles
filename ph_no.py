def number(a):
    if len(a)==10 and a[0] in "789":
        print('your number is valid')
    else:
        print("number is invalid")

mobile_no=input("enter the mobile number")
number(mobile_no)