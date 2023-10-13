'''
@Author: Vinit 
@Date: 2023-10-13 10:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python function that takes two lists and returns True if they have at
least one common member.
'''

def check_common(list_one, list_two):
    temp = set(list_one) & set(list_two)
    if len(temp) > 0:
        return True
    else:
        return False


list_one = [1,2,3,4,5]
list_two = [15,16,17,18,3]

#calling the function
print(check_common(list_one, list_two))


#print(set(list_one) | set(list_two)) #union
#print(set(list_one) & set(list_two)) #intersection
#print(set(list_one) ^ set(list_two)) #difference
