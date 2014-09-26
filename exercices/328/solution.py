# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 22:46:19 2014

@author: hang
"""
# import operator
# from functools import reduce
#
# def mul(n):
#    rs = reduce(operator.mul, n, 1)
#    return rs

def mul(n):
    acc = 1
    for i in n:
        acc *= i
    return acc
    
#    print(mul_2([1,2,3])+mul_2([1,2,3]))