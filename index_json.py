import pandas as pd

from cryptoindex.mongo_setup import query_mongo


db = 'index'
cll = 'index_level_1000'

df = query_mongo(db, cll)

df['Time'] = [int(x) for x in df['Time']]

df = df.rename(columns={'Time': 'time', 'Index Value': 'value'})

df = df.loc[df['time'] > 1467331200]
print(df)

df = str(df.to_dict(orient="records"))



value = 'json = '

final = value + df

print(final)

with open('result.json', 'w') as f:
    f.write(final)
