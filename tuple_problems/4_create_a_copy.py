'''
@Author: Vinit 
@Date: 2023-10-13 14:55:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to create the colon of a tuple.
'''


from copy import deepcopy

my_tuple = (1, 2, 3.3, 'four', True, [])


copy_of_my_tuple = deepcopy(my_tuple)
copy_of_my_tuple[5].append(99)



print("original tuple: ",my_tuple)
print("copied tuple: ",copy_of_my_tuple)
