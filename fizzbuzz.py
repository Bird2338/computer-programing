# How long is the FizzBuzz
Pinput = input('How fizzy do yo want your buzz')
x = 1

# FailSafe checkpoint
if Pinput.isnumeric():
    Pinput = (int(Pinput))
else:
    print(f'ERROR|Pinput.isnimeric|{Pinput.isnumeric()}')
    exit()

# FizzBuzz check and print
for i in range(1, (Pinput + 1)):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)