# Inports and basic variables
race_info_true = False
race_picked = False
import time
import random



# --------------------Start up text--------------------
# Def type start loop
def type_start():
    start_input = input().lower()
    if start_input == "start":
        ()
    else:
        type_start()

# running start up text
print("Welcome to Oliver's magnifacint RPG simulator")
time.sleep(1.5)
print("Type start to play: ")
type_start()



# --------------------Picking a name--------------------
print(".")
print("Welcome adventurer")
time.sleep(1)
print("Who will you be known as?: ")
player_name = input()



# --------------------Picking a race--------------------
# def race stat view back loop
def race_stat_view():
    race_stat_view_input = input().lower()
    if race_stat_view_input == "back":
        race_info_menu()
    else:
        race_stat_view()
    
#  def race info input
def race_info_menu_input():
    race_info_input = input().lower()
    if race_info_input == "back":
        ()
    elif race_info_input == "human":
        print(".")
        print("- +1 to every stat")
        time.sleep(0.5)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "dwarf":
        print(".")
        print("- +2 to Constitution")
        time.sleep(0.5)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "gnome":
        print(".")
        print("- +2 to Intelligence")
        time.sleep(0.5)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "goblin":
        print(".")
        print("- +2 to Dexterity and +1 to Constitution")
        time.sleep(0.5)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "halfling":
        print(".")
        print("- +2 to Dexterity")
        time.sleep(0.5)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "elf":
        print(".")
        print("- +2 to Dexterity")
        time.sleep(0.5)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "half-elf":
        print(".")
        print("- +2 to Charisma and 2 Ability Score increases")
        time.sleep(0.5)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "tiefling":
        print(".")
        print("- +2 to Charisma and +1 to Intelligence")
        time.sleep(0.5)
        print("type 'back' to go back")
        race_stat_view()
    else:
        print("invalid input")
        race_info_menu_input()
        
# def race info menu
def race_info_menu():
    print(".")
    print("Each race efects your stats")
    time.sleep(0.5)
    print("Races:")
    time.sleep(0.5)
    print("Human")
    time.sleep(0.5)
    print("Dwarf")
    time.sleep(0.5)
    print("Gnome")
    time.sleep(0.5)
    print("Goblin")
    time.sleep(0.5)
    print("Halfling")
    time.sleep(0.5)
    print("Elf")
    time.sleep(0.5)
    print("Half-Elf")
    time.sleep(0.5)
    print("Tiefling")
    time.sleep(0.5)
    print("Type a 'race' to see it's stats or type 'back'")
    race_info_menu_input()
    
# race picking while loop
while race_picked == False:
    time.sleep(0.5)
    print(".")
    print(f"What will {player_name}'s race be?")
    time.sleep(0.5)
    print("type 'race info' for information on races, or type 'rand' for a random race.")
    race_pick_input = input().lower()
    if race_pick_input == "race info":
        race_info_menu()
    elif race_pick_input == "rand":
        rand_race = random.randrange(1,9)
        if rand_race == 1:
            player_race = "Human"
            race_picked = True
        elif rand_race == 2:
            player_race = "Dwarf"
            race_picked = True
        elif rand_race == 3:
            player_race = "Gnome"
            race_picked = True
        elif rand_race == 4:
            player_race = "Goblin"
            race_picked = True
        elif rand_race == 5:
            player_race = "Halfling"
            race_picked = True
        elif rand_race == 6:
            player_race = "Elf"
        elif rand_race == 7:
            race_picked = True
            player_race = "Half-Elf"
            race_picked = True
        elif rand_race == 8:
            player_race = "Tiefling"
            race_picked = True
    elif race_pick_input == "human":
        player_race = "Human"
        race_picked = True
    elif race_pick_input == "dwarf":
        player_race = "Dwarf"
        race_picked = True
    elif race_pick_input == "gnome":
        player_race = "Gnome"
        race_picked = True
    elif race_pick_input == "goblin":
        player_race = "Goblin"
        race_picked = True
    elif race_pick_input == "halfling":
        player_race = "Halfling"
        race_picked = True
    elif race_pick_input == "elf":
        player_race = "Elf"
        race_picked = True
    elif race_pick_input == "half-elf":
        player_race = "Half-Elf"
        race_picked = True
    elif race_pick_input == "tiefling":
        player_race = "Tiefling"
        race_picked = True
    else:
        print("Invalid race")



# --------------------Picking stats--------------------
# 
