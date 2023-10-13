'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to find out the number of CPUs using
'''


import os

cpu_count = os.cpu_count()
print(cpu_count)