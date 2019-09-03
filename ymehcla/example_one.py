"""
sqlalchemy / sqlite and pandas
"""
import pandas as pd
import sqlalchemy as sqla

db = sqla.create_engine("sqlite:////media/alxfed/toca/dbase/firstbase.sqlite")
table = pd.read_sql_table(table_name="yelp", con=db, columns=['Name'])
list = table.values

for one in list:
    v, = one
    pass

print('ok')
