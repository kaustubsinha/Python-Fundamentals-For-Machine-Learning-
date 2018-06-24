# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:10:08 2018

@author: Kaustub Sinha
"""

''' Code Challenge Problem '''
"""
'''Q1. (Create a program that fulfills the following specification.)'''

"""
str1 = """This is a multi line string. This code challenge is to
test your understanding about strings.You need to print some part of this string.
From here print this text without manually counting the indexes."""

Find_start = str1.find('F')
print(Find_start)
print(str1[137:])

print("__________________________________")

"""

'''Q2. (Create a program that fulfills the following specification.)'''

"""

'''str2 = "Welcome to Pink City Jaipur"'''
str2 = input("Please Enter Text")
print(str2)
output2 = str2.replace(' ','*')
print(output2)

print("__________________________________")
"""

Q3. (Create a program that fulfills the following specification.)

"""

'''str3 = "Welcome to Pink City Jaipur"'''
str3 = input("Please Enter Text")
output3 = "*".join(str3)
print(output3)

print("__________________________________")
"""
Q4. (Create a program that fulfills the following specification.)

"""
'''str4 = "Forsk Technologies"'''
str4 = input("Please Enter Text")
index = str4.find(" ")
print (str4[index:].strip(),str4[:index].strip())

print("__________________________________")
