# Inports and basic variables
import time
import random


# def Type start loop
def type_start():
    start_input = input().lower()
    if start_input == 'start':
        ()
    else:
        type_start()



# Start up text
print("Welcome to Oliver's magnifacint RPG simulator")
time.sleep(2)
print('Type start to play: ')
type_start()



# Picking a name
print('Welcome adventurer')
time.sleep(1)
player_name = input('What shall you be known as? ')
