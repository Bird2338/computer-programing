# Inports and basic variables
race_info_true = False
race_picked = False
global no_done
no_done = False
global is_stats_done
is_stats_done = False
ayok = False
stat_input = 0
global stat_points
stat_points = 1
global str_
global dex_
global con_
global int_
global wis_
global cha_
str_ = 10
dex_ = 10
con_ = 10
int_ = 10
wis_ = 10
cha_ = 10
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
time.sleep(1)
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
        print("- +1 to every stat")
        time.sleep(0.1)
        print("speed - 30 feet")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "dwarf":
        print(".")
        time.sleep(1)
        print("- +2 to Constitution")
        time.sleep(0.1)
        print("- Darkvision")
        time.sleep(0.1)
        print("Speed - 25 feet")
        time.sleep(0.1)
        print("- Poison Resist")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "gnome":
        print(".")
        time.sleep(1)
        print("- +2 to Intelligence")
        time.sleep(0.1)
        print("- Darkvision")
        time.sleep(0.1)
        print("Speed - 25")
        time.sleep(0.1)
        print("- Mind Magic Resist")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "goblin":
        print(".")
        time.sleep(1)
        print("- +2 to Dexterity and +1 to Constitution")
        time.sleep(0.1)
        print("- Darkvision")
        time.sleep(0.1)
        print("Speed - 30")
        time.sleep(0.1)
        print("- Charm resist")
        time.sleep(0.1)
        print("- Disengage or Hide action as a bonus action")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "halfling":
        print(".")
        time.sleep(1)
        print("- +2 to Dexterity")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "elf":
        print(".")
        time.sleep(1)
        print("- +2 to Dexterity")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "half-elf":
        print(".")
        time.sleep(1)
        print("- +2 to Charisma and 2 Ability Score increases")
        time.sleep(0.1)
        print("type 'back' to go back")
        race_stat_view()
    elif race_info_input == "tiefling":
        print(".")
        time.sleep(1)
        print("- +2 to Charisma and +1 to Intelligence")
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
    time.sleep(0.1)
    print("Races:")
    time.sleep(0.1)
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
    time.sleep(0.1)
    print("Type a 'race' to see it's stats or type 'back'")
    race_info_menu_input()
    
# race picking while loop
while race_picked == False:
    print(".")
    time.sleep(1)
    print(f"What will {player_name}'s race be?")
    time.sleep(0.1)
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
# #$&$%^^*$%#$@#%@^$%&^*&(%**^%#&$^@#%!^@&#%^*$&(%*^)(&(%^*$%#&$@^#@^#U$%*(&^)&(%*^$#%@^#!%$^@&#%*&$(*%)(*&(%^*$#%@#%^@%$&%*$&^(%*&%^*$%&#$@^#!%$@^&#^*$&%(*^&(%^*$%#&$@^#)))))))))motify playabilaty
# Picking stats start
print(".")
time.sleep(1)
print("You have 27 points to spend on stats")
time.sleep(0.1)
print("The lowest your stats can go is 8 and the highest is 15")
time.sleep(0.1)
print("your stats start at 8")
time.sleep(0.1)
print("type '+' or '-' followed by the first three letters of a stat")
time.sleep(0.1)
print("removing a point will give you that point back to be spent somewhere else")

# stat pick input loop
def stat_pick_input():
    global str_
    global dex_
    global con_
    global int_
    global wis_
    global cha_
    global stat_points
    stat_input = input().lower()
    if (stat_input == "+str") and (int(str_ ) < 15) and (stat_points != 0):
        temp_var = str_
        str_ = temp_var + 1
        point_hold = stat_points
        stat_points = point_hold - 1
    elif (stat_input == "+dex") and ((dex_ ) < 15) and (stat_points != 0):
        temp_var = dex_
        dex_ = temp_var + 1
        point_hold = stat_points
        stat_points = point_hold - 1
    elif (stat_input == "+con") and (int(con_ ) < 15) and (stat_points != 0):
        temp_var = con_
        con_ = temp_var + 1
        point_hold = stat_points
        stat_points = point_hold - 1
    elif (stat_input == "+int") and (int(int_ ) < 15) and (stat_points != 0):
        temp_var = int_
        int_ = temp_var + 1
        point_hold = stat_points
        stat_points = point_hold - 1
    elif (stat_input == "+wis") and (int(wis_ ) < 15) and (stat_points != 0):
        temp_var = wis_
        wis_ = temp_var + 1
        point_hold = stat_points
        stat_points = point_hold - 1
    elif (stat_input == "+cha") and (int(cha_ ) < 15) and (stat_points != 0):
        temp_var = cha_
        cha_ = temp_var + 1
        point_hold = stat_points
        stat_points = point_hold - 1
    elif (stat_input == "-str") and (int(str_ ) > 8):
        temp_var = str_
        str_ = temp_var - 1
        point_hold = stat_points
        stat_points = point_hold + 1
    elif (stat_input == "-dex") and (int(dex_ ) > 8):
        temp_var = dex_
        dex_ = temp_var - 1
        point_hold = stat_points
        stat_points = point_hold + 1
    elif (stat_input == "-con") and (int(con_ ) > 8):
        temp_var = con_
        con_ = temp_var - 1
        point_hold = stat_points
        stat_points = point_hold + 1
    elif (stat_input == "-int") and (int(int_ ) > 8):
        temp_var = int_
        int_ = temp_var - 1
        point_hold = stat_points
        stat_points = point_hold + 1
    elif (stat_input == "-wis") and (int(wis_ ) > 8):
        temp_var = wis_
        wis_ = temp_var - 1
        point_hold = stat_points
        stat_points = point_hold + 1
    elif (stat_input == "-cha") and (int(cha_ ) > 8):
        temp_var = cha_
        cha_ = temp_var - 1
        point_hold = stat_points
        stat_points = point_hold + 1
    else:
        print("Invalid Input")
        stat_pick_input()

# stat points are 0, continue loop
def stat_is_0():
    stat_continue_input = input().lower()
    if stat_continue_input == "y":
        global is_stats_done
        is_stats_done = True
    elif stat_continue_input == "n":
        global no_done
        no_done = True
    else:
        stat_is_0

# Picking stats loop
while is_stats_done == False:
    print(".")
    time.sleep(1)
    print("stats")
    time.sleep(0.1)
    print(f"{str_} Strength")
    time.sleep(0.1)
    print(f"{dex_} Dexterity")
    time.sleep(0.1)
    print(f"{con_} Constitution")
    time.sleep(0.1)
    print(f"{int_} Intelligence")
    time.sleep(0.1)
    print(f"{wis_} Wisdom")
    time.sleep(0.1)
    print(f"{cha_} Charisma")
    time.sleep(0.1)
    print(f"You have {stat_points} points left")
    stat_pick_input()
    if stat_points == 0:
        print(".")
        time.sleep(1)
        print("stats")
        time.sleep(0.1)
        print(f"{str_} Strength")
        time.sleep(0.1)
        print(f"{dex_} Dexterity")
        time.sleep(0.1)
        print(f"{con_} Constitution")
        time.sleep(0.1)
        print(f"{int_} Intelligence")
        time.sleep(0.1)
        print(f"{wis_} Wisdom")
        time.sleep(0.1)
        print(f"{cha_} Charisma")
        time.sleep(0.1)
        print("you are out of points, are you done picking stats? y/n")
        stat_is_0()



# --------------------Race stat increases--------------------
# #$&$%^^*$%#$@#%@^$%&^*&(%**^%#&$^@#%!^@&#%^*$&(%*^)(&(%^*$%#&$@^#@^#U$%*(&^)&(%*^$#%@^#!%$^@&#%*&$(*%)(*&(%^*$#%@#%^@%$&%*$&^(%*&%^*$%&#$@^#!%$@^&#^*$&%(*^&(%^*$%#&$@^#)))))))))motify playabilaty
# ability score increase
def ability_score_increase():
    global str_
    global dex_
    global con_
    global int_
    global wis_
    global cha_
    print(".")
    time.sleep(1)
    print("abiltiy score increase")
    time.sleep(0.1)
    print("Type the first three letters of the ability you wish to increase by one")
    time.sleep(1)
    print(".")
    time.sleep(0.1)
    print(f"{str_} Strength")
    time.sleep(0.1)
    print(f"{dex_} Dexterity")
    time.sleep(0.1)
    print(f"{con_} Constitution")
    time.sleep(0.1)
    print(f"{int_} Intelligence")
    time.sleep(0.1)
    print(f"{wis_} Wisdom")
    time.sleep(0.1)
    print(f"{cha_} Charisma")
    time.sleep(0.1)
    ability_score_increase_input = input().lower()
    if ability_score_increase_input == "str":
        var_hold = str_
        str_ = var_hold + 1
    elif ability_score_increase_input == "dex":
        var_hold = dex_
        dex_ = var_hold + 1
    elif ability_score_increase_input == "con":
        var_hold = con_
        con_ = var_hold + 1
    elif ability_score_increase_input == "int":
        var_hold = int_
        int_ = var_hold + 1
    elif ability_score_increase_input == "wis":
        var_hold = wis_
        wis_ = var_hold + 1
    elif ability_score_increase_input == "cha":
        var_hold = cha_
        cha_ = var_hold + 1
    else:
        print("Invalid input")
        ability_score_increase_input()

if player_race == "Human":
    var_hold = str_
    str_ = var_hold + 1
    var_hold = dex_
    dex_ = var_hold + 1
    var_hold = con_
    con_ = var_hold + 1
    var_hold = int_
    int_ = var_hold + 1
    var_hold = wis_
    wis_ = var_hold + 1
    var_hold = cha_
    cha_ = var_hold + 1
elif player_race == "Dwarf":
    var_hold = con_
    con_ = var_hold + 2
elif player_race == "Gnome":
    var_hold = int_
    int_ = var_hold + 2
elif player_race == "Goblin":
    var_hold = dex_
    dex_ = var_hold + 2
    var_hold = con_
    con_ = var_hold + 1
elif player_race == "Halfling":
    var_hold = dex_
    dex_ = var_hold + 2
elif player_race == "Elf":
    var_hold = dex_
    dex_ = var_hold + 2
elif player_race == "Half-Elf":
    ability_score_increase()
    time.sleep(1)
    print(".")
    time.sleep(0.1)
    print(f"{str_} Strength")
    time.sleep(0.1)
    print(f"{dex_} Dexterity")
    time.sleep(0.1)
    print(f"{con_} Constitution")
    time.sleep(0.1)
    print(f"{int_} Intelligence")
    time.sleep(0.1)
    print(f"{wis_} Wisdom")
    time.sleep(0.1)
    print(f"{cha_} Charisma")
    time.sleep(0.1)
    ability_score_increase()
    time.sleep(1)
    print(".")
    time.sleep(0.1)
    print(f"{str_} Strength")
    time.sleep(0.1)
    print(f"{dex_} Dexterity")
    time.sleep(0.1)
    print(f"{con_} Constitution")
    time.sleep(0.1)
    print(f"{int_} Intelligence")
    time.sleep(0.1)
    print(f"{wis_} Wisdom")
    time.sleep(0.1)
    print(f"{cha_} Charisma")
    time.sleep(0.1)
    var_hold = cha_
    cha_ = var_hold + 2
elif player_race == "Tiefling":
    var_hold = cha_
    cha_ = var_hold + 2
    var_hold = int_
    int_ = var_hold + 1
print("your final starting stats are:")
time.sleep(1)
print(f"{str_} Strength")
time.sleep(0.1)
print(f"{dex_} Dexterity")
time.sleep(0.1)
print(f"{con_} Constitution")
time.sleep(0.1)
print(f"{int_} Intelligence")
time.sleep(0.1)
print(f"{wis_} Wisdom")
time.sleep(0.1)
print(f"{cha_} Charisma")
