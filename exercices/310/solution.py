# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 01:03:38 2014

@author: hang
"""
f = open('words', 'r')
content = f.read()
count = 0
for i in range(len(content)):
    if content[i] == "e":
        count = count + 1    
print(count)
