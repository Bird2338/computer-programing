# Inports and basic variables
race_info_true = False
race_picked = False
import time
import random



# ----------Start up text----------
# Def type start loop
def type_start():
    start_input = input().lower()
    if start_input == "start":
        ()
    else:
        type_start()

# running start up text
print("Welcome to Oliver's magnifacint RPG simulator")
time.sleep(2)
print("Type start to play: ")
type_start()



# ----------Picking a name----------
print("Welcome adventurer")
time.sleep(1)
print("Who will you be known as?: ")
player_name = input()



# ----------Picking a race----------
# race picking while loop
while race_picked == False:
    time.sleep(1)
    print(f"What will {player_name}'s race be?")
    time.sleep(1)
    print("Type a 'race' or type 'race info': ")
    race_pick_input = input().lower()
    if race_pick_input == "race info":
        print(True)
