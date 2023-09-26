modulus = 10 % 3
print (f'10 % 3 = {modulus}')

multiplication = (6 * 6)
print (f'6 * 6 = {multiplication}')

float_division = (6 / 2)
print (f'6 / 2 = {float_division}')

addition = (5 + 7)
print (f'5 + 7 = {addition}')

subtraction = (9 - 4)
print (f'9 - 4 = {subtraction}')

less_than = (6 < 7)
print (f'6 < 7 = {less_than}')

greater_than = (3 > 8)
print (f'3 > 8 = {greater_than}')

equals_equals = (6 == 4)
print (f'6 == 4 = {equals_equals}')

greater_than_or_equals_to = (5 >= 5)
print (f'5 >= 5 = {greater_than_or_equals_to}')

less_than_or_equal_to = ( 9 <= 8)
print (f'9 <= 8 = {less_than_or_equal_to}')

X_equals = 5
print (f'X = {X_equals}')

not_equals_to = (6 != 3)
print (f'6 != 3 = {not_equals_to}')

and_and1 = 4
and_and2 = 6
if and_and1 == 4 and and_and2 == 6:
    print (f'{and_and1} and {and_and2} are equal to 4 and 6, yay!')
else:
    print (f'{and_and1} and {and_and2} are not equal to 4 and 6, me sad...')

or_or = 4
if or_or == 4 or or_or == 6:
    print('or_or is equals to 4 or 6, yay!')
else:
    print ('or_or is not equals to 4 or 6, me sad...')

not_num = 4
input_num = 4
if input_num is not not_num:
    print (f'{input_num} is not equal to {not_num}, yay!')
else:
    print(f'{input_num} is equal to {not_num}, me sad...')