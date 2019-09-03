import sqlite3


conn = sqlite3.connect("/media/alxfed/toca/dbase/firstbase.sqlite")
cur = conn.cursor()
cur.execute("select Name, Address, phone_mobile from yelp limit 3;")
results = cur.fetchall()
# val, = results[0]

conn.close()
print('ok')