# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 01:03:38 2014

@author: hang
"""

def euclidean(a, b):
    d = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    return d

def opt_euclidean(a, b):
    import math
    c = []
    for i in range (2):
        d = a[i]-b[i]
        d = math.pow(d,2)
        c.append(d)        
    distm = math.sqrt(math.fsum(c))
    return distm
    
def np_euclidean(a, b):
    import numpy as np
    x = np.array(a) 
    y = np.array(b)
    distnp = numpy.linalg.norm(x-y)
    return distnp
