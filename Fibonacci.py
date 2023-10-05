y = 0
total = 1
last_total = 0
for x in range(1, 10):
    y = total
    total = total + last_total
    last_total = y
    print(total)
