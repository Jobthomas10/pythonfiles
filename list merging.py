list1=[]
list2=[]
list1_size=int(input("enter the size of the list:"))
print("enter the element")
for i in range(list1_size):
    list1.append(int(input()))
list2_size=int(input("enter the size of list2"))
print(("enter the elements"))
for j in range(list2_size):
    list2.append(int(input()))
    combined_list=list1+list2
    even_list=[]
    odd_list=[]
    for i in combined_list:
        if i%2==0:
            even_list.append(i)
        else:odd_list.append(i)
    even_list.sort()
    odd_list.sort()
    final_list=even_list+odd_list
print(f"The final list is:{final_list}")