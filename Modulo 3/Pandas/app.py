import pandas as pd
import os

csv_path='sales.csv'
if not os.path.exists(csv_path):
    data=[
        {'date':'2025-12-01',
           'product':'camisa',
           'price':50,
           'quantity':2},
        {'date':'2025-12-01',
           'product':'vestido',
           'price':290,
           'quantity':2},
        {'date':'2025-12-01',
           'product':'calça',
           'price':300,
           'quantity':2},
        {'date':'2025-12-01',
           'product':'blusa',
           'price':250,
           'quantity':2},
        {'date':'2025-12-01',
           'product':'cinto',
           'price':50,
           'quantity':1},
        {'date':'2025-12-01',
           'product':'meias',
           'price':40,
           'quantity':1},
        {'date':'2025-12-01',
           'product':'tênis',
           'price':500,
           'quantity':1},
        {'date':'2025-12-01',
           'product':'chinelo',
           'price':60,
           'quantity':1},
        {'date':'2025-12-01',
           'product':'boné',
           'price':50,
           'quantity':1},
        {'date':'2025-12-01',
           'product':'bermuda',
           'price':100,
           'quantity':2},
        {'date':'2025-12-01',
           'product':'sandalha',
           'price':75,
           'quantity':2}        
        ]
    df_example = pd.DataFrame(data)
    df_example.to_csv(csv_path,index= False)
    print('Criado com sucesso.',csv_path)

df= pd.read_csv(csv_path,parse_dates=['date'])

required= {'date','product','price','quantity'}
if not required.issubset(set(df.columns)):
    print('As colunas estão erradas!')

df['total']=df['price']*df['quantity']
df[['total']].to_csv('total.csv',index=False)
print('foi criado')