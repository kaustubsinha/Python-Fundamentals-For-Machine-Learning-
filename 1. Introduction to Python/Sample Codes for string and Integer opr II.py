# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:08:01 2018

@author: Kaustub Sinha
"""

"""
Q1. (Create a program that fulfills the following specification.)
"""
""" List: '2','4','7','8','9','12'""" 
""" tuple: '2','4','7','8','9','12'""" 

"""List Creation""" 
data1 = input("enter the values")
list =  data1.split(',')
print(list)

"""tuple creation"""
data2 = input("enter the values")
tuple = tuple(data2)
print(tuple)

"""
Q2. (Create a program that fulfills the following specification.)

"""
numbers =  [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for num in numbers:
    print(num)
    
    
"""
Q3. (Create a program that fulfills the following specification.)

"""
url = input("Enter a Url")
dict1 = {}
for item in url:
    if item not in dict.keys():
        dict1[item] =1
    else:
        dict1[item]+=1
        
print(dict1)

"""
Q4. (Create a program that fulfills the following specification.)

"""
str1 = input("Eneter a String")
digit = 0
letter = 0
for x in str1:
    if (x.isalpha()):
        letter+=1
    elif(x.isnumeric()):
        digit+=1

print(letter,digit)

"""
Q5. (Create a program that fulfills the following specification.)
2,6,8,4,7,1,9,3

"""
a = input("Enter a numaric comma saperated value  : ")
b = a.split(',')
c = b[1:-1]
sum_no=0
length=0
for x in c:
    print(x)
    sum_no+=int(x)
    length+=1
print(sum_no,length)
avg=(sum_no/length)
print(avg)

"""
Q6. (Create a program that fulfills the following specification.)
13,1,2,13,2,1,13
"""
'''data = input("Enter a numaric comma saperated value")'''
data = 13, 1, 2, 13, 2, 1, 13
data= list(data)
print(data)

flag = 0
list3=[]

for x in data:
    if(x == 13):
        flag =1
        continue
    if(flag ==0):
        list3.append(x)   
    flag = 0
    
y = sum(list3)
print(y)

