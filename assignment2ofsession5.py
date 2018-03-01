# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:21:08 2018

@author: lokesh.r
"""

subject = ["Americans","Indians"]
verb = ["play","watch"]
obj = ["Baseball","Cricket"]

for s in subject:
    for v in verb:
        for o in obj:
            print("%s %s %s" %(s,v,o))