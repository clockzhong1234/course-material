# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
if len(sys.argv) < 2:
    print("Please enter two integers and operator for calculation.")
    sys.exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
c = str(sys.argv[2])
print(c)

if c == "+":
    r = a + b
    print(a+b)
if c == "-":
    r = a - b
    print(r)
if c == "*":
    r = a * b
    print(r)
if c == "/":
    r = a / b
    print(r)
if c == "%":
    r = a % b
    print(r)
if c == "^":
    r = a ** b
    print(r)
