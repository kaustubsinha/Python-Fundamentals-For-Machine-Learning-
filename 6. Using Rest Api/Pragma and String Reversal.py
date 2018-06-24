# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 23:10:12 2018

@author: Kaustub Sinha
"""
"""
Q1. (Create a program that fulfills the following specification.)
"""

def panagram(nt):
    check="abcdefghijklmnopqrstuvwxyz"
    for l in check:
        if(l in nt):
            continue
        else:
            return False
    return True           
n=input("Enter Any Text:")
if(panagram(n.lower())):
    print("Yes It is a Pangram")
else:
    print("No It is not a Pangram") 
    
    
    
"""
Q2. (Create a program that fulfills the following specification.)

"""
def Rev(s):
    list1=[]
    list2=[]
    str1= " "
    for i in s:
        list1.append(i)
    list2 = list1[::-1]
    str1 = ("".join(list2))
    print(str1)
    
data = str(input("Enter a String :"))
print(Rev(data))