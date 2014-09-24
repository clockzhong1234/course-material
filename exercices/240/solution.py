# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 00:15:32 2014

@author: hang
"""

a = 1
b = 1
f = [1, 1]
for i in range(8):
    c = a + b
    f.append(a+b)
    a = b
    b = c
print ", ".join(str(e) for e in f)
print("...")
