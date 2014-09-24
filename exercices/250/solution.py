# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 00:38:41 2014

@author: hang
"""

def draw_n_squares(n):
    
    
    r = 1 + 2 * n
    odd = "+"
    for k in range(n):
        odd = odd + "---+"
    even = "|"
    for k in range(n):
        even = even + "   |"
    for i in range(r):
        t = i + 1
        if t % 2 == 0:
            print(even)
        else:
            print(odd)
