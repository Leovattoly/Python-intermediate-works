Dear Student,


Please find the below attached code,


# checking a number is palindrome
# using math.log() + recursion + list comprehension
import math

# the recursive function to reverse
def rev(num):
    return int(num != 0) and ((num % 10) *(10**int(math.log(num, 10))) +rev(num // 10))


k=0
palindrome_list = list()

# using math.log() + recursion + list comprehension
# for checking a number is palindrome

for i in range(1,100):
    res = i == rev(i)
    
    if res == True :
        
        # palindrome number adding to a list
        palindrome_list += [i]
        
k = 0
# printing the palindrome numbers in a row of ten
while(k <= len(palindrome_list)):
    print(palindrome_list[k:k+10])
    k = k+10
       

