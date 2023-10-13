'''
@Author: Vinit 
@Date: 2023-10-12 15:30:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
'''

sample_words = input("Enter:").split(",")

#converted list to set for the unique elements
my_set = set(sample_words)

#sort and convert it to list
sorted_unique_words = sorted(my_set)
print(sorted_unique_words)

