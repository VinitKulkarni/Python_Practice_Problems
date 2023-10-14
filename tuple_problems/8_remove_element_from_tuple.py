'''
@Author: Vinit 
@Date: 2023-10-13 16:30:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to remove an item from a tuple.
'''

my_tuple = (1, 2, 3.3, 'four', True, [])

#removing element directly not possible in tuple

my_list = list(my_tuple)
my_list.pop(-1)
new_tuple = tuple(my_list)
print(new_tuple)