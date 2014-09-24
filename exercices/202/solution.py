# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:26:02 2014

@author: hang
"""

def start_with(input, value):
    m = len(input)
    n = len(value)
    d = m - n
    if (input == value) or ((value + input[-d:]) == input):
        return True
    else:
        return False
        