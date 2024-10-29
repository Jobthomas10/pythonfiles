'''Author :Job thomas cherian
   Date :29/10/2024
   program for finding a prime number
   '''

num=int(input("enter a number"))
isprime= True
for i in range(2,(num//2+1)):
  if num%i==0:
      isprime= False
      break
if isprime:
    print(f"{num} is prime")
else:
    print(f"{num} is composite")
