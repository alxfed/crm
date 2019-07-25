import pandas as pd
import numpy as np

data1 = pd.DataFrame(np.ones((6, 3), dtype=float),
                  columns=['a', 'b', 'c'],
                  index=pd.date_range('6/12/2012', periods=6))

data2 = pd.DataFrame(np.ones((6, 3), dtype=float) * 2,
                  columns=['a', 'b', 'c'],
                  index=pd.date_range('6/13/2012', periods=6))

def AddTogether(row):
    all_of_it = row['People']+' '+ row['emails']
    plus = '+'
    return pd.Series([all_of_it, plus])

data = {'People':['Alex', 'Nancy'],
        'emails':['alxfed@gmail.com', 'nlind@gmail.com']}

data3 = pd.DataFrame(data)

data3[['All of it', 'Plus']] = data3.apply(AddTogether, axis=1)

print('ok')
'''
# Use the height and width to calculate the area
def calculate_area(row):
    return row['height'] * row['width']

rectangles_df.apply(calculate_area, axis=1)


# Use .apply to save the new column if we'd like
rectangles_df['area'] = rectangles_df.apply(calculate_area, axis=1)
rectangles_df

'''