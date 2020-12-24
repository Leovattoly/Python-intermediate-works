#!/usr/bin/env python
# coding: utf-8

# In[6]:



# import required modules 
import requests, json 


# base_url variable to store url 
base_url = "https://api.blockcypher.com/v1/eth/main/addrs/"

# Give wallet address 
wallet_address = input("Enter the wallet address of ETH: ") 

# complete url address 
complete_url = base_url + wallet_address +"/balance" 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 

final_balance = x["balance"] 
    
	# print following values 
print("Final Balance of ETH : ",str(final_balance)) 


base_url_btc = "https://api.blockcypher.com/v1/btc/main/addrs/"

# Give wallet address 
wallet_address = input("Enter the wallet address of BTC: ") 

# complete url address 
complete_url = base_url_btc + wallet_address +"/balance" 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 
final_balance = x["balance"] 
    
	# print following values 
print("Final Balance of BTC : ",str(final_balance)) 



# In[ ]:




