#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import required modules 
import requests, json 

# base_url variable to store url 
base_url_1 = "https://api.themoviedb.org/3/person/"

API_KEY = # Please create a API Key from the site

base_url_2= "/movie_credits?api_key="+API_KEY+"&language=en-US"

# Give Personal ID
person_id = input("Enter Personal ID: ") 

vote_avg_threshold = input("Enter Vote average: ") 

# complete url address 
complete_url = base_url_1+person_id+base_url_2

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 

data = dict()

if vote_avg_threshold >= x["vote_average"]:
    data = {"id":x["credit_id"],"title" : x["title"],"vote_avg":x["vote_average"]}
else:
    print("Vote average is less than",vote_avg_threshold," for the given id ",person_id)
    



# In[ ]:




