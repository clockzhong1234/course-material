# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 17:50:53 2014

@author: hang
"""
al="abcdefghijklmnopqrstuvwxyz"
for i in range(25):
    for j in range(i+1,26,1):
        s=al[i]+al[j]
        print(s)
        
                