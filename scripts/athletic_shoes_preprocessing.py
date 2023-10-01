import tensorflow as tf
import numpy as np
import os
import pandas as pd

data_directory = './../shoedoku/data/'
image_size = (136,136)

image_df = pd.read_csv('./../shoedoku/data/meta-data.csv')

# loading shoe dataset from the csv file
shoeType_filt = image_df['SubCategory'] == 'Sneakers and Athletic Shoes'
# setting up a filter to get only the sneakers/athletic shoes
df = image_df.loc[shoeType_filt]
# filtering down our dataset


# creating a data generator
data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input,
)

# loading the dataset
dataset = data_generator.flow_from_directory(
    data_directory, target_size=image_size, batch_size=32, color_mode='rgb', classes=['test'], shuffle=True
    )
# the kw argument classes is there because our images are not divided into distinct classes
# rather, 

# loading pre-trained model
feature_extractor = tf.keras.applications.MobileNetV2(
    input_shape=(136,136,3), include_top=False, weights='imagenet', pooling='avg'
)

# now, for each sneaker/athletic shoe, we extract the image embeddings and we will use these to add them to our dataset
image_features_embeddings = feature_extractor.predict(dataset, verbose=1)

distance = np.dot(image_features_embeddings, image_features_embeddings.T)
# transposing the embedding matrix and computing the matrix product
norms = np.linalg.norm(image_features_embeddings, axis=1)
norms_matrix = np.outer(norms, norms)
distance /= norms_matrix
# normalizing the distance matrix


np.savetxt('similarity_matrix.csv', distance, delimiter=',')



