# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of 
# mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person
#  who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of 
#  the number of times they appear in the file. After the dictionary is produced, the program reads through the
#   dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

bigWord = None
bigCount = None
for lines in handle:
   
    line = lines.rstrip().split()
    if 'From' in line:
       
        l = line[1]
        counts[l] = counts.get(l,0)+1 
       
for word,count in counts.items():
     if bigCount is None or count>bigCount:
         bigCount = count
         bigWord = word

print(bigWord,bigCount)


