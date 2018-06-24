# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 22:49:26 2018

@author: Kaustub Sinha
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:17:55 2018

@author: Kaustub Sinha
"""
"""

Q1. (Create a program that fulfills the following specification.)

"""
from functools import reduce
def Print(list1):
    addition = 0
    multiply = 0
    largest = 0
    smallest = 0 
    news = 0
    new_list = []
    addition = reduce((lambda x, y: x + y), list1)
    multiply = reduce((lambda x, y: x * y), list1)
    largest = reduce(lambda x, y: max(x,y), list1)
    smallest = reduce(lambda x, y: min(x,y), list1)
    #news = reduce(lambda x, y: sort(x,y), list1)
    
    list1=[]
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    print(new_list)  
    list1.sort()     

    print('add = ' , addition)
    print('multiply =',multiply)    
    print('Largest =',largest)
    print('Smallest =',smallest)   
    print ('Sortted =', list1)
    
numbers = [int(item) for item in input("Enter the numbers: ").split(",")]
Print(numbers)


"""
Q3. (Create a program that fulfills the following specification.)
"""
def Pattern(Start,End):
    
