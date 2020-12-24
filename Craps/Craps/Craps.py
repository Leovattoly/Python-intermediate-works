import random

def testCraps(n):
    
    win = 0
    fail = 0
    for i in range(n):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        total_dice = dice_1 + dice_2
        if(total_dice == 7 or total_dice == 11):
            win = win+1
        elif(total_dice == 2 or total_dice == 3 or total_dice == 12):
            fail = fail +1
        else:
            continue
    return(win/n)


    

print(testCraps(100))
