'''
@Author: Vinit 
@Date: 2023-10-13 13:54:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to remove an item from a set if it is present in the set
'''

my_set = {"hi","how","are",'You'}
print(my_set)


#remove the elements if present
my_set.discard('hi')
print(my_set)