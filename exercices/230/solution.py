# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:26:02 2014

@author: hang
"""

import is_prime
import itertools
n = itertools.count(100000001)
for i in n:
    if is_prime.is_prime(i) == True:
        print(i)
        break
