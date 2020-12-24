import random

list_of_words = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango'] # list of words for testing

def finding_letter(str,c): # Defined for finding the positions of characters in string
    i=0
    li = list()
    for i in range(len(str)):
        if (str[i] == c):
            li.append(i)
    if(len(li) != 0):
        return (li)
    else:
        return -1

str = random.choice(list_of_words) #selecting words randomly
string = " "*(len(str)-1)
count_ans = 0
chk_str = list(string.split(" ")) 
i = 4
while(i !=0):

    if(count_ans != len(str)):
        print("Guess a letter (",i," gusses are remining:)")
        c = input("")
        d = (finding_letter(str,c))
        if(d != -1):
            for pos in d:
                chk_str[pos] = str[pos]
                count_ans = count_ans+1
            
            print("The answer so far is" ,chk_str)
           
        else:
            i=i-1
    else :
        break
if count_ans == len(str):
    print ("Good job ! You found the word ",str," !")
else:
    print("Not quite, the correct word was ",str,". Better luck next time.")
        
  