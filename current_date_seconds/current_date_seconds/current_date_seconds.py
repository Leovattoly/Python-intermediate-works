import datetime

def currentDate(x):
    hrs = x*24
    min = hrs * 60
    seconds = min * 60
    return seconds

print ("The total number of seconds is ", currentDate(4)) #expected outcome: The total number of seconds is 345600.0.
print ("The total number of seconds is ",currentDate(7)) #expected outcome: The total number of seconds is 604800.0.
