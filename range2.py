'''Author: Job Thomas cherian
   Date:29/10/2024
   program to find prime numbers upto n numbers'''

limit=int(input("Enter a number: "))
for i in range(2, limit +1):
    isprime= True
    for i in range(2,(limit//2)+1):
        if limit % i ==0:
            isprime=False
        break
if isprime:
    print(f"{limit} is prime")
else :
    print(f"{limit} not a prime")