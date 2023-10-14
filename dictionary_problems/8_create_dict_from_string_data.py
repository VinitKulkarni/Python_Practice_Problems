'''
@Author: Vinit 
@Date: 2023-10-14 15:35:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''

my_dict = {}
sample_string = "w3resource"

for item in sample_string:
    if item in my_dict:
        my_dict[item] += 1
    else:
        my_dict[item] = 1

print(my_dict)