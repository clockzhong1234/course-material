# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 11:17:39 2014

@author: Axel
"""

import requests
from bs4 import BeautifulSoup as bsoup
r = requests.get('http://www.ncbi.nlm.nih.gov/pubmed/?term=gene+network')
doc = r.text
with open('fpubmed.html', "w") as fpubmed:
    fpubmed.write(doc)
soup = bsoup(doc)
#print(soup.title)
#print(doc)
"""print(soup.title.text)"""

count = soup.find_all('meta', {'name':'ncbi_resultcount'})[0]
print(count.attrs)
print(count['content'])


author = soup.find_all('p', { "class" : "desc" })[0]
print(author.text)


