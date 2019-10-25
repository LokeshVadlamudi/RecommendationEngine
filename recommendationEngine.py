#recommendation engine
#item similarity based recommendation

#importing libs
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter('ignore')

df = pd.read_csv('books.csv', sep='\s*,\s*',error_bad_lines=False)

#print(df.columns)
#print(df.columns.tolist())
#Index(['bookID,title,authors,average_rating,isbn,isbn13,language_code,# num_pages,ratings_count,text_reviews_count'], dtype='object')

#for the shape of the dataset
#print(df.shape)

#dropping unnamed columns
df=df.loc[:,~df.columns.str.contains('^Unnamed')]

print(df.head())
