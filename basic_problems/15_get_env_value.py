'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a python program to access environment variables. 
'''



import os

#set the env
os.environ["testkey"] = "testvalue"

#get the value of testkey
env_data = os.getenv("testkey")
print(env_data)


#get the env
env_data1 = os.getenv("JAVA_HOME")
print(env_data1)


