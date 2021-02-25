# Putting it all together
'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates
a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the 
dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(name)

senders = list()
for line in handle:
    if line.startswith('From:'): 
        continue
    if line.startswith('From'):
        line = line.split()
        senders.append(line[1])

counts = dict()
for sender in senders:
    counts[sender] = counts.get(sender, 0) + 1

emailsender = None
mostmessages = None
for sender, messages in counts.items():
    if mostmessages is None or messages > mostmessages:
        emailsender = sender
        mostmessages = messages
print(emailsender, mostmessages)