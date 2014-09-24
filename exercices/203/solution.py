# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 18:07:22 2014

@author: hang
"""

def is_multiple(a, b):
    if (a == b) or ((b != 1) and (a % b == 0)):
        return True
    else:
        return False
    