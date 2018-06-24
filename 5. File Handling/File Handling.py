# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 22:58:20 2018

@author: Kaustub Sinha
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:07:18 2018

@author: Kaustub Sinha
"""

"""
Q1. (Create a program that fulfills the following specification.)\

"""

def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return 'FizzBuzz'

    elif num % 3 == 0:
        return 'Fizz'

    elif num % 5==0:
        return 'Buzz'
    
    else:
        return num

for n in range(1,51):
    print(fizz_buzz(n))
    
"""
Q2. (Create a program that fulfills the following specification.)

"""
vList = "aeiou "
TemList = []
finalOut = []
inData = input("Enter a string  : ")

for i in inData:
    if(i not in vList):
        TemList.append(i+'o'+i)
    else:
        TemList.append(i)
print ("".join(TemList))
        
"""
Q3. (Create a program that fulfills the following specification.)

"""
"""
GrayScale
"""
from PIL import Image
img = Image.open("sample.jpg")
img_info = img.info
print (img.size)
img.convert("L").show()

"""
Rotate Image
"""
img.rotate(90).show()

"""
Crop (Center) (size = 160(W), 204(H))
"""
box = [100,100,300,300]
img.crop(box).show()

"""
ThumbNail
"""
"""
Crop (Center) (size = 160(W), 204(H))
"""
img.Thumbnail(75,75).show()
