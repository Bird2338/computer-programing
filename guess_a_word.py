#Random Word Genorator
#random_word Output is Lower Case
y = 1
import random
x = (random.randint(1, 267751))

with open('words.txt') as f:
  while y != x:
    f.readline()
    y = y + 1
  random_word = f.readline().lower()

print(random_word)
print(len(random_word))


#User Guesses A word
#user_guess Output Is Lower Case
is_right = False
while is_right == False:
  user_input = input('What Is Your Guess: ').lower()
  if len(random_word) - 1 != len(user_input):
    print('Wrong')
  else:
    for z in range(len(random_word) - 1):
      print(user_input[z])
      print(random_word[z])
      if user_input[z] == random_word[z]:
        print('yay')