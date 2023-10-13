'''
@Author: Vinit 
@Date: 2023-10-11 10:15:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days 
'''

import datetime 

start_date = datetime.date(2014, 7, 2) 
end_date = datetime.date(2014, 7, 11)

difference = end_date - start_date
print(difference)

