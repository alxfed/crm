import pandas as pd


def AddTogether(row):
    all_of_it = row['People']+' '+ row['emails']
    plus = '+'
    return pd.Series([all_of_it, plus])

data = {'People':['Alex', 'Nancy'],
        'emails':['alxfed@gmail.com', 'nlind@gmail.com']}

data3 = pd.DataFrame(data)

data3[['All of it', 'Plus']] = data3.apply(AddTogether, axis=1)

print('ok')
