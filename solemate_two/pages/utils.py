#Utitlies to run the app 
from pathlib import Path
import pandas as pd 
import random


def cid_to_path(cid : str):
    '''Converts a shoe id to the path to the image of the shoe'''
    id_color = cid.split("-")
    #join the id_color[0] and id_color[1] with a dot inbetween and add .jpg
    new_path = "images/" + id_color[0] + "." + id_color[1] + ".jpg"
    return str(new_path)

def path_to_cid(path : Path):
    '''Converts a path to the image of the shoe to the shoe id'''
    #split the path by the slashes
    path = str(path)
    print(path)
    path = path.split("/")
    #get the last element of the list
    path = path[-1]
    #split the path by the dots
    path = path.split(".")
    #get the first element of the list
    cid = path[0]
    color = path[1]
    return cid + "-" + color

def get_next_image(accept : bool, current_image : str):
    '''Gets the next image to be displayed in the app.
            Parameters: 
                accept (bool): whether the user accepted the last shoe
                current_image (str): the path of the last shoe
    ''' 
    shoe_id = path_to_cid(current_image)
    print(shoe_id)
    df = pd.read_csv(Path("pages/static/data/shoes_similarity.csv"))
    #get the row of the shoe
    shoe_row = df[df["CID"] == shoe_id]
    #get the next cid most similar to the shoe
    if accept:
        col = str(random.randint(1,3))
        new_shoe_id = shoe_row[col].iloc[0]
        # like_shoe = Sneaker(cid=path_to_cid(current_image))
        # like_shoe.save()
        
    else : 
        col = str(random.randint(4,5))
        new_shoe_id = shoe_row[col].iloc[0]
    
    return cid_to_path(new_shoe_id)