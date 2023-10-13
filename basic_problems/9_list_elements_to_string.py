'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to concatenate all elements in a list into a string and return it.
'''

my_list = [1, 2, 3, 4, 5]
len_of_list = len(my_list)
string_data = ""


for item in range(len_of_list):
	string_data = string_data + str(my_list[item])
	

print(string_data)
print(type(string_data))


