'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to create a histogram from a given list of integers.
'''


my_list = [2,3,6,1]

for item in my_list:
    pattern = ''
    while item > 0:
        pattern = pattern + "x"
        item = item - 1
    print(pattern)
