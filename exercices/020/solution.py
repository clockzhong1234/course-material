# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 00:27:56 2014

@author: hang
"""

import sys
if sys.argv[1] == None or (sys.argv[2]) == None:
    print("Please enter two integers.")
else:
       s = int(sys.argv[1]) - int(sys.argv[2])
       print(s)
       