'''
@Author: Vinit 
@Date: 2023-10-14 15:42:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to count the values associated with key in a
dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
'''

sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, 
               {'id': 2, 'success': False, 'name': 'Rabi'}, 
                {'id': 3, 'success': True, 'name': 'Alex'}]

count = 0
for item in sample_data:
    if (item.get("success") == True):
        count = count + 1


print("These many count are found with Success with True ==> ",count)
