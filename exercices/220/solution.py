# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:26:02 2014

@author: hang
"""

import is_prime
l = []
for i in range(10000, 10050, 1):
    if is_prime.is_prime(i) == True:
        l.append(i)
print(l)
