'''
@Author: Vinit 
@Date: 2023-10-14 15:10:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to remove a key from a dictionary.
'''

sample_dict = {'fname': "Sachin", "lname": "Tendulkar", 'age': 50}

print("deleted key is: ",sample_dict.pop("age"))

print("dictionary after key delete:",sample_dict)