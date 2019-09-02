"""
sqlalchemy / sqlite and pandas
"""
import pandas as pd
import sqlalchemy as sqla

db = sqla.create_engine("sqlite:////media/alxfed/toca/dbase/firstbase.sqlite")
table = pd.read_sql("select * from yelp limit 5;", db)

print('ok')
