'''
@Author: Vinit 
@Date: 2023-10-12 13:00:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

user_input = input("Enter the string:")


if(len(user_input) >= 3):
    if((user_input[-3::]) == "ing"):
        user_input = user_input + "ly"
    else:
        user_input = user_input + "ing"
    print("Result = ", user_input)
else:
    print("!!! String length is less than 3. String unchanged !!!")
    print("Result = ", user_input)


