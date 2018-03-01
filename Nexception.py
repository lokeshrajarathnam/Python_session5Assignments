# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:11:57 2018

@author: lokesh.r
"""

def numbExcep():
    try:
        n = 5/0
        print(n)
    except ZeroDivisionError :
        print("cannot divide number by zero")
    finally:
        print("please make sure divisor is > 0")
    
numbExcep()
     