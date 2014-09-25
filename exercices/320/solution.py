# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 18:37:44 2014

@author: hang
"""
import string
dict_al = dict.fromkeys(string.ascii_lowercase, 0)
f = open('words', 'r')
content = f.read()
al = ""
for i in range(len(content)):
    if content[i].isalpha() == True:
        al = al + content[i]
count = 0
al = al.lower()
for letter in al:
    if letter in dict_al.keys():
        dict_al[letter] += 1
        count += 1
for key in dict_al:
    print("{}: {:.2f}".format(key, dict_al[key] / count))
    

