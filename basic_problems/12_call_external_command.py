'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a python program to call an external command in Python. 
'''


import subprocess

#this will work in windows
subprocess.run(["notepad"])


#this will not work in windows
#subprocess.run(["ls -l"])
