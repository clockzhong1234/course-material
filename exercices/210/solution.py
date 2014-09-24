# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:26:02 2014

@author: hang
"""

import is_prime
s = 0
for i in range(1000):
    if is_prime.is_prime(i) == True:
        s = s + i
print(s)
       