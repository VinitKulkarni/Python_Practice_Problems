'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

input_data = input("Enter the data:")

list_data = list(input_data.split(","))
print(list_data)
print(type(list_data))

tuple_data = tuple(input_data.split(","))
print(tuple_data)
print(type(tuple_data))