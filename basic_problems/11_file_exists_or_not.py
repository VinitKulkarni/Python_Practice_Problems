'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to check whether a file exists. 
'''


import os.path

#file exists or not
file_path = 'C:/Users/vinit/PYTHONWORK/firstcode.py'
check_file_status = os.path.isfile(file_path)
print('{0} path status = {1}\n'.format(file_path, check_file_status))


#path exists or not
directory_path = 'C:/Users/vinit/PYTHONWORK'
check_path_status = os.path.exists(directory_path)
print('{0} path exists = {1}'.format(directory_path, check_path_status))