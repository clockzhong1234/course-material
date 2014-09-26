# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 16:07:49 2014

@author: hang
"""
import json
f = open('velib.json','r')
dict = json.load(f)

with open('solution_velib.json', 'w') as outfile:
  json.dump(dict, outfile)

