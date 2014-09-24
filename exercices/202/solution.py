# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:26:02 2014

@author: hang
"""

def start_with(input, value):
    m = len(input)
    n = len(value)
    if m > n :
        d = m - n
        back = input[-d:]
        new_input = value + back
        if new_input == input:
            return True
        else:
            return False
    elif m == n:
        if input == value:
            return True
        else:
            return False
    else:
        return False
        