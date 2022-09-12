# -*- coding: utf-8 -*-
"""list_methods.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KqcXbBF_IOpWBoaPfYJyYQmuIItCIcCn
"""

# methods

lst = [1,2,3,4,5] # list class object

print(type(lst))

list_len = len(lst) # function
print(list_len)
"""
len() - function
    arguments - 1 argument strictly - list/string
    return - return the length of the given list or string as an integer
"""

"""
append() - method
    Description - It will add the provided eleement into the given list as element at the end of the list
    arguments - 1 argument strictly - int/list/string/tuple/dict/anu class object
    return - None
"""

# methods

lst = [1,2,3,4,5] # list class object

lst.append(10)

# print(lst)

lst.append(1000)

for temp in lst:
  print(temp, end = ' ')

"""
count() - method
    Description - It will return the count of occurence of the element passed as argument in the provided argument
    arguments - 1 argument - any element to search
    return - if available returns no.of occurences, if not available returns 0
"""

fruits = ['apple', 'banana', 'cherry', "cherry", "cherry"]

x = fruits.count("cherr")

x

lst = [] # list class object

lst = lst.append(10)

lst.append(200)
print(lst)