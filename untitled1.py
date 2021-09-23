# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:40:33 2021

@author: Angel
"""

a = ['apple','melon', 'orange','pine apple']
#for i in range(3):
#    print(a[i])
    
b = set(a) 
#print(b)

b.add('grape')
#print(b)

b.add('apple')
#print(b)

b.remove('apple')
#print(b)

b.discard('apple')
#print(b)

b.pop()
#print(b)

set1 = {''}