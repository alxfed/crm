import sqlite3


conn = sqlite3.connect("/media/alxfed/toca/dbase/firstbase.sqlite")
cur = conn.cursor()
cur.execute("select * from yelp limit 5;")

results = cur.fetchall()

print('ok')