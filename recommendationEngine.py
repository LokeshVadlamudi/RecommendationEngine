#recommendation engine
#item similarity based recommendation

#importing libs
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

df = pd.read_csv('books.csv', sep='\s*,\s*',error_bad_lines=False)

#print(df.columns)
#print(df.columns.tolist())
#Index(['bookID,title,authors,average_rating,isbn,isbn13,language_code,# num_pages,ratings_count,text_reviews_count'], dtype='object')

#for the shape of the dataset
#print(df.shape)
#size -- (13719, 8)

#dropping unnamed columns
df=df.loc[:,~df.columns.str.contains('^Unnamed')]

#dropping isbn and isbn13 columns
df.drop(['isbn','isbn13'],axis=1,inplace=True)
#print(df.columns)

#display all the datatypes
#print(df.dtypes)


#will help to show all the text strings in the column.
pd.set_option('display.max_colwidth',-1)



#simple popularity based recommendation
top10 = df.sort_values('average_rating',ascending = False).head(5)


 







