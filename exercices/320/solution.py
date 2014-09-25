# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 18:37:44 2014

@author: hang
"""
f = open('words', 'r')
content = f.read()
al = ""
for i in range(len(content)):
    if content[i].isalpha() == True:
        al = al + content[i]
l = len(al)
al = al.lower()
dict_al = { "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, 
"i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
 "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
for letter in al:
    dict_al[letter] += 1/l
for key in dict_al:
    print(key, ": ", '%.2f' % dict_al[key])
