from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

import pandas as pd
from pathlib import Path
shoe_df = pd.read_csv(Path('data/meta-data.csv'))
shoe_filt = shoe_df['SubCategory'] == 'Sneakers and Athletic Shoes'
df = shoe_df.loc[shoe_filt]
df['SubCategory'].unique()

#create a list of urls to scrape by using the id in the CID collumn and splitting the CID in two parts before the - is the product
#and after the - is the color. Then put together a url using https://www.zappos.com/product/ + product + /color/ + color

cid_df = df['CID'].str.split('-',expand=True)
cid_df.columns = ['product','color']

cid_df['url'] = 'https://www.zappos.com/product/' + cid_df['product'] + '/color/' + cid_df['color']

#loop through the urls and get the shoe name, color, and price and put it in a dataframe
shoe_brand = []
shoe_names = []
shoe_colors = []
shoe_prices = []

for url in cid_df['url']:
    print(url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    
    
    soup = BeautifulSoup(webpage, "html.parser")
        
    
    brandinfo = soup.find(class_='Cq-z')
    shoeinfo = soup.find(class_='Dq-z')
    colorinfo = soup.find(class_='U4-z')
    price = soup.find('span',class_="Hr-z")
    
    try:
        shoe_brand.append(brandinfo.text.strip())
    except:
        shoe_brand.append('NaN')
    
    try:
        shoe_names.append(shoeinfo.text)
    except:
        shoe_names.append('NaN')
    
    try: 
        shoe_colors.append(colorinfo.text)
    except:
        shoe_colors.append('NaN')
    
    try:
        shoe_prices.append(price.get('content'))
    except:
        shoe_prices.append('NaN')
        

    
df['brand'] = shoe_brand
df['name'] = shoe_names
df['color'] = shoe_colors
df['price'] = shoe_prices
df['url'] = cid_df['url']

df.to_csv(Path('data/completeshoe.csv'))
