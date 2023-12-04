# --------------------Inports and basic variables--------------------
# inports
import time
import random

# variabls
race_picked = False
race_info_true = False
hold = 0
is_stats_done = False
stat_points = 15



# --------------------Player charactor index--------------------
# player index
player = {
    "name": 0,
    "race": 0,
    "speed": 0,
    "darkvision": 0,
    "resistances": [],
    "abilitys": [],
    "proficiencies": [],
    "str": 10,
    "dex": 10,
    "con": 10,
    "int": 10,
    "wis": 10,
    "cha": 10,
}



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
time.sleep(1)
print("Type start to play: ")
type_start()



# --------------------Picking a name--------------------
print(".")
time.sleep(1)
print("Welcome adventurer")
time.sleep(1)
print("Who will you be known as?: ")
player["name"] = input()



# --------------------Picking a race--------------------
# def race stat view back loop
def race_stat_view():
    race_stat_view_input = input().lower()
    if race_stat_view_input == "back":
        ()
    else:
        race_stat_view()
    
#  def race info input
def race_info_menu_input():
    race_info_input = input().lower()
    if race_info_input == "back":
        ()
    elif race_info_input == "human":
        print(".")
        time.sleep(1)
        print("----------Human Stats----------")
        time.sleep(1)
        print("- +1 to every stat")
        time.sleep(0.1)
        print("- speed = 30 feet")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "dwarf":
        print(".")
        time.sleep(1)
        print("----------Dwarf Stats----------")
        time.sleep(1)
        print("- +2 to Constitution")
        time.sleep(0.1)
        print("- Darkvision")
        time.sleep(0.1)
        print("- Speed = 25 Feet")
        time.sleep(0.1)
        print("- Poison Resist")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "gnome":
        print(".")
        time.sleep(1)
        print("----------Gnome Stats----------")
        time.sleep(1)
        print("- +2 to Intelligence")
        time.sleep(0.1)
        print("- Darkvision")
        time.sleep(0.1)
        print("- Speed = 25 Feet")
        time.sleep(0.1)
        print("-Mind Magic Resist")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "goblin":
        print(".")
        time.sleep(1)
        print("----------Goblin Stats----------")
        time.sleep(1)
        print("- +2 to Dexterity and +1 to Constitution")
        time.sleep(0.1)
        print("- Darkvision")
        time.sleep(0.1)
        print("- Speed = 30 Feet")
        time.sleep(0.1)
        print("- Charm Resist")
        time.sleep(0.1)
        print("- Nimble Escape = Disengage or Hide action as a bonus action")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "halfling":
        print(".")
        time.sleep(1)
        print("----------Halfling Stats----------")
        time.sleep(1)
        print("- +2 to Dexterity")
        time.sleep(0.1)
        print("- Speed = 25 Feet")
        time.sleep(0.1)
        print("- Lucky = if you roll a one you reroll the dice")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "elf":
        print(".")
        time.sleep(1)
        print("----------Elf Stats----------")
        time.sleep(1)
        print("- +2 to Dexterity")
        time.sleep(0.1)
        print("- Darkvision")
        time.sleep(0.1)
        print("- Speed = 30 Feet")
        time.sleep(0.1)
        print("- Charm Resist")
        time.sleep(0.1)
        print("- Proficiency In Perception")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "half-elf":
        print(".")
        time.sleep(1)
        print("----------Half-Elf Stats----------")
        time.sleep(1)
        print("- +2 to Charisma and 2 Ability Score increases")
        time.sleep(0.1)
        print("- Darkvision")
        time.sleep(0.1)
        print("- Speed = 30 Feet")
        time.sleep(0.1)
        print("- Charm Resist")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "tiefling":
        print(".")
        time.sleep(1)
        print("----------Tiefling Stats----------")
        time.sleep(1)
        print("- +2 to Charisma and +1 to Intelligence")
        time.sleep(0.1)
        print("- Darkvision")
        time.sleep(0.1)
        print("- Speed = 30 Feet")
        time.sleep(0.1)
        print("- Fire Resist")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    else:
        print("invalid input")
        race_info_menu_input()
        
# def race info menu
def race_info_menu():
    print(".")
    time.sleep(1)
    print("Each race efects your stats")
    time.sleep(1)
    print("Races:")
    time.sleep(1)
    print("Human")
    time.sleep(0.1)
    print("Dwarf")
    time.sleep(0.1)
    print("Gnome")
    time.sleep(0.1)
    print("Goblin")
    time.sleep(0.1)
    print("Halfling")
    time.sleep(0.1)
    print("Elf")
    time.sleep(0.1)
    print("Half-Elf")
    time.sleep(0.1)
    print("Tiefling")
    time.sleep(1)
    print("Type a 'race' to see it's stats or type 'back'")
    race_info_menu_input()
    
# race picking while loop
while race_picked == False:
    print(".")
    time.sleep(1)
    name_hold = player["name"]
    print(f"What will {name_hold}'s race be?")
    time.sleep(1)
    print("type 'race info' for information on races, or type 'rand' for a random race.")
    race_pick_input = input().lower()
    if race_pick_input == "race info":
        race_info_menu()
    elif race_pick_input == "rand":
        rand_race = random.randrange(1,9)
        if rand_race == 1:
            player["race"] = "Human"
            race_picked = True
        elif rand_race == 2:
            player["race"] = "Dwarf"
            race_picked = True
        elif rand_race == 3:
            player["race"] = "Gnome"
            race_picked = True
        elif rand_race == 4:
            player["race"] = "Goblin"
            race_picked = True
        elif rand_race == 5:
            player["race"] = "Halfling"
            race_picked = True
        elif rand_race == 6:
            player["race"] = "Elf"
        elif rand_race == 7:
            race_picked = True
            player["race"] = "Half-Elf"
            race_picked = True
        elif rand_race == 8:
            player["race"] = "Tiefling"
            race_picked = True
    elif race_pick_input == "human":
        player["race"] = "Human"
        race_picked = True
    elif race_pick_input == "dwarf":
        player["race"] = "Dwarf"
        race_picked = True
    elif race_pick_input == "gnome":
        player["race"] = "Gnome"
        race_picked = True
    elif race_pick_input == "goblin":
        player["race"] = "Goblin"
        race_picked = True
    elif race_pick_input == "halfling":
        player["race"] = "Halfling"
        race_picked = True
    elif race_pick_input == "elf":
        player["race"] = "Elf"
        race_picked = True
    elif race_pick_input == "half-elf":
        player["race"] = "Half-Elf"
        race_picked = True
    elif race_pick_input == "tiefling":
        player["race"] = "Tiefling"
        race_picked = True
    else:
        print("Invalid race")

# Race atributes
if player["race"] == "Human":
    player["speed"] = 30
elif player["race"] == "Dwarf":
    player["speed"] = 25
    player["darkvision"] = True
    player["resistances"].append("poison")
elif player["race"] == "Gnome":
    player["speed"] = 25
    player["darkvision"] = True
    player["resistances"].append("mind magic")
elif player["race"] == "Goblin":
    player["speed"] = 30
    player["darkvision"] = True
    player["resistances"].append("charm")
    player["abilitys"].append("nimble escape")
elif player["race"] == "Halfling":
    player["speed"] = 25
    player["abilitys"].append("lucky")
elif player["race"] == "Elf":
    player["speed"] = 30
    player["darkvision"] = True
    player["resistances"].append("charm")
    player["proficiencies"].append("Perception")
elif player["race"] == "Half-Elf":
    player["speed"] = 30
    player["darkvision"] = True
    player["resistances"].append("charm")
elif player["race"] == "Tiefling":
    player["speed"] = 30
    player["darkvision"] = True
    player["resistances"].append("fire")
    


# --------------------Picking stats--------------------
# print stat instructions
print(".")
time.sleep(1)
print(f"You have {stat_points} points to spend on stats")
time.sleep(0.1)
print("The lowest your stats can go is 8 and the highest is 15")
time.sleep(0.1)
print("your stats start at 8")
time.sleep(0.1)
print("type '+' or '-' followed by the first three letters of a stat")
time.sleep(0.1)
print("removing a point will give you that point back to be spent somewhere else")

# print stats
def print_stats():
    print(".")
    time.sleep(1)
    print("-----Stats-----")
    time.sleep(0.1)
    hold = player["str"]
    print(f"strength {hold}")
    time.sleep(0.1)
    hold = player["dex"]
    print(f"dexterity {hold}")
    time.sleep(0.1)
    hold = player["con"]
    print(f"constitution {hold}")
    time.sleep(0.1)
    hold = player["int"]
    print(f"intelligence {hold}")
    time.sleep(0.1)
    hold = player["wis"]
    print(f"wisdom {hold}")
    time.sleep(0.1)
    hold = player["cha"]
    print(f"charisma {hold}")

# stat_input_loop
def stat_input_loop():
    global player
    global stat_points
    stat_input = input()
    if len(stat_input) == 5:
        if (stat_input[2] == "s") and (stat_input[3] == "t") and (stat_input[4] == "r"):
            print(True)
        else:
            print("Invalid Input")
            stat_input_loop()
    else:
        print("Invalid Input")
        stat_input_loop()
# Picking stats loop
while is_stats_done == False:
    print_stats()
    
    
    
# --------------------Race stat increases--------------------
