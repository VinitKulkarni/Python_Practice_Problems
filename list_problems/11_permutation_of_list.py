'''
@Author: Vinit 
@Date: 2023-10-13 10:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to generate all permutations of a list in Python.
'''

from itertools import permutations

my_list = [1,9,5]

perm_result = permutations(my_list)

for item in perm_result:
    print(item)