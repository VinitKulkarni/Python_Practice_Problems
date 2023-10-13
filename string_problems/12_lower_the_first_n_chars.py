'''
@Author: Vinit 
@Date: 2023-10-12 18:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to lowercase first n characters in a string.
'''

#n = how many first chars you want to make lower case
n = 4
sample_string = "ReGiStRaTiOn"

print(sample_string[:4].lower() + sample_string[4:])