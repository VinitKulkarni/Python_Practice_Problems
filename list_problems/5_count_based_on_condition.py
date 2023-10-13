'''
@Author: Vinit 
@Date: 2023-10-13 10:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''


sample_list = ['1','abc', 'xyz', 'aba', '1221']


count = 0
for item in sample_list:
    if len(item) > 2:
        if item[0] == item[-1]:
            count += 1

print(count)

