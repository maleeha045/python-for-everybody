import urllib.request
import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
fh = open('mbox.txt')
c = 0
for lines in fh:
    
    if not lines.startswith('From:'):
        
     continue
    line = lines.split()
    domain = line[1].split('@')
    email = domain[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
    else:
        
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
    conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

