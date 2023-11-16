indices = {1}
out = [int(i in indices) for i in range(10)]
print(out)
#Random Word Genorator
#random_word Output is Lower Case
myList = ['one', 'two', 'three']

myList.append('four')

print(myList)

# ['one', 'two', 'three', 'four']
y = 1
import random
x = (random.randint(1, 267751))

with open('words.txt') as f:
  while y != x:
    f.readline()
    y = y + 1
  random_word = f.readline().lower()

print(random_word)


#User Guesses A word
#user_guess Output Is Lower Case


is_right = False
while is_right == False:
  user_input = input('What Is Your Guess').lower()
  if len(random_word) != len(user_input):
    print('Wrong')
  else:
    for z in range(len(random_word)):
      for q in range(len(user_input)):
        break