'''
@Author: Vinit 
@Date: 2023-10-13 13:56:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to create a union, intersection, difference of sets.
'''

sample_set1 = {1,2,3}
sample_set2 = {3,4,5}

#union
print(sample_set1 | sample_set2)

#intersection
print(sample_set1 & sample_set2)

#difference
print(sample_set1.difference(sample_set2))
