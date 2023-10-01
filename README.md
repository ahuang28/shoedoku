# shoedoku

![](./iPhone 14 - 5)
![](./iPhone 14 - 6)

## Inspiration
First of all we, love shoes so much we don't wear shoes and keep them displayed. That said, searching over the net for shoes isn't the most fun thing to do, it takes a while and you might not even find the pair for you. So why not make an app that works like tinder, simple to use and matches pretty well. 


## What it does
It's a tinder, but for shoes. It displays an image with a short description of the shoe, then allows the user to either swipe right in order to approve/like the shoe or swipe left otherwise. Based on the swipes we then recommend other shoes that the user might like based on the likes and dislike.

## How we built it
First we found a good [dataset](https://www.kaggle.com/datasets/aryashah2k/large-shoe-dataset-ut-zappos50k/data) on Kaggle, the one we settled with had 12000+ sneakers, shoes with images and a few information about the shoes.

We then leverage tools such as **pandas** and **TensorFlow** to create a similarity matrix based of the images for all 12000+ shoes. What the similarity matrix represents is how "close" shoes are to each other within the embedding space, which is essentially a very high dimensional space that projects shoes to a set of coordinates, based on the features extracted from the images by the AI. To give a better heuristic to the shoes we are going to recommend we ended up using many features from the dataset file _meta-data.csv_ such as heel_height, toestyle...

The web app was built with django and figma.


## Challenges we ran into
There was missing many relevant information in the dataset such as the brand name, name, color and price. Thus we had to web scrape that data from the original site [zappos](https://www.zappos.com/). To scrape we used a python script used beautiful soup to select the data we needed. 

Another difficulty was taking the similarity matrix and then translating the similarity into CID's which could be used to identify the shoes. The reason for this difficulty was due to the fact that we had trimmed the original dataset down to only sneakers, but they carried on their indices from the original dataset. so our similarity matrix compared different rows within our sneaker dataset with each other, but figuring out which indices within the original dataset these corresponded to was a bit of a challenge.

Yet another difficulty we encountered was that the csv dataset and the images folder downloaded from Kaggle were not consistent, i.e. there were images in the images folder that were not included in our csv dataset. After much frustration and debugging, we eventually noticed the error and fixed it by copying all the files in the csv dataset to a separate directory and running diff to see which files were inconsistent.

Our last major difficulty was underestimating the amount of time it would take to complete everything with it executing as desired. This was under the assumption that the 'minor' stuff such as performing the computation of the similarity matrix, and finding similar sneakers for all the sneakers in the dataset, would be less error-prone and time-consuming than they actually turned out to be. In actuality the AI-related part of our project took the least amount of time compared to the webdev side.


## Accomplishments that we're proud of
One of the things about our project that we are proud of is how we dealt with the issues we encountered. Although they were very frustrating, eventually we got through them, learning valuable things both technically and mentally along the way. 


## What we learned
Throughout this project we learned a variety of things, including:
- Perform some preliminary checks on the data before you begin working with it, to save yourself the time and stress of trying to figure out what is wrong with your project. This can include things such as making sure your dataset and your images folder are consistent, for example.
- Have a realistic vision of what is possible in the alotted timeframe. Although it is good to aim high and to have some degree of ambition when taking on these types of projects, it is important to stop and consider whether an idea you are considering is feasible in the alotted timeframe, and to also allow extra time for bugs/errors.
- Utilize Divide & Conquer. Utilizing each team member's strengths to divide up the work and spend time efficiently is a great strategy, and once members are done with their respective parts they can reconvene together and tackle the remaining portions as a group.


## What's next for Solemate
Potential next steps might include expanding the app to house another subcategory of shoe, like heels, for example. Another possibility would be to have a dynamically changing "You might like" tab that displays a similar shoe every few seconds to catch the user's interest.
