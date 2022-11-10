# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
#  each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting 
#  the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = 0
lst = dict()
for line in handle:
    if not line.startswith("From"):
        continue
    else:
        line = line.rstrip().split()
        if len(line)>5:
            word =line[5]
            word = word[0:2]
            lst[word] = lst.get(word,0) +1

for k,v in sorted(lst.items()):
   print(k,v)        
    