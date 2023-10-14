'''
@Author: Vinit 
@Date: 2023-10-14 14:30:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''

sample_dict = {0: 10, 1:20}

n = input("how many key values you want to add:")
for item in range(int(n)):
    key = int(input("enter the key:"))
    value = int(input("enter the value:"))
    sample_dict[key] = value


print(sample_dict)