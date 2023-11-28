def consonant_substring_value(string):
    new_string = string.lower()
    count = 0
    max_count = 0
    
    #Looping through each substring.
    for l in new_string:
        if l != "a" and l != "e" and l != "i" and l != "o" and l != "u":
            count += ord(l) - 96
            #Updating value of max_count
            if count > max_count:
                max_count = count
        else:
            count = 0

    return max_count      

#Example cases
print(consonant_substring_value("zodiac"))
print(consonant_substring_value("strength"))
print(consonant_substring_value("queue"))                

        
