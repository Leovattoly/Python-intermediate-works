import pandas as pd


import seaborn as sns


import numpy as np


import scipy.stats as st


import matplotlib.pyplot as plt


#




#import the data


df = pd.read_csv('lahman-teams.csv')




#made a simple graph

np_hist = np.random.normal(loc=0, scale=1, size=1000)


bb_df = df.loc[df.yearID >= 1995].copy()

d =pd.DataFrame(bb_df['SB'],bb_df['W'],bb_df['ERA'])
d.plot.hist(bins=12, alpha=0.5)
#plt.hist(x=d, bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)

# function to show the plot 
plt.show() 

#df[['W', 'SB', 'ERA']].hist(bins=90)