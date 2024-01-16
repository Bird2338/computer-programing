print('For loop to iterate through the letters in a word:')
word = 'cheese'
for item in word:
    print(item)


print('For loop using the range() function:')
for nums_1 in range(1, 10):
    print(nums_1)


print('For loop to iterate through a list:')
Cheese_List = ['Bree', 'Parm', 'Goat', 'Blue']
print('Cheese types:')
for Cheese in Cheese_List:
    print(Cheese)
    
    
print('Using an else statement inside a for loop:')
flowers = ['Jasmine','Lotus','Rose','Sunflower']
for Fl in flowers:
    if Fl == 'Rose':
         break
    else:
         print(Fl)


print('Nested for loops (one loop inside another loop):')
list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
for nums_2 in list1:
    for veggies in list2:
        print(f'{nums_2} {veggies}')
        
        
print('Using break statement inside a for loop:')
colors = ['blue','red','green','yellow']
for co in colors:
    if co == 'green':
         break
    else:
         print(co)


print('Using continue statement inside a for loop:')
vehicles = ['Car','Cycle','Bus','Tempo']
for ve in vehicles:
    if ve == 'Bus':
         continue
    else:
         print(ve)
         

print('For loop to count the number of elements in a list:')
Numbers = [12,3,56,67,89,90]
count = 0
for nums_4 in Numbers:
    count = count + 1
print(count)


print('For loop to find the sum of all numbers in a list:')
Numbers = [12,3,56,67,89,90]
Sum = 0
for nums_3 in Numbers:
    Sum = (Sum + nums_3)
    print(Sum)
    
    
print('For loop to find the multiples of 5 in a list:')
numbers = [2,5,6,10,15,20,25]
for nums_5 in numbers:
    nums_7 = 0
    for nums_6 in range(1, 100):
        nums_7 = nums_7 + 5
        if nums_5 == nums_7:
            t_f = 'true'
            break
        else:
            t_f = 'false'
    print(f'{nums_5} is {t_f}')
    

print('For loop to copy elements from one list to another:')
list1 = ['Mango','Banana','Orange']
list2 = list1
for l2 in list2:
    print(l2)
    

print('For loop to find the maximum element in a list:')
numbers = [1,4,50,80,12]
Max = 0
for nums_8 in numbers:
    if nums_8 > Max:
        Max = nums_8
    else:
        continue
print(f'the bigest number is {Max}')


print('or loop to find the minimum element in a list:')
numbers = [1,4,50,80,12]
Min = 1000
for nums_9 in numbers:
    if nums_9 < Min:
        Min = nums_9
    else:
        continue
print(f'the smallest number is {Min}')


print('For loop to sort the numbers in a list in ascending order (least to greatest):')
# try any amount of numbers!!!
cnt = 0
numbers = [1,4,50,80,12,5,17,82,3,6,90,12,56,78,45,23,45,67,454,34]
for nums_12 in numbers:
    cnt = cnt + 1
cnt = cnt -1
x = 0
y = 0
for z in range(1, 10000000000000000000000000):
    if numbers[x] > numbers[x + 1]:
        y = numbers[x]
        numbers[x] = numbers[x + 1]
        numbers[x + 1] = y
        x = 0
    else:
        x = x + 1
    if x == cnt:
        break
print(numbers)


print('For loop to sort the numbers in a list in descending order (greatest to least):')
# try any amount of numbers!!!
cnt = 0
numbers = [1,4,50,80,12,5,17,82,3,6,90,12,56,78,45,23,45,67,454,34]
for nums_12 in numbers:
    cnt = cnt + 1
cnt = cnt -1
x = 0
y = 0
for z in range(1, 10000000000000000000000000):
    if numbers[x] < numbers[x + 1]:
        y = numbers[x]
        numbers[x] = numbers[x + 1]
        numbers[x + 1] = y
        x = 0
    else:
        x = x + 1
    if x == cnt:
        break
print(numbers)


print('For loop to print the multiples of 3 using range() function:')
g = 0
for num_13 in range(10):
    g = g + 3
    print(g)
    
  
print('For loop to print the multiples of 5 using range() function:')
h = 0
for num_14 in range(20):
    h = h + 5
    print(h)
    

print('For loop to print the numbers in reverse order using range() function:')
j = 11
for num_15 in range(10):
    j = j -1
    print(j)