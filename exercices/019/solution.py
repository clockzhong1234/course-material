# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 00:27:56 2014

@author: hang
sys.exit(1) 
"""

import sys
if len(sys.argv) < 2:
    print("Please enter a parameter")
else:
    s = int(sys.argv[1]) + int(sys.argv[2])
    print(s)
