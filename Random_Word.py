y = 1
import random
x = (random.randint(1, 267751))
print(x)

with open('words.txt') as f:
  while y != x:
    f.readline()
    y = y + 1
  print(f.readline())
    