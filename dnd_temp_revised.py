# defining stuff
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
latitude_input = input('What Is The Latitude? ')
longitude_input = input('What Is The Longitude? ')



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

# Checking if latitude_input is valid

if (is_integer(latitude_input) == True) and (int(latitude_input) <= 30) and (int(latitude_input) >= -30):
    latitude_input_check = True
else:
    latitude_input_check = False
    
# Checking if longitude_input is valid
if (is_integer(longitude_input) == True) and (int(longitude_input) <= 50) and (int(longitude_input) >= -50):
    longitude_input_check = True
else:
    longitude_input_check = False
    
    
    
# Inputs are commputed into the final temp

if (month_input_check == True) and (mountan_input_check == True) and (desert_input_check == True) and (latitude_input_check == True) and (longitude_input_check == True):
    x = 1
    # calculate Temp depending on the month
    if int(month_input) == 1:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 2:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 3:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 4:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 5:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 6:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 7:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 8:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 9:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 10:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 11:
        month_temp = 0 + random.randrange(-5,5)
    elif int(month_input) == 12:
        month_temp = 0 + random.randrange(-5,5)
    # calculate temp depending on distence from corner
    lon_lat_temp = int(round(math.sqrt(pow(((-25) - int(longitude)), 2) + pow(((-15) - (latitude)),2)))
    print(lon_lat_temp)
else:
    print('ERROR')
    

# Prints the temp
if x == 0:
    print('ERROR')
else:
    print(temp)









