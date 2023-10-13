'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'} 
'''


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])


list1 = list(color_list_1)
list2 = list(color_list_2)

len_of_list1 = len(list1)
len_of_list2 = len(list2)


for item1 in range(len_of_list1):
    flag = True
    for item2 in range(len_of_list2):
        if (list1[item1] == list2[item2]):
            flag = False
            break
    #if flag == true
    if (flag == True):
        print(list1[item1])
