side = 0
while side == 0:
    #Random Word Genorator
    #random_word Output is Lower Case
    y = 1
    import random
    x = (random.randint(1, 267751))

    with open('words.txt', 'r') as f:
        while y != x:
            f.readline()
            y = y + 1
        random_word_n = f.readline().lower().strip('n')


    # Testing Checks
    random_word = random_word_n[0:(len(random_word_n) - 1)]


    #turn base
    turns = (len(random_word)) + 5


    # Variables
    binary_input = []
    binary_output = [(i in binary_input) for i in range(len(random_word))]
    is_right = False

       
    # The Loop
    for g in range(turns):
        if is_right == True:
            break
        print(f'You Have {turns} Turns Left')
        h_check = False
        user_input = input('Guess A Word Or A Letter: ').lower()
        is_alpha_check = user_input.isalpha()
        if is_alpha_check == False:
            print('ERROR/ISALPHA/FALSE')
        elif len(user_input) == 1:
            # The Single Letter Path
            for z in range(len(random_word)):
                if user_input == random_word[z]:
                    binary_input.append(z)
                    binary_output = [(i in binary_input) for i in range(len(random_word))]
                    check = True
                    for x in binary_output:
                        if x != True:
                            check = False
                    if check == True:
                        is_right = True
                        print('You Win, Yay!')
        else:
            # The Word Path
            if user_input == random_word:
                print('You Win, Yay!')
                for new in range(len(random_word)):
                    binary_input.append(new)
                binary_output = [(i in binary_input) for i in range(len(random_word))]
                is_right = True
            else:
                print('Wrong')
        #Binary To Words
        binary_to_letters = []
        count = 0
        for h in (binary_output):

            if h == True:
                binary_to_letters.extend(random_word[count])
            else:
                binary_to_letters.extend('-')
            count = count + 1
        print(binary_to_letters)
        turns = turns - 1
    side2 = 0
    if is_right == False:
        print('Sad, You Lose')
        print(f'The Word Was {random_word}')
    
    p_input = input("Type 'Start' To Play Again: ").lower()
    if p_input == 'start':
        side = 0
    else:
        print('see ya later')
        side = 1
