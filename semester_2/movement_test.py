lines = {
    'line_0': '------------------------------',
    'line_1': '------------------------------',
    'line_2': '------------------------------',
    'line_3': '------------------------------',
    'line_4': '------------------------------',
    'line_5': '------------------------------',
    'line_6': '------------------------------',
    'line_7': '------------------------------',
    'line_8': '------------------------------',
    'line_9': '------------------------------',
}

def print_lines():
    print(lines['line_0'])
    print(lines['line_1'])
    print(lines['line_2'])
    print(lines['line_3'])
    print(lines['line_4'])
    print(lines['line_5'])
    print(lines['line_6'])
    print(lines['line_7'])
    print(lines['line_8'])
    print(lines['line_9'])

player = (0, 0)

def player_load():

    if player[0] == 0:
        line_hold = lines['line_0']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_0'] = ''.join(line_hold_split)

    elif player[0] == 1:
        line_hold = lines['line_1']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_1'] = ''.join(line_hold_split)

    elif player[0] == 2:
        line_hold = lines['line_2']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_2'] = ''.join(line_hold_split)

    elif player[0] == 3:
        line_hold = lines['line_3']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_3'] = ''.join(line_hold_split)

    elif player[0] == 4:
        line_hold = lines['line_4']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_4'] = ''.join(line_hold_split)

    elif player[0] == 5:
        line_hold = lines['line_5']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_5'] = ''.join(line_hold_split)

    elif player[0] == 6:
        line_hold = lines['line_6']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_6'] = ''.join(line_hold_split)

    elif player[0] == 7:
        line_hold = lines['line_7']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_7'] = ''.join(line_hold_split)

    elif player[0] == 8:
        line_hold = lines['line_8']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_8'] = ''.join(line_hold_split)

    elif player[0] == 9:
        line_hold = lines['line_9']
        line_hold_split = [*line_hold]
        num_hold = int(player[1])
        line_hold_split[num_hold] = '0'
        lines['line_9'] = ''.join(line_hold_split)
    
def player_move():

    move_input = input()

    global player

    if move_input == 'w':

        if player[0] == 0:
            
            line_hold = lines['line_9']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_0']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_0'] = ''.join(line_hold_split)
                player = (9, player[1])

        elif player[0] == 1:
            
            line_hold = lines['line_0']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_1']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_1'] = ''.join(line_hold_split)
                player = (0, player[1])
        
        elif player[0] == 2:
            
            line_hold = lines['line_1']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_2']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_2'] = ''.join(line_hold_split)
                player = (1, player[1])

        elif player[0] == 3:
            
            line_hold = lines['line_2']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_3']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_3'] = ''.join(line_hold_split)
                player = (2, player[1])

        elif player[0] == 4:
            
            line_hold = lines['line_3']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_4']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_4'] = ''.join(line_hold_split)
                player = (3, player[1])
        
        elif player[0] == 5:
            
            line_hold = lines['line_4']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_5']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_5'] = ''.join(line_hold_split)
                player = (4, player[1])

        elif player[0] == 6:
            
            line_hold = lines['line_5']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_6']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_6'] = ''.join(line_hold_split)
                player = (5, player[1])

        elif player[0] == 7:
            
            line_hold = lines['line_6']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_7']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_7'] = ''.join(line_hold_split)
                player = (6, player[1])

        elif player[0] == 8:
            
            line_hold = lines['line_7']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_8']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_8'] = ''.join(line_hold_split)
                player = (7, player[1])

        elif player[0] == 9:
            
            line_hold = lines['line_8']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_9']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_9'] = ''.join(line_hold_split)
                player = (8, player[1])

    if  move_input == 's':

        if player[0] == 0:
            
            line_hold = lines['line_1']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_0']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_0'] = ''.join(line_hold_split)
                player = (1, player[1])

        elif player[0] == 1:
            
            line_hold = lines['line_2']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_1']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_1'] = ''.join(line_hold_split)
                player = (2, player[1])
        
        elif player[0] == 2:
            
            line_hold = lines['line_3']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_2']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_2'] = ''.join(line_hold_split)
                player = (3, player[1])

        elif player[0] == 3:
            
            line_hold = lines['line_4']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_3']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_3'] = ''.join(line_hold_split)
                player = (4, player[1])

        elif player[0] == 4:
            
            line_hold = lines['line_5']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_4']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_4'] = ''.join(line_hold_split)
                player = (5, player[1])
        
        elif player[0] == 5:
            
            line_hold = lines['line_6']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_5']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_5'] = ''.join(line_hold_split)
                player = (6, player[1])

        elif player[0] == 6:
            
            line_hold = lines['line_7']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_6']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_6'] = ''.join(line_hold_split)
                player = (7, player[1])

        elif player[0] == 7:
            
            line_hold = lines['line_8']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_7']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_7'] = ''.join(line_hold_split)
                player = (8, player[1])

        elif player[0] == 8:
            
            line_hold = lines['line_9']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_8']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_8'] = ''.join(line_hold_split)
                player = (9, player[1])

        elif player[0] == 9:
            
            line_hold = lines['line_0']
            line_hold_split = [*line_hold]
            num_hold = player[1]

            if line_hold_split[num_hold] == '-':
                line_hold = lines['line_9']
                line_hold_split = [*line_hold]
                num_hold = int(player[1])
                line_hold_split[num_hold] = '-'
                lines['line_9'] = ''.join(line_hold_split)
                player = (0, player[1])

    if move_input == 'a':

        if player[0] == 0:

            if player[1] == 0:

                line_hold = lines['line_0']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_0']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_0'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_0']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_0']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_0'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
        
        if player[0] == 1:

            if player[1] == 0:

                line_hold = lines['line_1']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_1']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_1'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_1']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_1']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_1'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
                    
        if player[0] == 2:

            if player[1] == 0:

                line_hold = lines['line_2']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_2']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_2'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_2']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_2']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_2'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
                    
        if player[0] == 3:

            if player[1] == 0:

                line_hold = lines['line_3']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_3']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_3'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_3']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_3']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_3'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
                    
        if player[0] == 4:

            if player[1] == 0:

                line_hold = lines['line_4']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_4']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_4'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_4']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_4']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_4'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
                    
        if player[0] == 5:

            if player[1] == 0:

                line_hold = lines['line_5']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_5']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_5'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_5']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_5']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_5'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
                    
        if player[0] == 6:

            if player[1] == 0:

                line_hold = lines['line_6']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_6']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_6'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_6']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_6']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_6'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
                    
        if player[0] == 7:

            if player[1] == 0:

                line_hold = lines['line_7']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_7']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_7'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_7']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_7']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_7'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
                    
        if player[0] == 8:

            if player[1] == 0:

                line_hold = lines['line_8']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_8']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_8'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_8']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_8']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_8'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
                    
        if player[0] == 9:

            if player[1] == 0:

                line_hold = lines['line_9']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[29] == '-':
                    line_hold = lines['line_9']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_9'] = ''.join(line_hold_split)
                    player = (player[0], 29)
            
            else:

                line_hold = lines['line_9']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold - 1] == '-':
                    line_hold = lines['line_9']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_9'] = ''.join(line_hold_split)
                    player = (player[0], num_hold - 1)
                    
    if move_input == 'd':
        
        if player[0] == 0:

            if player[1] == 29:

                line_hold = lines['line_0']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_0']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_0'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_0']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_0']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_0'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)
        
        if player[0] == 1:

            if player[1] == 29:

                line_hold = lines['line_1']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_1']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_1'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_1']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_1']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_1'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)
                    
        if player[0] == 2:

            if player[1] == 29:

                line_hold = lines['line_2']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_2']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_2'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_2']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_2']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_2'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)
                    
        if player[0] == 3:

            if player[1] == 29:

                line_hold = lines['line_3']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_3']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_3'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_3']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_3']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_3'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)
                    
        if player[0] == 4:

            if player[1] == 29:

                line_hold = lines['line_4']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_4']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_4'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_4']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_4']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_4'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)
                    
        if player[0] == 5:

            if player[1] == 29:

                line_hold = lines['line_5']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_5']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_5'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_5']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_5']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_5'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)
                    
        if player[0] == 6:

            if player[1] == 29:

                line_hold = lines['line_6']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_6']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_6'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_6']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_6']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_6'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)

        if player[0] == 7:

            if player[1] == 29:

                line_hold = lines['line_7']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_7']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_7'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_7']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_7']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_7'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)
                    
        if player[0] == 8:

            if player[1] == 29:

                line_hold = lines['line_8']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_8']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_8'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_8']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_8']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_8'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)
                    
        if player[0] == 9:

            if player[1] == 29:

                line_hold = lines['line_9']
                line_hold_split = [*line_hold]
                num_hold = player[0]

                if line_hold_split[0] == '-':
                    line_hold = lines['line_9']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[0])
                    line_hold_split[num_hold] = '-'
                    lines['line_9'] = ''.join(line_hold_split)
                    player = (player[0], 0)
            
            else:

                line_hold = lines['line_9']
                line_hold_split = [*line_hold]
                num_hold = player[1]

                if line_hold_split[num_hold + 1] == '-':
                    line_hold = lines['line_9']
                    line_hold_split = [*line_hold]
                    num_hold = int(player[1])
                    line_hold_split[num_hold] = '-'
                    lines['line_9'] = ''.join(line_hold_split)
                    player = (player[0], num_hold + 1)
                    
        






run = 0

while run == 0:
    player_load()
    print_lines()
    player_move()
