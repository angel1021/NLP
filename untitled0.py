# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:18:06 2021

@author: Angel
"""

# this is a practice typing

#x = int()
#y = int(input('input number: '))
#for i in range(5):
#    x += y
#print(x)

#def max(a,b):
#    return a if a>b else b
#def min(a,b):
#    return a if a<b else b


#print(f'max number: {max(3,5)}')
#print(f'min number: {min(3,5)}')

#def max(a,b,c):
#    if a>b:
#        big = a
#    else:
#        big = b
#    return c if big<c else big
#big = max(50,3,77)
#print(big)

class Lesson:
    
    teacher = 'Fennie'
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

p = Lesson('Cindy','Cheng')
if __name__ == '__main__':
    print(Lesson.teacher)
    print(p.firstname)
    print(p.lastname)
        

