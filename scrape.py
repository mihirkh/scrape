#!/usr/bin/env python
# coding: utf-8
import time
import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/fare.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
alinks = soup.findAll('a')
link = alinks[34]['href']
prefix = 'http://web.mta.info/developers/'
link[link.find('fares_'):]
urllib.request.urlretrieve(prefix+link,link[link.find('fares_'):])

#for i in range(34,len(alinks)):
for i in range(34,38):
    link = alinks[i]['href']
    urllib.request.urlretrieve(prefix+link,'data/'+link[link.find('fares_'):])
    print(i)
    time.sleep(1)

