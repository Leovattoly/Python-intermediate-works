#!/usr/bin/env python
# coding: utf-8

# In[27]:


def time():
    time = str(input("Enter time [hh:mm:ss]:"))
    
    if(len(time) >8 ):
        print("Invalid time ")
        return
    
    hh= time[0]+time[1]
    hh= int(hh)
    if( (hh >= 0 and hh <= 23) == False):
        print("Hour must be a 2-digit number.")
        return
    if(time[2] != ":" or time[5] != ":"):
        print("Must separate hour, minute and second with colons.")
        return
    
    mm= time[3]+time[4]
    mm= int(mm)
    if( (mm >= 0 and mm <= 59) == False):
        print("Minute must be a 2-digit number.")
        return
    
    ss= time[6]+time[7]
    ss= int(ss)
    if( (ss >= 0 and ss <= 59) == False):
        print("Second must be a 2-digit number.")
        return
    time_ = time[0]+time[1]+time[3]+time[4]+time[6]+time[7]
    print(time_)
    
    
    
    
        
    
time()


# In[31]:


def string_prac ():
    
    s = str(input("Enter the string: "))
    s = s.upper()
    all_freq = {} 
  
    for i in s: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
     #printing result  
    print ("Count of all characters in",s, "is :\n "+  str(all_freq)) 
string_prac()


# In[ ]:


def water_usage():
    
    f= open("water.txt","w")

    for i in range(2):
        acc = str(input("Enter account number: "))
        r_b = str(input("Enter R for residential, B for business: "))
        galoon = str(input("Enter number of gallons used: "))
    
        content = str(acc+" "+r_b+" "+galoon)
        f.writelines(content)
        f.writelines("\n")
    f.close()
water_usage()


# In[ ]:


f= open("water.txt","r")
print(f.read()) 


# In[ ]:


def water_bill():
    
    f= open("water.txt","r")

    for i in range(2):   
        content = f.readline()
        acc = int (content[0:4])
        r_b = str(content[5])
        galoon = int (content[7:11])
        
        if r_b == "R":
            if galoon > 6000:
                amount = 6000*0.05 + (galoon - 6000) *0.07
            else:
                amount = galoon * 0.05
        else:
            if galoon > 8000:
                amount = 8000*0.06 + (galoon - 6000) *0.08
            else:
                amount = galoon * 0.06
        print ("Customer ",i+1, " bill amount: ",amount)
            
    f.close()
water_bill()


# In[ ]:




