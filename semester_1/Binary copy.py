indices = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
out = [int(i in indices) for i in range(10)]
print(out)

check = True
for x in out:
    if x != True:
        check = False
    
if check == True:
    print('yay')