'''How to count words in a file'''

# Read data from user input
name = input('Enter file:')
file = open(name, 'r')

# Count word frequency (update count)
counts = {}
for line in file:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word,0) + 1

# Find the most common word (largest item in a list)
bigcount = None
bigword = None
for word,count in counts.items():
  if bigcount is None or count > bigcount:
    bigword = word
    bigcount = count

print(bigword, bigcount)