# --------------------Inports and basic variables--------------------
# inports
from time import sleep
import random
import math

# global time
# global random
# global math

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
    "AC": 0,
    # abilitys
    "darkvision": 0,
    "resistances": [],
    "abilitys": [],
    "proficiencies": [],
    "invintory": [],
    # weapons
    "weapon": 0,
    # spells
    "spells": [],
    # armors
    "gauntlets": 0,
    "main_armor": 0,
    "helm": 0,
    "boots": 0,
    # trinkets
    "ring": 0,
    "amulet": 0,
    # player area
    "area": "forest",
    "where": "trail"
}



# --------------------Start up text--------------------
# Def type start loop
def type_start():
    global race_picked
    global race_info_true
    global hold
    global is_stats_done
    global stat_points
    global new_to_this
    global health_potion
    global player
    start_input = input("input: ").lower()
    if start_input == "start":
        
        # --------------------Picking a name--------------------
        print(".")
        sleep(1)
        print("Welcome adventurer")
        sleep(1)
        print("Who will you be known as?: ")
        player["name"] = input("input: ")



        # --------------------Picking a race--------------------
        # def race stat view back loop
        def race_stat_view():
            race_stat_view_input = input("input: ").lower()
            if race_stat_view_input == "back":
                ()
            else:
                race_stat_view()
            
        #  def race info input
        def race_info_menu_input():
            race_info_input = input("input: ").lower()
            if race_info_input == "back":
                ()
            elif race_info_input == "human":
                print(".")
                sleep(1)
                print("----------Human Stats----------")
                sleep(1)
                print("- +1 to every stat")
                sleep(0.1)
                print("- speed = 30 feet")
                sleep(0.1)
                print("type 'back' to go back")
                race_stat_view()
            elif race_info_input == "dwarf":
                print(".")
                sleep(1)
                print("----------Dwarf Stats----------")
                sleep(1)
                print("- +2 to Constitution")
                sleep(0.1)
                print("- Darkvision")
                sleep(0.1)
                print("- Speed = 25 Feet")
                sleep(0.1)
                print("- Poison Resist")
                sleep(0.1)
                print("type 'back' to go back")
                race_stat_view()
            elif race_info_input == "gnome":
                print(".")
                sleep(1)
                print("----------Gnome Stats----------")
                sleep(1)
                print("- +2 to Intelligence")
                sleep(0.1)
                print("- Darkvision")
                sleep(0.1)
                print("- Speed = 25 Feet")
                sleep(0.1)
                print("-Mind Magic Resist")
                sleep(0.1)
                print("type 'back' to go back")
                race_stat_view()
            elif race_info_input == "goblin":
                print(".")
                sleep(1)
                print("----------Goblin Stats----------")
                sleep(1)
                print("- +2 to Dexterity and +1 to Constitution")
                sleep(0.1)
                print("- Darkvision")
                sleep(0.1)
                print("- Speed = 30 Feet")
                sleep(0.1)
                print("- Charm Resist")
                sleep(0.1)
                print("- Nimble Escape = Disengage or Hide action as a bonus action")
                sleep(0.1)
                print("type 'back' to go back")
                race_stat_view()
            elif race_info_input == "halfling":
                print(".")
                sleep(1)
                print("----------Halfling Stats----------")
                sleep(1)
                print("- +2 to Dexterity")
                sleep(0.1)
                print("- Speed = 25 Feet")
                sleep(0.1)
                print("- Lucky = if you roll a one you reroll the dice")
                sleep(0.1)
                print("type 'back' to go back")
                race_stat_view()
            elif race_info_input == "elf":
                print(".")
                sleep(1)
                print("----------Elf Stats----------")
                sleep(1)
                print("- +2 to Dexterity")
                sleep(0.1)
                print("- Darkvision")
                sleep(0.1)
                print("- Speed = 30 Feet")
                sleep(0.1)
                print("- Charm Resist")
                sleep(0.1)
                print("- Proficiency In Perception")
                sleep(0.1)
                print("type 'back' to go back")
                race_stat_view()
            elif race_info_input == "half-elf":
                print(".")
                sleep(1)
                print("----------Half-Elf Stats----------")
                sleep(1)
                print("- +2 to Charisma and 2 Ability Score increases")
                sleep(0.1)
                print("- Darkvision")
                sleep(0.1)
                print("- Speed = 30 Feet")
                sleep(0.1)
                print("- Charm Resist")
                sleep(0.1)
                print("type 'back' to go back")
                race_stat_view()
            elif race_info_input == "tiefling":
                print(".")
                sleep(1)
                print("----------Tiefling Stats----------")
                sleep(1)
                print("- +2 to Charisma and +1 to Intelligence")
                sleep(0.1)
                print("- Darkvision")
                sleep(0.1)
                print("- Speed = 30 Feet")
                sleep(0.1)
                print("- Fire Resist")
                sleep(0.1)
                print("type 'back' to go back")
                race_stat_view()
            else:
                print("invalid input")
                race_info_menu_input()
                
        # def race info menu
        def race_info_menu():
            print(".")
            sleep(1)
            print("Each race efects your stats")
            sleep(1)
            print("Races:")
            sleep(1)
            print("Human")
            sleep(0.1)
            print("Dwarf")
            sleep(0.1)
            print("Gnome")
            sleep(0.1)
            print("Goblin")
            sleep(0.1)
            print("Halfling")
            sleep(0.1)
            print("Elf")
            sleep(0.1)
            print("Half-Elf")
            sleep(0.1)
            print("Tiefling")
            sleep(1)
            print("Type a 'race' to see it's stats or type 'back'")
            race_info_menu_input()
            
        # race picking while loop
        while race_picked == False:
            print(".")
            sleep(1)
            name_hold = player["name"]
            print(f"What will {name_hold}'s race be?")
            sleep(1)
            print("type 'race info' for information on races, or type 'rand' for a random race.")
            race_pick_input = input("input: ").lower()
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
        sleep(1)
        print(f"You have {stat_points} points to spend on stats.")
        sleep(0.1)
        print("The lowest your stats can go is 8 and the highest is 15.")
        sleep(0.1)
        print("your stats start at 8.")
        sleep(0.1)
        print("type '+'number or '-'number followed by the first three letters of a stat.")
        sleep(0.1)
        print("example - '+3str'")
        sleep(0.1)
        print("removing a point will give you that point back to be spent somewhere else.")

        # print stats
        def print_stats():
            print(".")
            sleep(1)
            print("-----Stats-----")
            sleep(0.1)
            hold = player["str"]
            print(f"strength {hold}")
            sleep(0.1)
            hold = player["dex"]
            print(f"dexterity {hold}")
            sleep(0.1)
            hold = player["con"]
            print(f"constitution {hold}")
            sleep(0.1)
            hold = player["int"]
            print(f"intelligence {hold}")
            sleep(0.1)
            hold = player["wis"]
            print(f"wisdom {hold}")
            sleep(0.1)
            hold = player["cha"]
            print(f"charisma {hold}")

        # stat_input_loop
        def stat_input_loop():
            global player
            global stat_points
            stat_input = input("input: ")
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
            stat_done = input("input: ").lower()
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
            sleep(1)
            print("abiltiy score increase")
            sleep(0.1)
            print("Type the first three letters of the ability you wish to increase by one")
            print_stats()
            ability_score_increase_input = input("input: ").lower()
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
        sleep(1)
        print("-----Final Stats-----")
        sleep(0.1)
        hold = player["str"]
        print(f"strength {hold}")
        sleep(0.1)
        hold = player["dex"]
        print(f"dexterity {hold}")
        sleep(0.1)
        hold = player["con"]
        print(f"constitution {hold}")
        sleep(0.1)
        hold = player["int"]
        print(f"intelligence {hold}")
        sleep(0.1)
        hold = player["wis"]
        print(f"wisdom {hold}")
        sleep(0.1)
        hold = player["cha"]
        print(f"charisma {hold}")



        # --------------------Health--------------------
        player["max_health"] = 5 + int(math.floor((player["con"] - 10) / 2))
        player["health"] = player["max_health"]
        
        player["AC"] = 10 + int(math.floor((player["dex"] - 10) / 2))


        # --------------------Start up text--------------------
        # Def type start loop
        def type_game_start():
            start_game_input = input("input: ").lower()
            if start_game_input == "start":
                ()
            else:
                type_game_start()

        # running start up text
        print(".")
        sleep(1)
        print(f"Welcome to Illdara {name_hold}")
        sleep(1)
        print("Type start to play: ")
        type_game_start()

        # intro text
        import time
        print(".")
        sleep(1)
        print("You have been called by His Majesty, 'High Eldchester Aldvon',")
        print("to Hunt the uncanny and Dangerous beasts, roaming the countryside.")
        print(".")
        sleep(0.1)
        print("It is a sunny morning and the sun glistens off the dewy grass")
        print("as you leave the small picturesque town of Fellsburry.")
        print(".")
        sleep(0.1)
        print("The path fades from cobble to a dusty dirt road")
        print("as you walk down the hill towards the Thornwood forest.")
        print(".")
        sleep(0.1)
        print("--enter--")
        enter = input()



        # --------------------intoduction--------------------
        # Old Man Be Talkin
        print("As you come cloaser to the edge of the forest")
        print("you are stoped by a small hunched old man sitting on a ramshackle dirty cart.")
        print(".")
        sleep(0.1)
        print("The man speeks to you in a creaky sharp voice.")
        print(".")
        sleep(0.1)
        print("--enter--")
        enter = input()
        print("-----Old Man-----")
        print("I see your Leaving the city.")
        print(".")
        sleep(0.1)
        print("Might I intrest you in some knowledge, sire?")
        print(".")
        sleep(0.1)
        print("--enter--")
        enter = input()
        print("Before you leave, there are a few things you must know.")
        print(".")
        sleep(0.1)
        print("If you should ever in doubt along your travals just type '?'")
        print("To see what commands you can preform.")
        print(".")
        sleep(0.1)
        print("You will learn the rest along the way.")
        print(".")
        sleep(0.1)
        print("--enter--")
        enter = input()
        if new_to_this == True:
            print("-----Old Man-----")
            print(f"I see you are new to this {name_hold}.")
            print(".")
            sleep(0.1)
            print("I shall give you two health potions")
            print
            print(".")
            player["invintory"].append("health_potion")
            player["invintory"].append("health_potion")
            sleep(0.1)
            print("--enter--")
            enter = input()
            print("-----Old Man-----")
            print("It seems you don't have a weapon yet.")
            print(".")
            sleep(0.1)
            print("perhaps you will find somthing in this old cart of mine.")
            print(".")
            sleep(0.1)
            print("--enter--")
            enter = input()
            print("-----------------")
            print("You search the cart and are rewarded with the discovery of")
            print("a slightly rusty short sword that still glints in the sun.")
            player["invintory"].append("short_sword")
            print(".")
            sleep(0.1)
            print("--enter--")
            enter = input()
            print("-----Old Man-----")
            print("You still need to equip the sword in your invintory.")
            print(".")
            sleep(0.1)
            print("But im sure you can figure it out.")
            print(".")
            sleep(0.1)
        print("That is all I have to say, good luck.")
        print("-----------------")
        print("--enter--")
        enter = input()
        print("After Talking to the old man, you continue on your way.")
        print(".")
        sleep(0.1)
        print("soon you see the forest looming cloaser, the trees seem to envelop you as you enter.")


    elif start_input == "/import":
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
                    "AC": 12,
                    # abilitys
                    "darkvision": 0,
                    "resistances": [],
                    "abilitys": [],
                    "proficiencies": [],
                    "invintory": ["health_potion", "health_potion", "short_sword"],
                    # weapons
                    "weapon": 0,
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
                    # player area
                    "area": "forest",
                    "where": "trail"
                }
    else:
        type_start()



# running start up text
print("Welcome to Oliver's magnifacint RPG simulator")
sleep(1)
print("Type start to play: ")
type_start()



# --------------------Game run--------------------
time = "morning"

# equiping
def equip():
    if new_hold == "short_sword":
        player["weapon"] = "short_sword"
        invintory_input()
    else:
        print("Invalid Input")
        invintory_input()




# invintory input
def invintory_input():
    global new_hold
    invintory_input_input = input("input: ").lower()
    if invintory_input_input == "back":
        ()
    elif len(invintory_input_input) < 5:
        print("Invalid Input")
        invintory_input()
    elif invintory_input_input[0] == "e" and invintory_input_input[1] != "q":
        new_hold = invintory_input_input.replace(" ", "").replace("e", "", 1)
        if new_hold in player["invintory"]:
            equip()
    elif invintory_input_input[0] == "e" and invintory_input_input[1] == "q" and invintory_input_input[2] == "u" and invintory_input_input[3] == "i" and invintory_input_input[4] == "p":
        new_hold = invintory_input_input.replace(" ", "").replace("equip", "")
        if new_hold in player["invintory"]:
            equip()
    elif invintory_input_input[0] == "?":
        new_hold = invintory_input_input.replace(" ", "").replace("?", "")
        if new_hold == "health_potion":
            print("A health_potion gives you 4d4 hitpoints.")
        elif new_hold == "short_sword":
            print("The short sword deals 1d6 + dex bounus damage.")
    elif invintory_input_input == "health_potion" and "health_potion" in player["invintory"]:
        player["invintory"].remove("health_potion")
        player["health"] += random.randrange(1, 5)
        print(player["health"])
        player["health"] += random.randrange(1, 5)
        print(player["health"])
        player["health"] += random.randrange(1, 5)
        print(player["health"])
        player["health"] += random.randrange(1, 5)
        print(player["health"])
    else:
        print("Invalid Input")
        invintory_input()
        
        

# invintory
def invintory():
    print(player["invintory"])
    print(".")
    sleep(0.1)
    print("type 'e' or 'equip' folowed by the name of an item to equip it.")
    print("type '?' followed by the name of an item to veiw it's stats.")
    print("Type the name of an item to use it.")
    print("or type 'back' to go back")
    invintory_input() 

# goblin stats
goblin = {
    "str": 8,
    "dex": 14,
    "con": 10,
    "int": 10,
    "wis": 8,
    "cha": 8,
    "health": 7,
    "AC": 15
}


# combat_input()
def combat_input():
    print(f"You have {player['health']} health left")
    print("what do you wish to do")
    print("if in doubt type '?'")
    combat_input_input = input("input: ").lower()
    if combat_input_input == "?":
        print("Here are a list of inputs for you to execute:")
        sleep(0.1)
        print("type 'a' or 'atack' to atack")
        sleep(0.1)
        print("type 'i' or 'invintory' in enter your invintory")
        combat_input()
    elif combat_input_input == "a" or "atack":
        your_roll = random.randrange(1, 21)
        if your_roll == 20:
            print("you rolled a nat 20 hitting it and doubleing the damage")
            your_atack = (random.randrange(1, 7) + int(math.floor((player["dex"] - 10) / 2))) * 2
            print(f"you manage to crit and slash at the goblin across the chest dealing {your_atack} damage!")
            goblin["health"] -= your_atack
        elif your_roll == 1:
            print("You Rolled a nat 1 and miss the goblin")
        elif your_roll >= goblin["AC"]:
            print(f"you Rolled a {your_roll} hitting the goblin")
            your_atack = random.randrange(1, 7) + int(math.floor((player["dex"] - 10) / 2))
            print(f"you manage to slash at the goblin across the chest dealing {your_atack} damage!")
            goblin["health"] -= your_atack
        else:
            print(f"you rolled a {your_roll} missing the goblin")
    elif combat_input_input == "i" or combat_input_input == "invintory":
        invintory()
        combat_input()  
    
    
# goblin combat
def goblin_combat():
    print("Out of the bushes jumps a goblin, growling and gnashing it's teeth!")
    global goblin
    combat_over = False
    while combat_over == False:
        combat_input()
        print("the goblin atempts to atack at you with it's short sword")
        enemy_roll = random.randrange(1, 21)
        if enemy_roll == 20:
            print("The Goblin Rolled a nat 20 hitting you and doubleing the damage")
            enemy_atack = (random.randrange(1, 7) + int(math.floor((goblin["dex"] - 10) / 2))) * 2
            print(f"the goblin manages to crit and slash at you across the chest dealing {enemy_atack} damage!")
            player["health"] -= enemy_atack
        elif enemy_roll == 1:
            print("The Goblin Rolled a nat 1 and misses you")
        elif enemy_roll >= player["AC"]:
            print(f"The Goblin Rolled a {enemy_roll} hitting you")
            enemy_atack = random.randrange(1, 7) + int(math.floor((goblin["dex"] - 10) / 2))
            print(f"the goblin manages to slash at you across the chest dealing {enemy_atack} damage!")
            player["health"] -= enemy_atack
        else:
            print(f"The Goblin Rolled a {enemy_roll} missing you you")
        if goblin["health"] <= 0:
            combat_over = True
            print("Yay, you have beaten the Goblin")
            player["gold"] += random.randrange(1,11)
            print(f"you now have {player['gold']} gold")
            player["where"] = "trail"
        if player["health"] <= 0:
            combat_over = True
            print("sad, You died")
            exit()
    



# forest continue random
def forest_continue():
    hold = random.randrange(1, 3)
    if hold == 1:
        ()
    elif hold == 2:
        player["where"] = "goblin"

    
    
    
# def ? input def
def new_input_inputs():
    print(".")
    sleep(0.1)
    print("Here are a list of inputs for you to execute:")
    sleep(0.1)
    print("'c' or 'continue' to continue on you journy")
    sleep(0.1)
    print("'i' or 'invintory' to open your invintory")
    sleep(0.1)
    print("'l' or 'look' to investigate the surrounding area")
    sleep(0.1)
    print("'s' or 'sleep' to take a long rest")
    sleep(0.1)
    print("'p' or 'player' to see player info")



# input def
def new_input_def():
    new_input_done = False
    while new_input_done == False:
        new_input_done = True
        print(".")
        sleep(0.1)
        print("if in doubt type '?'")
        new_input = input("input: ").lower()
        if new_input == "?":
            new_input_inputs()
        elif new_input == "c" or new_input == "continue":
            forest_continue()
        elif new_input == "i" or new_input == "invintory":
            invintory()
        elif new_input == "p" or new_input == "player":
            print(player)
        else:
            new_input_done = False
            print("Invalid Input")


# forest area
def new_forest_area():
    while player["area"] == "forest":
        if player["where"] == "trail":
            hold = random.randrange(1, 4)
            if hold == 1:
                print("Pine trees continue to envolop you on ether side.")
            elif hold == 2:
                print("Pine and fir trees still continue to grow thick around you.")
            elif hold == 3:
                print("not much changes among the trees as you continue")
            new_input_def()
        elif player["where"] == "goblin":
            print("as you stop in a clearing srounded by pines your spine runns cold as you realise your not alone. ")
            goblin_combat()

    
# program start
if player["area"] == "forest":
    new_forest_area()
