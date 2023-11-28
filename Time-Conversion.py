def convert(hour, minute, period):
    #If statement that checks for correct inputs
    if hour > 12 or hour == 0 or minute > 59 or (period != "am" and period != "AM" and period != "pm" and period != "PM"):
        print("Incorrect inputs.")
        print("Use am/AM or pm/PM.")
        print("Hour cannot be 0 or exceed 12.")
        print("Minute should not exceed 59")
    
    #Converting hour to 0 whenever it's 12 in AM 
    if hour == 12 and (period == "am" or period == "AM"):
        hour = 0 
    #Adding 12 to digits whenever hour is not 12 in PM      
    elif hour != 12 and (period == "pm" or period == "PM"):
        hour += 12
    
    #Formatting the time to have 4 digits
    hour_string = str(hour).zfill(2)
    minute_string = str(minute).zfill(2)

    return(hour_string + minute_string)

#Example cases    
print(convert(11, 29, "am"))
print(convert(1,15,"pm"))
print(convert(12, 25, "pm")) 
print((convert(12, 1, "am")))

#Incorrect inputs case
print(convert(13,78,"pM"))  
        
