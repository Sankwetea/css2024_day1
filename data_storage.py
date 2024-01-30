# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:42 2024

@author: Sankwetea


"""

"""
#Storing data in Python
1. Lists
2. Dictionaries
3. Data Frames

"""
import pandas

file = pandas.read_csv("country_data.csv")

print(file)

age1 = 30
age2 = 25
age3 = 29

age = [30,25,29,46,22]

print(age)

"""

[30, 25, 29, 46, 22]

"""

print(age[0])

"""
30
"""

print(age[1])
"""
25
"""

print(min(age))
"""
22
"""

print(sum(age))
"""
152
"""

print(len(age))


#print avg(age)
avg = sum(age)/len(age)

print(avg)
"""
30.4
"""

print(age[0:3])

age.append(100)
print(age)
"""
[30, 25, 29, 46, 22, 100]
"""

