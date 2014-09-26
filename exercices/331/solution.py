# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 16:07:49 2014

@author: hang
"""
import json
f = open('velib.json','r')
dict = json.load(f)
new_dict={}
for i in range(len(dict)):    
    zipcode = str(dict[i]['address']).split()
    zipcode = zipcode[len(zipcode)-2]
    city = str(dict[i]['address']).split()
    city = "".join(city[len(city)-1])
    name=" ".join(str(dict[i]['name']).split())
    address=dict[i]['address'].split()
    address=" ".join(address[:-3])
    new_dict[i]={"zip_code" : zipcode, "city" : city, "name" : name, "address" : address}
with open('solution_velib.json', 'w') as outfile:
  json.dump(new_dict, outfile)

