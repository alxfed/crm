import sqlite3


db_path = '/media/alxfed/toca/dbase/logbase.sqlite'
sche_ma = '(date text, trans text, symbol text, qty text, price text)'
tbl_name = 'log_table_today'

def ConnMakeCursor(abs_path):
    conn = sqlite3.connect(abs_path, isolation_level=None)
    curs = conn.cursor()
    return conn, curs


def CreateTableIfNotExists(curs, table_name, schema):
    par = (table_name, schema)
    curs.execute("create table if not exists ? ?", par)


def AddLine(curs, table_name, line):
    par = (table_name, line)
    curs.execute("insert into ? values ?", par)


co, cu = ConnMakeCursor(db_path)
try:
    CreateTableIfNotExists(cu, tbl_name, sche_ma)
except sqlite3.Error:
    print('sqlite3 Error')
li = ()




co.close()
print('ok')