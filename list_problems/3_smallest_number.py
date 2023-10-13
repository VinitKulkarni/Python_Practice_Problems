'''
@Author: Vinit 
@Date: 2023-10-13 10:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to get the smallest number from a list.
'''

my_list = [10,21,13,19,15]
smallest_element = my_list[0]

for item in my_list:
     if(item < smallest_element):
          smallest_element = item

print("smalles element in list is: ",smallest_element)