'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: Vinit
@Last Modified time: 2023-10-11 15:40:00
@Title : Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''


my_list = [1, 5, 8, 3]

present = True
absent = False
search_element = 3

if search_element in my_list:
    print(present)
else:
    print(absent)