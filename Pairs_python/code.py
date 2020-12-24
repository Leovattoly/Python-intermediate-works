def solution(A):
    k = 0
    # dictionary for storing count each element
    value_dict = dict()
    # looping throug the given A
    for i in range(len(A)):
        a= 0
        for j in range(len(A)):
            # finding the identical pairs
            if(A[i] == A[j] and i != j):
                a = a+1
                
        value_dict [A[i]] = a*2
    # splitting the dictionary
    values = [] 
    items = value_dict.items() 
    for item in items: 
        values.append(item[1]) 
    # sorting the calues in ascending order
    values.sort()
    # returning the last element
    return (values[-1])
print(solution([3,5,6,3,3,5]))
                
                