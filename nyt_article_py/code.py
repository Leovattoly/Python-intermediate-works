# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:09:46 2020

@author: DELL
"""

import matplotlib.pyplot as plt
import pandas as pd


# Check that the file can be opened and if not ask the user to try again (hint: use the try/except structure)
    
try:
    df = pd.read_csv("NYT_articles.csv") # inserting data 
except:
  print("Something went wrong ! . Please Try again.")

# Count and output how many articles are in the file
no_aarticle_and_attributes = df.shape
print(no_aarticle_and_attributes[0]," articles are in the file\n")

#5. Count and output how many categories are in the file, and how many articles are in each category
category = df.pivot_table(index = ['ArticleCategory'], aggfunc ='size') 
print("Number of articles in each category\n")
print(category) 

# Create a new csv file with your name (for example: "ndvir.csv")

# In the new file, create the following fields: PublishTime, ArticleTitle, ArticleAuthor, ArticleSubtitle, ArticleURL, ArticleKeywords, ArticleCategory

df.to_csv(path_or_buf= "ndvir.csv",index=False)


# In this part you will process the word frequency in the merged csv file you created. For all the word counts, use the data from the following three columns combined: ArticleTitle, ArticleSubtitle, ArticleKeywords.

# Note: when counting words, disregard capitalization (count lowercase and uppercase together)

from collections import Counter
results_ArticleTitle = Counter()
results_ArticleSubtitle = Counter()
results_ArticleKeywords = Counter()
df['ArticleTitle'].str.lower().str.split().apply(results_ArticleTitle.update)
print("Word count in Article Title:",len(results_ArticleTitle))
df['ArticleSubtitle'].str.lower().str.split().apply(results_ArticleSubtitle.update)
print("\nWord count in Article Subtitle:",len(results_ArticleSubtitle))

df['ArticleKeywords'].str.lower().str.split().apply(results_ArticleKeywords.update)

print("\nWord count in Article Keywords:",len(results_ArticleKeywords))