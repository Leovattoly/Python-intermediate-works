def counting_dozens(number_of_cookies):
    return(int(number_of_cookies//12))   #returnng the number of dozens 

number_of_cookies = int(input("How many cookies?")) 
print("Number of Dozens: ",counting_dozens(number_of_cookies)) #printing the dozen number

