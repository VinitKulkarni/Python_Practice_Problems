'''
@Author: Vinit 
@Date: 2023-10-13 14:19:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to use of frozensets.
'''

my_frozenset1 = frozenset(['india','russia','usa'])
my_frozenset2 = frozenset(['china','japan','india'])


union_set = my_frozenset1.union(my_frozenset2)
intersection_set = my_frozenset1.intersection(my_frozenset2)
difference_set = my_frozenset1.difference(my_frozenset2)
symetric_diff_set = my_frozenset1.symmetric_difference(my_frozenset2)

print("union result = ",union_set)
print("intersection result = ",intersection_set)
print("difference result = ",difference_set)
print("symetric diff result = ",symetric_diff_set)