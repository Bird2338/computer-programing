x = 𝚿


month_input = input('what month num is it? ')
mountan_input = input('in mountans? y/n ').lower()
latitude = input('what is the latitude? ')
longitude = input('what is the longitude? ')

month_input_check = month_input.isnumeric()
mountan_input_check = mountan_input.isalpha()
latitude_check = latitude.isnumeric()
longitude_check = longitude.isnumeric()

x = 0
if (month_input_check == True) and (mountan_input_check == True) and (latitude_check == True) and (longitude_check == True):
    if latitude or longitude <= 50:
        if latitude or longitude >= -50:
            if month_input <= 12:
                if month_input >= 1:
                    if mountan_input == 'y' or mountan_input == 'n':
                        x = 1
if x == 0:
    print('ERROR')
else:
    print('temp')