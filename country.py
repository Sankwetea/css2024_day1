# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:13:38 2024

@author: Sankwetea
"""
import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

print(file.describe())
"""
           Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000
"""

file = pandas.read_csv("iris.csv")

print(file)

print(file.info())

file = pandas.read_csv("insurance_data.csv",skiprows=5)

print(file)

"""
   X      Y
0   108  392.5
1    19   46.2
2    13   15.7
3   124  422.2
4    40  119.4
..  ...    ...
58    9   87.4
59   31  209.8
60   14   95.5
61   53  244.6
62   26  187.5
"""

file = pandas.read_csv("housing_data.csv")


print(file)

print(file.info)


"""
    0.00632   18   2.31    0  0.538  6.575  ...  1    296  15.3   396.9  4.98    24
0    0.02731  0.0   7.07  0.0  0.469  6.421  ...  2  242.0  17.8  396.90  9.14  21.6
1    0.02729  0.0   7.07  0.0  0.469  7.185  ...  2  242.0  17.8  392.83  4.03  34.7
2    0.03237  0.0   2.18  0.0  0.458  6.998  ...  3  222.0  18.7  394.63  2.94  33.4
3    0.06905  0.0   2.18  0.0  0.458  7.147  ...  3  222.0  18.7  396.90  5.33  36.2
4    0.02985  0.0   2.18  0.0  0.458  6.430  ...  3  222.0  18.7  394.12  5.21  28.7
..       ...  ...    ...  ...    ...    ...  ... ..    ...   ...     ...   ...   ...
500  0.06263  0.0  11.93  0.0  0.573  6.593  ...  1  273.0  21.0  391.99  9.67  22.4
501  0.04527  0.0  11.93  0.0  0.573  6.120  ...  1  273.0  21.0  396.90  9.08  20.6
502  0.06076  0.0  11.93  0.0  0.573  6.976  ...  1  273.0  21.0  396.90  5.64  23.9
503  0.10959  0.0  11.93  0.0  0.573  6.794  ...  1  273.0  21.0  393.45  6.48  22.0
504  0.04741  0.0  11.93  0.0  0.573  6.030  ...  1  273.0  21.0  396.90  7.88  11.9

[505 rows x 14 columns]

"""

column_names = ["A", "B", "C" ....]

file =pandas.read_csv("housing_data.csv", 

import numpy as np

arr = np.array([1, 2, 3, 4 , 5])

print(arr)

print(type(arr))


names = ["A", "B", "C"]
file =pandas.read_csv("housing_data.csv", names = ["A", "B"])
print(file(info))

"""
Dictionaries - key:value pairs

cat: "a feline mammal"

"""

mammals ={"cat" : "a feline mammal"," lion " : " king of the jungle","elephant":"Africanis loxondata"}
print(mammals["cat"])


"""
Data frames

df = dataframe
"""

fruits = ["apples", "oranges" ,"lemons"]
size_nm = [14, 3, 5]

prices = ["5.00" , "15.00" ,"16.00" ]

dataframe[ 'prices'] = prices
df.drop(columns=["sizes"])
