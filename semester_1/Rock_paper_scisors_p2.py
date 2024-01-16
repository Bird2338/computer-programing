p1_input = input('(Player One) Rock, Paper, scissors:')
p2_input = input('(Player Two) Rock, Paper, scissors:')

# if (p1_input == "Rock" or p1_input == "rock") and (p2_input == "Paper" or p2_input == "paper"):
#     print('Player Two Wins')

if p1_input == 'rock' or p1_input == 'Rock':
    p1_input = 1
elif p1_input == 'paper' or p1_input == 'Paper':
    p1_input = 2
elif p1_input == 'scissors' or p1_input == 'Scissors':
    p1_input = 3
else:
    print('ERROR')
    
if p2_input == 'rock' or p2_input == 'Rock':
    p2_input = 1
elif p2_input == 'paper' or p2_input == 'Paper':
    p2_input = 2
elif p2_input == 'scissors' or p2_input == 'Scissors':
    p2_input = 3
else:
    print('ERROR')

if (p1_input > p2_input) or (p1_input == 1 and p2_input == 3):
    print('Player One Wins')
elif (p2_input > p1_input) or (p2_input == 1 and p1_input == 3):
    print('Player Two Wins')
else:
    print('ERROR')