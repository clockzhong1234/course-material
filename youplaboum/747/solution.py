# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 11:17:39 2014

@author: Axel
"""

import requests
from bs4 import BeautifulSoup as bsoup
r = requests.get('http://www.openwetware.org/wiki/Labs')
doc = r.text
soup = bsoup(doc)
print(soup.title)
print(soup.title.text)
print(soup.toggler)
