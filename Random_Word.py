y = 0
import random
x = (random.randint(1, 3))
print(x)

with open('words.txt') as f:
  while y != x:
    f.readline()
    y = y + 1
  print(f.readline())
    