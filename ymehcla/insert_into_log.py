"""
log file in a database
"""
import sqlite3

def conn_and_make_cursor(abs_path):
    """
    Creates connection and makes a cursor. Returns both of them.
    :param abs_path: absolute path to the existing log database
    :return: connection, cursor
    """
    conn = sqlite3.connect(abs_path) # , isolation_level=None) for working without commit
    curs = conn.cursor()
    return conn, curs


def create_table_if_not_exists(curs, table_name, schema):
    par = (table_name, schema)
    curs.execute("create table if not exists ? ?", par)
    return


def add_line(conn, curs, table_name, line):
    par = (table_name, line)
    curs.execute("insert into ? values ?", par)
    conn.commit()
    return


def main():
    """

    :return:
    """
    DB_PATH = '/media/alxfed/toca/dbase/logbase.sqlite'
    SCHE_MA = '(date text, trans text, symbol text, qty text, price text)'
    TBL_NAM = 'log_table_today'
    print('Starting main ')
    try:
        co, cu = conn_and_make_cursor(DB_PATH)
    except sqlite3.Error as er:
        print('sqlite3 Error ', er.args[0])
        exit(246)
    try:
        create_table_if_not_exists(cu, TBL_NAM, SCHE_MA)
    except sqlite3.Error as er:
        print('sqlite3 Error ', er.args[0])

    co.close()


if __name__ == '__main__':
    main()
    print('main - done')