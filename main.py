import sqlite3

conn = sqlite3.connect('forest.db')
cur = conn.cursor()
sud_lvl = int(input())
terrain = input()
cur.execute("SELECT name, looks_like FROM Events WHERE suddenness >= ? AND 'place' = ?", (sud_lvl, terrain))
recults = cur.fetchall()
children = {}
looks = set()
for rec in recults:
    child = rec[0]
    look = rec[1]
    looks.add(look)
    if child in children:
        children[child].add(look)
    else:
        children[child] = {look}
for child in sorted(children.keys()):
    print(child, end=', ')
    print()
for look in sorted(looks):
    print(look, end=', ')
conn.close()