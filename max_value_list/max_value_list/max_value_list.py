def get_input():
    n = int(input("Enter the total number of reading: "))
    temp_list = list()
    i=0
    if n >=1:
        for i in range(n):
            temp = int(input("Enter the temprature: "))
            temp_list.append(temp)      
        return temp_list
    else:
        return -300000

temperatures = list()
temperatures = get_input()
if temperatures != 300000:
    best_position = 0
    for i in range(len(temperatures)):
        if(temperatures[i] > temperatures[best_position]):
            best_position = i
    print(best_position," : 00")
else :
    print("invalid input")

        
    



