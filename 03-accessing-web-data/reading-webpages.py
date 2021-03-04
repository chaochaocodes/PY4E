'''
Reading Webpages like Files using urllib
'''

import urllib.request, urllib.parse, urllib.error
    
# 1.  Read like a File
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
	print(line.decode().strip())
    # reads the HTML file!
    # returns header + body, but header not returned in this for loop; accessed another way


# 2. Working with the data.  Retrieve and find frequency of words
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    # line is a byte string, decode into character string
    for word in words:
        counts[word]: counts.get(word,0) +  1
print(counts)
# array of words, count and save in dict

