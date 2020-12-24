import re

def string_manipulation(str):
    x = re.sub("\s", "", str) # Removing Space
    x = re.sub("\W","",x)    #Removing punctuation
    x = x.lower()            #converting to upper case 
    i=0
    li = list()             #initializing a list
    while(i <= len(x)):
        li_item = x[i:i+3]
        if(li_item[0] =='a' or li_item[0] == 'A'): #Checking the starting character 'a' or 'A'
            i = i+3
        else:
            li.append(x[i:i+3])                 #adding in the list
            i = i+3            
    print(li)
        
        
    
string_manipulation("Ab..DEF")