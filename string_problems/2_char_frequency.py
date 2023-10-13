'''
@Author: Vinit 
@Date: 2023-10-12 14:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to count the number of characters (character frequency) in a
string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

sample_string = "google.com"

#empty dict
my_dict = {}

for char in sample_string:
    if char in my_dict:
        my_dict[char] = my_dict[char] + 1
    else:
        my_dict[char] = 1 
    
print(my_dict)

