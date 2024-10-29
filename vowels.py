'''Author: Job thomas cherian
   Date :29/10/2028'''
string=input("enter a string")
vowels="aeiouAEIOU"
vcount =0
for a in string:
    if a in vowels:
        vcount+=1
print(vcount)
