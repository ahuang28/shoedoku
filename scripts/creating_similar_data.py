import pandas as pd
import numpy as np

# similarity_matrix = np.loadtxt('similarity_matrix.csv', delimiter=',')
image_df = pd.read_csv('meta-data.csv/meta-data.csv')
# reading in our dataset
shoeType_filt = image_df['SubCategory'] == 'Sneakers and Athletic Shoes'
# filtering down our dataset to include only sneakers/athletic shoes
df = image_df.loc[shoeType_filt]

df.reset_index(inplace=True)

# for each shoe_i, we will fetch the i_th row of the similarity matrix, sort it, and pick the 4 most similar
# each of these will have their own column inside the dataframe

# to get the proper CID for the most similar shoes, we use argsort to get the indices of the images
# that yield the highest match, and then use iloc on the dataframe (since the index represents the row of the similarity matrix)
# and then extract the CID that way

distance = np.loadtxt('similarity_matrix.csv', delimiter=',')
# loading in our similarity matrix

df['5'] = pd.Series(df.index).apply(
    lambda ind: df.iloc[(np.argsort(distance[int(ind)])[1]), 1]
)

df['4'] = pd.Series(df.index).apply(
    lambda ind: df.iloc[(np.argsort(distance[int(ind)])[3214]), 1]
)

df['3'] = pd.Series(df.index).apply(
    lambda ind: df.iloc[(np.argsort(distance[int(ind)])[6430]), 1]
)

df['2'] = pd.Series(df.index).apply(
    lambda ind: df.iloc[(np.argsort(distance[int(ind)])[9644]), 1]
)

df['1'] = pd.Series(df.index).apply(
    lambda ind: df.iloc[(np.argsort(distance[int(ind)])[12855]), 1]
)

print(df.head())

df.to_csv('sneakers_similarity_df.csv')