'''
@Author: Vinit 
@Date: 2023-10-13 10:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

#sort the list
sample_list.sort()
#print(sample_list)


#add the elements to new elements if not present
new_list = []
for item in sample_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)


