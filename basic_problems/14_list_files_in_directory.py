'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to list all files in a directory in Python. 
'''


import os
 
path = "C:/Users/vinit/PYTHONWORK"
dir_list = os.listdir(path)
 
print(dir_list)