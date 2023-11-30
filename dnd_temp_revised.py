(desert_input_check == True) and (latitude_input_check == True) and (longitude_input_check == True):
    x = 1
    
    
    # calculate Temp depending on the month
    if int(month_input) == 1:
        month_temp = -20 + random.randrange(-5,5)
    elif int(month_input) == 2:
        month_temp = -10 + random.randrange(-5,5)
    elif int(month_input) == 3:
        month_temp = -0 + random.randrange(-5,5)
    elif int(month_input) == 4:
        month_temp = 10 + random.randrange(-5,5)
    elif int(month_input) == 5:
        month_temp = 15 + random.randrange(-5,5)
    elif int(month_input) == 6:
        month_temp = 20 + random.randrange(-5,5)
    elif int(month_input) == 7:
        month_temp = 20 + random.randrange(-5,5)
    elif int(month_input) == 8:
        month_temp = 15 + random.randrange(-5,5)
    elif int(month_input) == 9:
        month_temp = 10 + random.randrange(-5,5)
    elif int(month_input) == 10:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 11:
        month_temp = -10 + random.randrange(-5,5)
    elif int(month_input) == 12:
        month_temp = -20 + random.randrange(-5,5)
        
        
    # calculate distence from coldest spot
    # coldest cordnents
    cold_x = -25
    cold_y = 15
    cold_distence = int((round(math.sqrt(pow(((cold_x) - int(longitude_input)), 2) + pow((cold_y - int(latitude_input)),2)))))
    print(cold_distence)
    
    # calculate distence from hottest spot and converts to tempature
    # hottest cordnents
    hot_x = 25
    hot_y = -15
    hot_distence = int((round(math.sqrt(pow(((hot_x) - int(longitude_input)), 2) + pow(((hot_y) - int(latitude_input)),2)))))
    print(hot_distence)
    
    # base_hot_temperature is calculated
    base_hot_temperature =
    
    # Calculating temperature
    temperature = 0

else:
    print('ERROR')
    

# Prints the temp
if x == 0:
    print('ERROR')
else:
    print(temperature)
