import sys 
F1= sys.argv[1] 
F2= sys.argv[2]

lines1 = []

lines2 = []


with open(F1) as fh:
    lines1 = fh.readlines()

with open(F2) as fh:
    lines2 = fh.readlines()
    
accounts ={}

account_List = []


for line in lines1[0:]:
    (account, pin, balance) = line.split("|")
    accounts[account] = [pin, int(balance)]
    account_List.append(account)

for line in lines2[0:]:
    (command, amount, account, pin) = line.split("|")
    amount = int(amount)

for account in accounts:
    if command == "add" and int(accounts[account][0]) == int(pin):
        accounts[account][1] += amount
        
    elif command == "sub" and int(accounts[account][0]) == int(pin) and (accounts[account][1]>= amount):
        accounts[account][1] -= amount
    else:
        accounts[account][1] == amount

i = 0

commands = []

with open(F1, "w") as fw:
    fw.write("\n")

for account in account_List:
    pin = str(accounts[account][0])
    amount = str(accounts[account][1])
    val = str(account)+"|"+pin+"|"+amount+"\n"
    fw.write(val)
    i += 1

   #if i < len(accounts.keys()):
