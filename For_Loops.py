word = 'cheese'
for item in word:
    print(item)


for nums_1 in range(1, 10):
    print(nums_1)


Cheese_List = ['Bree', 'Parm', 'Goat', 'Blue']
print('Cheese types:')
for Cheese in Cheese_List:
    print(Cheese)
    
    
flowers = ['Jasmine','Lotus','Rose','Sunflower']
for Fl in flowers:
    if Fl == 'Rose':
         break
    else:
         print(Fl)

list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
for nums_2 in list1:
    for veggies in list2:
        print(f'{nums_2} {veggies}')
        
        
colors = ['blue','red','green','yellow']
for co in colors:
    if co == 'green':
         break
    else:
         print(co)


vehicles = ['Car','Cycle','Bus','Tempo']
for ve in vehicles:
    if ve == 'Bus':
         continue
    else:
         print(ve)
         
         
Numbers = [12,3,56,67,89,90]
count = 0
for nums_4 in Numbers:
    count = count + 1
print(count)


Numbers = [12,3,56,67,89,90]
Sum = 0
for nums_3 in Numbers:
    Sum = (Sum + nums_3)
    print(Sum)
    
    
