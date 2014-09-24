# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 00:27:56 2014

@author: hang
"""

import sys
if len(sys.argv) < 2:
    print("Please enter a parameter")
    sys.exit(1)   
s = int(sys.argv[1]) + int(sys.argv[2])
print(s)
