y = 1
import random
x = (random.randint(1, 267751))

with open('words.txt') as f:
  while y != x:
    f.readline()
    y = y + 1
  word = f.readline()

word = word.lower()
print(word)

guess = input('give me one or more letters: ')
guess = guess.lower()
for z in range(len(word)):
  for q in range(len(guess)):
    if z != q:
      break
    elif word[z] == guess[q]:
      print(word[z])
