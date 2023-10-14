'''
@Author: Vinit 
@Date: 2023-10-14 16:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to check multiple keys exists in a dictionary.
'''

sample_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
key_check_list = [1,5,10]


for item in key_check_list:
    if item in sample_dict.keys():
        print(item," result = found")
    else:
        print(item," not found")