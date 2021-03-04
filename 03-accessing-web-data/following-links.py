'''
Following Links in Python

In this assignment you will write a Python program that will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: 
http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: 
http://py4e-data.dr-chuck.net/known_by_Ogheneochuko.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: C
'''

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')

names = list()
first_name = re.findall('_by_(\S+).html', url)
names.append(first_name)

i = 0
while i < int(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    index = 0
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        index += 1
        if index == int(position):
            print(tag.get('href', None))
            url = tag.get('href', None)
            y = re.findall('_by_(\S+).html', url)
            names.append(y)
            i += 1
        
print(names)
return names[-1]