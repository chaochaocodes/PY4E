'''
The data file for this application: http://www.py4e.com/code3/mbox.txt.
'''

import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
# make connection to db, checks access to file
cur = conn.cursor()
# 'handle' to open, send, receive SQL commands

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # extract org from email address aka domain name
    extract_domain = email.split('@')
    org = extract_domain[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    # doesn't read file, checks records; ? = placeholder 
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()