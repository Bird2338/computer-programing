lines = {
    'line_0': '111111111111111111111111111111',
    'line_1': '110000000000000000000000000011',
    'line_2': '110000000000000000000000000011',
    'line_3': '110000000000000000000000000011',
    'line_4': '110000000000000000000000000011',
    'line_5': '110000000000000000000000000011',
    'line_6': '110000000000000000000000000011',
    'line_7': '110000000000000000000000000011',
    'line_8': '110000000000000000000000000011',
    'line_9': '111111111111111111111111111111',
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

player = (0, 9)

def player_load():
    if player[0] == 0:
        line_hold = lines['line_0']
        num_hold = player[1]
        line_hold[num_hold] = 'x'
        print(line_hold)
