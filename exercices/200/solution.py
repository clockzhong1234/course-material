# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:26:02 2014

@author: hang
"""

def is_prime(num):
    j = 0
    n = int(num ** 0.5) + 1
    for i in range(2, n, 1):
        if num % i == 0:
            j = 1
    if j == 0:
        return False
    else:
        return True