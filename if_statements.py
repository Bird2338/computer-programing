salary = int(input('what is your salary? '))
years = int(input('How many years have you worked here? '))

if years >= 5:
    print (f'your bonus will be {salary * 0.05}.')
else:
    print('you do not qualify for a bonus.')