import ccxt

address = input("Enter the adress: ")
bittrex = ccxt.bittrex({
    'apiKey': '...', # Create an account in https://global.bittrex.com/ to get an API key
    'secret': address, # Feild name
})

# fetch your account balances for each asset
account_balance = bittrex.fetch_balance()# execute the order


print("Availble Balance: ",account_balance)
