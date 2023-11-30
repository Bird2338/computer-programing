# defining stuff
other = True
import math
import random
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
        
        
        
# Select person gives terain imputs
month_input = input('What Month Num Is It? ')
mountan_input = input('In Mountans? y/n ').lower()
desert_input = input('In Desert? y/n ').lower()
high_temp = input('High temp? ')
low_temp = input('low temp? ')



# Checking if terain imputs are numrals or alphabet

# Checking if month_input is valid
if (month_input.isnumeric() == True) and (int(month_input) <= 12) and (int(month_input) >= 1):
    month_input_check = True
else:
    month_input_check = False
    
# Checking if mountan_input is valid
if (mountan_input.isalpha() == True) and (mountan_input == 'y' or mountan_input == 'n'):
    mountan_input_check = True
else:
    mountan_input_check = False
    
# Checking if desert_input is valid
if (desert_input.isalpha() == True) and (desert_input == 'y' or desert_input == 'n'):
    desert_input_check = True
else:
    desert_input_check = False

# Checking if high_temp is valid
if is_integer(high_temp) == True:
    high_temp_check = True
else:
    high_temp_check = False
        
# Checking if low_temp is valid
if is_integer(low_temp) == True:
    low_temp_check = True
else:
    low_temp_check = False
    
    
# Inputs are commputed into the final temp

latitude_input = -31
for t in range(61):
    longitude_input = -51
    lat = latitude_input
    latitude_input = lat + 1
    for i in range(101):
        longi = longitude_input
        longitude_input = longi + 1
        if (month_input_check == True) and (mountan_input_check == True) and (desert_input_check == True) and (high_temp_check == True) and (low_temp_check == True):
            x = 1
            
            
            # calculate Temp depending on the month
            if int(month_input) == 1:
                month_temp = -20 + random.randrange(-5,5)
            elif int(month_input) == 2:
                month_temp = -10 + random.randrange(-5,5)
            elif int(month_input) == 3:
                month_temp = 5 + random.randrange(-5,5)
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
                month_temp = 5 + random.randrange(-5,5)
            elif int(month_input) == 11:
                month_temp = -10 + random.randrange(-5,5)
            elif int(month_input) == 12:
                month_temp = -20 + random.randrange(-5,5)
                
                
            # calculate distence from coldest spot
            # coldest cordnents
            cold_x = -25
            cold_y = 15
            cold_distence = int((round(math.sqrt(pow(((cold_x) - int(longitude_input)), 2) + pow((cold_y - int(latitude_input)),2)))))
            
            # convesition to tempature
            cold_tempature = (cold_distence)
            
            
            # calculate distence from hottest spot and converts to tempature
            # hottest cordnents
            hot_x = 25
            hot_y = -15
            hot_distence = int((round(math.sqrt(pow(((hot_x) - int(longitude_input)), 2) + pow(((hot_y) - int(latitude_input)),2)))))
            
            # convesition to tempature
            hot_tempature = (0 - hot_distence)
            
            
            # Temperature global average
            temperature_global_average = 52
    
            # Tempature calculation
            tempature = temperature_global_average + hot_tempature + cold_tempature + month_temp

            if other == True:
                if (tempature >= int(low_temp)) and (tempature <= int(high_temp)):
                    file = open('temp_graph.txt', 'a')
                    file.write(f'({int(longitude_input)},{int(latitude_input)}),')
                    file.close()
                    other = False
            else:
                other = True
# Prints the temp
if x == 0:
    print('ERROR')
else:
    print(tempature)
