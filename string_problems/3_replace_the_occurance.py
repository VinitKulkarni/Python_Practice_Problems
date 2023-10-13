'''
@Author: Vinit 
@Date: 2023-10-12 14:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''

sample_string = "restart"
new_string = ""
new_string = new_string + sample_string[0]



for item in sample_string[1:]:
    if(item == sample_string[0]):
        new_string = new_string + "$"
    else:
        new_string = new_string + item        


print(new_string)

