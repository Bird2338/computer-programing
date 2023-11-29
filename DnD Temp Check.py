import random
month_input = int(input('what month num is it? '))
mountan_input = input('in mountans? y/n ').lower()
latitude = int(input('what is the latitude? '))
longitude = int(input('what is the longitude? '))

mountan_input_check = mountan_input.isalpha()
x = 0
other = 1


if (mountan_input_check == True):
    if latitude or longitude <= 50:
        if latitude or longitude >= -50:
            if month_input <= 12:
                if month_input >= 1:
                    if mountan_input == 'y' or mountan_input == 'n':
                        x = 1
                        if latitude < 0 and longitude > 0:
                            mound = random.randrange(-80,-40)
                        else:
                            mound = random.randrange(-10,-0)
                        if month_input == 1:
                            month_temp = -20 + random.randrange(-5,5)
                        elif month_input == 2:
                            month_temp = -10 + random.randrange(-5,5)
                        elif month_input == 3:
                            month_temp = 0 + random.randrange(-5,5)
                        elif month_input == 4:
                            month_temp = 0 + random.randrange(-5,5)
                        elif month_input == 5:
                            month_temp = 10 + random.randrange(-5,5)
                        elif month_input == 6:
                            month_temp = 20 + random.randrange(-5,5)
                        elif month_input == 7:
                            month_temp = 20 + random.randrange(-5,5)
                        elif month_input == 8:
                            month_temp = 10 + random.randrange(-5,5)
                        elif month_input == 9:
                            month_temp = 0 + random.randrange(-5,5)
                        elif month_input == 10:
                            month_temp = 0 + random.randrange(-5,5)
                        elif month_input == 11:
                            month_temp = -10 + random.randrange(-5,5)
                        elif month_input == 12:
                            month_temp = -20 + random.randrange(-5,5)
                        if mountan_input == 'n':
                            temp = 50 - int(latitude * 2) + int(longitude / 2) + month_temp
                        elif mountan_input == 'y':
                            temp = 50 - int(latitude * 2) + int(longitude / 2) + month_temp + mound
if x == 0:
    print('ERROR')
else:
    print(temp)
