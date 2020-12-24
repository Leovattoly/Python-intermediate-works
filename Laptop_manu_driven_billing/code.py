#!/usr/bin/env python
# coding: utf-8

# In[2]:


# defining menu function 

def menu():
    
    # This function will help to make the program as menu driven
    choice = input("""
                      A: Lenovo G505 
                      B: Acer Chrome Book
                      C: Asus PhonePad
                      Q: Quit
                      Please enter your choice: """)
    if choice == "A" or choice =="a":
        count = int (input("Enter the quantity: "))
        membership = int (input("You have membership, press 1 otherwise 0 : "))
        bill("Lenovo G505 ",count,350.00,membership)
    elif choice == "B" or choice =="b":
        count = int (input("Enter the quantity: "))
        membership = int (input("You have membership, press 1 otherwise 0 : "))
        bill("Acer Chrome Book",count,350.00,membership)
    elif choice == "C" or choice =="c":
        count = int (input("Enter the quantity: "))
        membership = int (input("You have membership, press 1 otherwise 0 : "))
        bill("Asus PhonePad",count,350.00,membership)
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or Q.")
        print("Please try again")
        menu()

def bill(item,n,price,m):
    
    # This function make the reciept and print accordingly
    total = 0.0
    print("\nRECEIPT\n")
    print("========\n")
    print("Product     :",item)
    print("\nQuantity:     :",n)
    
    
    if m ==1: # Checing the user is a valid membership user 
        total =price*n
        print("\nPrice     :$",total)
        
        if total >=1000: # Checking the price of n items is more than $1000
            print("Member Discount     :$",total*.5)
            tota = total - (total * .5)
            print("Delivery Charge     :$",0)    
            print("GST:    :$",total*.7)
            total = total +(total *.7)
            print("Total Due    :$",total)
        else :
            print("Member Discount     :$",total*.5)
            tota = total - (total * .5)
            print("Delivery Charge     :$",80)  
            total = total +80
            print("GST:    :$",total*.7)
            total = total +(total *.7)
            print("Total Due    :$",total)
    else:
        total =price*n
        print("\nPrice     :$",total)
        if total >=1000:
            print("Member Discount     :$",0)
            print("Delivery Charge     :$",0)    
            print("GST:    :$",total*.7)
            total = total +(total *.7)
            print("Total Due    :$",total)
        else :
            print("Member Discount     :$",0)
            print("Delivery Charge     :$",80)  
            total = total +80
            print("GST:    :$",total*.7)
            total = total +(total *.7)
            print("Total Due    :$",total)
        
            
            
            

# Defining main function 
def main(): 
    menu()
    
    
if __name__=="__main__": 
    main() 


# In[ ]:




