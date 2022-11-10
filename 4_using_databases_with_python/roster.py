import json
import sqlite3

conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

cur.executescript('''

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id, course_id)
);
''')

fname = input("Enter JSON file - ")
if len(fname)<1:
    fname='roster_data.json'
file = open(fname).read()
data = json.loads(file)
for stuff in data:
    name = stuff[0]
    title = stuff[1]
    role =stuff[2]
    # print(name,title,role)
    cur.execute('''
    INSERT OR IGNORE INTO User (name) VALUES (?)
    ''', (name,))
    cur.execute(' SELECT id FROM User WHERE name = ?',(name,))
    user_id =cur.fetchone()[0]

    cur.execute('''
    INSERT OR IGNORE INTO Course (title) VALUES (?)
    ''', (title,))
    cur.execute(' SELECT id FROM Course WHERE title = ?',(title,))
    course_id =cur.fetchone()[0]

    cur.execute('''
    INSERT OR REPLACE INTO Member (user_id,course_id,role) VALUES (?,?,?)
    ''', (user_id,course_id,role))
    conn.commit()

cur.execute('''SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
    ''')

for c in cur:
    print(c[0],c[1],c[2])

cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
''')
for c in cur:
    print(c[0])
cur.close()