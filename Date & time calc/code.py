DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
def daylight_saving(daytime):
    
    if(daytime[1] > 23 or daytime[2] > 59  ):
        return ("Error")
    if(daytime[1] == 23):
        
        # Finding the day
        i = DAYS.index(daytime[0])
        # increasing the day by one
        i = i+1
        if (i>6):
            i = 0
        new_day = DAYS[i]
        
        # creating new tuple with updated data
        updated_daytime =(new_day ,00,daytime[2])
        
    else:
        # creating new tuple with updated data
        updated_daytime =( daytime[0],daytime[1]+1,daytime[2])
        
    # Returning updated tuple
    return updated_daytime

# DO NOT MODIFY BELOW HERE

print(daylight_saving(('Mon', 11, 30)))

print(daylight_saving(('Wed', 16, 0)))

print(daylight_saving(('Tue', 23, 55)))

print(daylight_saving(('Sat', 23, 10)))