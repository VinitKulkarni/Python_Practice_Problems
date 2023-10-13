'''
@Author: Vinit 
@Date: 2023-10-12 15:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python function that takes a list of words and returns the length of the longest
one.
'''


def max_length_print(my_list):
    max_length = 0
    for item in my_list:
        if(max_length < len(item)):
            data = item
            max_length = len(item)
    print("longest string is => ",data)


my_list = ["c","python","java","golanguage"]
max_length_print(my_list)