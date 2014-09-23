# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 17:50:53 2014

@author: hang
"""
al="abcdefghijklmnopqrstuvwxyz"
for i in range(25):
    j = i + 1
    for j in range(26):
        s=al[i]+al[j]
        print(s)
        