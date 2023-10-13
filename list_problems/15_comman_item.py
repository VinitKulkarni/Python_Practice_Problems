'''
@Author: Vinit 
@Date: 2023-10-13 10:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to find common items from two lists
'''

def check_common(list_one, list_two):
    print(set(list_one) & set(list_two))


list_one = [1,2,3,4,5]
list_two = [15,16,17,18,3,1]

#calling the function
check_common(list_one, list_two)