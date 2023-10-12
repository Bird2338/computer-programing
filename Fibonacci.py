x = int(input('How deep into the fibonacci do you want to go?'))
y = 0
total = 1
last_total = 0
for x in range(1, (x + 1)):
    y = total
    total = total + last_total
    last_total = y
    print(total)