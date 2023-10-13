'''
@Author: Vinit 
@Date: 2023-10-12 15:50:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python program to display formatted text (width=50) as output.
'''
import textwrap

sample_data = '''
    Google was officially launched in 1998 by Larry Page and Sergey Brin to market Google Search, which has become the most used web-based search engine. Larry Page and Sergey Brin, students at Stanford University in California, developed a search algorithm at first known as "BackRub" in 1996, with the help of Scott Hassan and Alan Steremberg. The search engine soon proved successful and the expanding company moved several times, finally settling at Mountain View in 2003. This marked a phase of rapid growth, with the company making its initial public offering in 2004 and quickly becoming one of the world's largest media companies. The company launched Google News in 2002, Gmail in 2004, Google Maps in 2005, Google Chrome in 2008, and the social network known as Google+ in 2011 (which was shut down in April 2019), in addition to many other products. In 2015, Google became the main subsidiary of the holding company Alphabet Inc.
'''

print(textwrap.fill(sample_data, width=50),"\n")

print(textwrap.wrap(sample_data,width=5),"\n")

print(textwrap.shorten(sample_data,width=50),"\n")
