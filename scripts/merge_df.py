import pandas as pd

df1 = pd.read_csv('./../data/completeshoe.csv')
df2 = pd.read_csv('./../data/sneakers_similarity_df.csv')

df2['Brand'] = df1['brand']
df2['Name'] = df1['name']
df2['Color'] = df1['color']
df2['Price'] = df1['price']

df2.to_csv(path_or_buf='sneaker_data_updated_complete.csv')