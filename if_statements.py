salary = int(input('what is your salary? '))
years = int(input('How many years have you worked here? '))

if years >= 5:
    print (f'your bonus will be {salary * 0.05}.')
else:
    print('you do not qualify for a bonus.')


y = int(input('How tall is your rectangle? '))
x = int(input('How wide is your rectangle? '))

if y == x:
    print('This is a square.')
else:
    print('This is not a square.')


Int_1 = int(input('What is your first number? '))
Int_2 = int(input('What is your second number? '))

if Int_1 > Int_2:
    print(f'{Int_1} is greater than {Int_2}')
else:
    if Int_1 < Int_2:
        print(f'{Int_1} is less than {Int_2}')
    else:
        if Int_1 == Int_2:
            print(f'{Int_1} is the same as {Int_2}')





P_1 = int(input('How old is person one? '))
P_2 = int(input('How old is person two? '))
P_3 = int(input('How old is person three? '))

if P_1 > P_2 and P_1 > P_3 and P_3 < P_2 and P_3 < P_1:
    print(f'Person one(age {P_1}) is the oldest and person three(age {P_3}) is the youngest')
else:
    if P_1 > P_2 and P_1 > P_3 and P_2 < P_1 and P_2 < P_3:
        print(f'Person one(age {P_1}) is the oldest and person two(age {P_2}) is the youngest')
    else:
        if P_3 > P_1 and P_3 > P_2 and P_1 < P_2 and P_1 < P_3:
            print(f'Person three(age {P_3}) is the oldest and person one(age {P_1}) is the youngest')
        else:
            if P_3 > P_1 and P_3 > P_2 and P_2 < P_1 and P_2 < P_3:
                print(f'Person three(age {P_3}) is the oldest and person two(age {P_2}) is the youngest')
            else:
                if P_2 > P_1 and P_2 > P_3 and P_1 < P_2 and P_1 < P_3:
                    print(f'Person two(age {P_2}) is the oldest and person one(age {P_1}) is the youngest')
                else:
                    if P_2 > P_1 and P_2 > P_3 and P_3 < P_1 and P_3 < P_2:
                        print(f'Person two(age {P_2}) is the oldest and person three(age {P_3}) is the youngest')
                    else:
                        print('Error')


c_h = int(input('how many classes have been held? '))
c_a = int(input('how many classes have you atended? '))
c_a_p = ((c_a / c_h) * 100)

if ((c_a / c_h) * 100) >= 75:
    print(f'{c_a_p}% He can attend, yay!')
else:
    print(f'{c_a_p}% He cant attend, sad...')