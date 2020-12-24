
def g_c_d(a,b): 
    if (a>500 or b>500):
        return 0
    if(b==0): 
        return a 
    else: 
        return g_c_d(b,a%b) 

lst_a = list()
lst_b = list()
i = 0
while(i < 10):
    n = int(input("Enter Number: "))
    if(n>=0):
        if(i<5):
            lst_a.append(n)
            i = i+1
        else:
            lst_b.append(n)
            i = i+1
print(lst_a)
print(lst_b)
total_lst_a = 0
total_lst_b = 0
for ele in range(0, len(lst_a)): 
    total_lst_a= total_lst_a + lst_a[ele] 
for ele in range(0, len(lst_b)): 
    total_lst_b= total_lst_b + lst_b[ele] 

gcd_value = g_c_d(total_lst_a,total_lst_b)

if(gcd_value != 0):
    print(gcd_value)
else:
    print("Error occured")
        

    
            
    
    