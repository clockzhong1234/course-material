# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 22:46:19 2014

@author: hang
"""
import operator
from functools import reduce

def mul(n):
    rs = reduce(operator.mul, n, 1)
    print(rs)
