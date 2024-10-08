'''
Author: Job Thomas Cherian
Date:08/10/2024
sub-string that consists of the last name only. 
'''
first_name="job"
last_name="thomas"
full_name=first_name+' '+last_name
print(full_name)

length=len(first_name)
print(length)
extracted_first_name=full_name[length+1:]
print(extracted_first_name)
