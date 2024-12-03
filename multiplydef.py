n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))

def multiply_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        n1+multiply_numbers(n1,n2-1)
        return n1+multiply_numbers(n1,n2-1)
print(multiply_numbers(n1,n2))