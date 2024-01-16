num1_input = int(input('what is your first number?:'))
operation_input = input('what is your operation?:')
num2_input = int(input('what is your second number?:'))

if operation_input == '*':
    print(f'{num1_input} {operation_input} {num2_input} = {num1_input * num2_input}')
else:
    if operation_input == '/':
        print(f'{num1_input} {operation_input} {num2_input} = {num1_input / num2_input}')
    else:
        if operation_input == '+':
            print(f'{num1_input} {operation_input} {num2_input} = {num1_input + num2_input}')
        else:
            if operation_input == '-':
                print(f'{num1_input} {operation_input} {num2_input} = {num1_input - num2_input}')
            else:
                if operation_input == 'x':
                    print(f'{num1_input} {operation_input} {num2_input} = {num1_input * num2_input}')
                else:
                    print('Error')