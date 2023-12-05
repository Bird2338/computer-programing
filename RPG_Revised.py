# --------------------Inports and basic variables--------------------
# inports
import time
import random
import math

# variabls
race_picked = False
race_info_true = False
hold = 0
is_stats_done = False
stat_points = 15
new_to_this = True



# --------------------item indexes--------------------
# health potion
health_potion = {
    "type": "potion"
}



# --------------------Player charactor index--------------------
# player index
player = {
    # base stats
    "max_health": 0,
    "health": 0,
    "gold": 0,
    "level": 1,
    "name": 0,
    "race": 0,
    "speed": 0,
    # stats
    "str": 10,
    "dex": 10,
    "con": 10,
    "int": 10,
    "wis": 10,
    "cha": 10,
    # abilitys
    "darkvision": 0,
    "resistances": [],
    "abilitys": [],
    "proficiencies": [],
    "invintory": [],
    # weapons
    "weapon_one": 0,
    "weapon_two": 0,
    # spells
    "spells": [],
    # armors
    "gauntlets": 0,
    "main_armor": 0,
    "helm": 0,
    "boots": 0,
    # trinkets
    "ring_one": 0,
    "ring_two": 0,
    "amulet": 0,
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
print(f"You have {stat_points} points to spend on stats.")
time.sleep(0.1)
print("The lowest your stats can go is 8 and the highest is 15.")
time.sleep(0.1)
print("your stats start at 8.")
time.sleep(0.1)
print("type '+'number or '-'number followed by the first three letters of a stat.")
time.sleep(0.1)
print("example - '+3str'")
time.sleep(0.1)
print("removing a point will give you that point back to be spent somewhere else.")

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
            if stat_input[0] == "+":
                if player["str"] + int(stat_input[1]) <= 15:
                    hold = player["str"]
                    player["str"] = hold + int(stat_input[1])
                    hold = stat_points
                    stat_points = hold - int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            elif stat_input[0] == "-":
                if player["str"] - int(stat_input[1]) >= 8:
                    hold = player["str"]
                    player["str"] = hold - int(stat_input[1])
                    hold = stat_points
                    stat_points = hold + int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            else:
                print("Invalid Input")
                stat_input_loop()
        elif (stat_input[2] == "d") and (stat_input[3] == "e") and (stat_input[4] == "x"):
            if stat_input[0] == "+":
                if player["dex"] + int(stat_input[1]) <= 15:
                    hold = player["dex"]
                    player["dex"] = hold + int(stat_input[1])
                    hold = stat_points
                    stat_points = hold - int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            elif stat_input[0] == "-":
                if player["dex"] - int(stat_input[1]) >= 8:
                    hold = player["dex"]
                    player["dex"] = hold - int(stat_input[1])
                    hold = stat_points
                    stat_points = hold + int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            else:
                print("Invalid Input")
                stat_input_loop()
        elif (stat_input[2] == "c") and (stat_input[3] == "o") and (stat_input[4] == "n"):
            if stat_input[0] == "+":
                if player["con"] + int(stat_input[1]) <= 15:
                    hold = player["con"]
                    player["con"] = hold + int(stat_input[1])
                    hold = stat_points
                    stat_points = hold - int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            elif stat_input[0] == "-":
                if player["con"] - int(stat_input[1]) >= 8:
                    hold = player["con"]
                    player["con"] = hold - int(stat_input[1])
                    hold = stat_points
                    stat_points = hold + int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            else:
                print("Invalid Input")
                stat_input_loop()
        elif (stat_input[2] == "i") and (stat_input[3] == "n") and (stat_input[4] == "t"):
            if stat_input[0] == "+":
                if player["int"] + int(stat_input[1]) <= 15:
                    hold = player["int"]
                    player["int"] = hold + int(stat_input[1])
                    hold = stat_points
                    stat_points = hold - int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            elif stat_input[0] == "-":
                if player["int"] - int(stat_input[1]) >= 8:
                    hold = player["int"]
                    player["int"] = hold - int(stat_input[1])
                    hold = stat_points
                    stat_points = hold + int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            else:
                print("Invalid Input")
                stat_input_loop()
        elif (stat_input[2] == "w") and (stat_input[3] == "i") and (stat_input[4] == "s"):
            if stat_input[0] == "+":
                if player["wis"] + int(stat_input[1]) <= 15:
                    hold = player["wis"]
                    player["wis"] = hold + int(stat_input[1])
                    hold = stat_points
                    stat_points = hold - int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            elif stat_input[0] == "-":
                if player["wis"] - int(stat_input[1]) >= 8:
                    hold = player["wis"]
                    player["wis"] = hold - int(stat_input[1])
                    hold = stat_points
                    stat_points = hold + int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            else:
                print("Invalid Input")
                stat_input_loop()
        elif (stat_input[2] == "c") and (stat_input[3] == "h") and (stat_input[4] == "a"):
            if stat_input[0] == "+":
                if player["cha"] + int(stat_input[1]) <= 15:
                    hold = player["cha"]
                    player["cha"] = hold + int(stat_input[1])
                    hold = stat_points
                    stat_points = hold - int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            elif stat_input[0] == "-":
                if player["cha"] - int(stat_input[1]) >= 8:
                    hold = player["cha"]
                    player["cha"] = hold - int(stat_input[1])
                    hold = stat_points
                    stat_points = hold + int(stat_input[1])
                else:
                    print("Invalid Input")
                    stat_input_loop()
            else:
                print("Invalid Input")
                stat_input_loop()
        else:
            print("Invalid Input")
            stat_input_loop()
        
    else:
        print("Invalid Input")
        stat_input_loop()
        
# is done picking stats loop
def done_picking_stats_input():
    stat_done = input().lower()
    if stat_done == "y":
        global is_stats_done
        is_stats_done = True
    else:
        ()

# Picking stats loop
while is_stats_done == False:
    print_stats()
    print(f"you have {stat_points} points left")
    stat_input_loop()
    if stat_points == 0:
        print_stats()
        print("you have 0 points left, are you done picking stats? y/n")
        done_picking_stats_input()
    
    
    
# --------------------Race stat increases--------------------
def ability_score_increase():
    print(".")
    time.sleep(1)
    print("abiltiy score increase")
    time.sleep(0.1)
    print("Type the first three letters of the ability you wish to increase by one")
    print_stats()
    ability_score_increase_input = input().lower()
    if ability_score_increase_input == "str":
        hold = player["str"]
        player["str"] = hold + 1
    elif ability_score_increase_input == "dex":
        hold = player["dex"]
        player["dex"] = hold + 1
    elif ability_score_increase_input == "con":
        hold = player["con"]
        player["con"] = hold + 1
    elif ability_score_increase_input == "int":
        hold = player["int"]
        player["int"] = hold + 1
    elif ability_score_increase_input == "wis":
        hold = player["wis"]
        player["wis"] = hold + 1
    elif ability_score_increase_input == "cha":
        hold = player["cha"]
        player["cha"] = hold + 1
    else:
        print("Invalid input")
        ability_score_increase_input()

if player["race"] == "Human":
    hold = player["str"]
    player["str"] = hold + 1
    hold = player["dex"]
    player["dex"] = hold + 1
    hold = player["con"]
    player["con"] = hold + 1
    hold = player["int"]
    player["int"] = hold + 1
    hold = player["wis"]
    player["wis"] = hold + 1
    hold = player["cha"]
    player["cha"] = hold + 1
elif player["race"] == "Dwarf":
    hold = player["con"]
    player["con"] = hold + 2
elif player["race"] == "Gnome":
    hold = player["int"]
    player["int"] = hold + 2
elif player["race"] == "Goblin":
    hold = player["dex"]
    player["dex"] = hold + 2
    hold = player["con"]
    player["con"] = hold + 1
elif player["race"] == "Halfling":
    hold = player["dex"]
    player["dex"] = hold + 2
elif player["race"] == "Elf":
    hold = player["dex"]
    player["dex"] = hold + 2
elif player["race"] == "Half-Elf":
    ability_score_increase()
    print_stats()
    ability_score_increase()
    print_stats()
    hold = player["cha"]
    player["cha"] = hold + 2
elif player["race"] == "Tiefling":
    hold = player["cha"]
    player["cha"] = hold + 2
    hold = player["int"]
    player["int"] = hold + 1

# print final stats
print(".")
time.sleep(1)
print("-----Final Stats-----")
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



# --------------------Health--------------------
player["max_health"] = 5 + int(math.floor((player["con"] - 10) / 2))
player["health"] = player["max_health"]



# --------------------Start up text--------------------
# Def type start loop
def type_game_start():
    start_game_input = input().lower()
    if start_game_input == "start":
        ()
    elif start_game_input == "/dev add":
        player = {
        # base stats
        "max_health": 0,
        "health": 0,
        "gold": 0,
        "level": 1,
        "name": 0,
        "race": 0,
        "speed": 0,
        # stats
        "str": 10,
        "dex": 10,
        "con": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        # abilitys
        "darkvision": 0,
        "resistances": [],
        "abilitys": [],
        "proficiencies": [],
        "invintory": [],
        # weapons
        "weapon_one": 0,
        "weapon_two": 0,
        # spells
        "spells": [],
        # armors
        "gauntlets": 0,
        "main_armor": 0,
        "helm": 0,
        "boots": 0,
        # trinkets
        "ring_one": 0,
        "ring_two": 0,
        "amulet": 0,
        }
    else:
        type_game_start()



# running start up text
print(".")
time.sleep(1)
print(f"Welcome to Illdara {name_hold}")
time.sleep(1)
print("Type start to play: ")
type_game_start()



# intro text
import time
print(".")
time.sleep(1)
print("You have been called by His Majesty, 'High Eldchester Aldvon',")
print("to Hunt the uncanny and Dangerous beasts, roaming the countryside.")
print(".")
time.sleep(6)
print("It is a sunny morning and the sun glistens off the dewy grass")
print("as you leave the small picturesque town of Fellsburry.")
print(".")
time.sleep(6)
print("The path fades from cobble to a dusty dirt road")
print("as you walk down the hill towards the Thornwood forest.")
print(".")
time.sleep(6)


# --------------------intoduction--------------------
# Old Man Be Talkin
print("As you come cloaser to the edge of the forest")
print("you are stoped by a small hunched old man sitting on a ramshackle dirty cart.")
print(".")
time.sleep(6)
print("The man speeks to you in a creaky sharp voice.")
print(".")
time.sleep(3)
print("-----Old Man-----")
print("I see your Leaving the city.")
print(".")
time.sleep(3)
print("Might I intrest you in some knowledge, sire?")
print(".")
time.sleep(3)
print("Before you leave, there are a few things you must know.")
print(".")
time.sleep(3)
print("If you should ever in doubt along your travals just type '?'")
print("To see what commands you can preform.")
print(".")
time.sleep(6)
print("You will learn the rest along the way.")
print(".")
time.sleep(3)
if new_to_this == True:
    print("-----Old Man-----")
    print(f"I see you are new to this{name_hold}.")
    print(".")
    time.sleep(2)
    print("I shall give you two health potions")
    print
    print(".")
    player["invintory"].append("health_potion")
    player["invintory"].append("health_potion")
    time.sleep(3)
    print("-----Old Man-----")
    print("It seems you don't have a weapon yet.")
    print(".")
    time.sleep(2)
    print("perhaps you will find somthing in this old cart of mine.")
    print(".")
    time.sleep(3)
    print("-----------------")
    print("You search the cart and are rewarded with the discovery of")
    print("a slightly rusty short sword that still glints in the sun.")
    player["invintory"].append("short_sword")
    print(".")
    time.sleep(6)
    print("-----Old Man-----")
    print("You still need to equip the sword in your invintory.")
    print(".")
    time.sleep(3)
    print("But im sure you can figure it out.")
    print(".")
    time.sleep(3)
print("That is all I have to say, good luck.")
print("-----------------")

print(player)


