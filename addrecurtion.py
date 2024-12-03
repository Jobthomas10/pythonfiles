def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        add_numbers(n1+1,n2-1)
        return add_numbers(n1+1,n2-1)
print(add_numbers(n1,n2))
