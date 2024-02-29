# MAIN IMPORT
from os import system
try:
    from pynput import keyboard

except:
    system('pip install pynput')
    
try:
    from colorama import Fore, Style

except:
    system('pip install colorama')        

from os import name
from os.path import dirname, abspath, join
from copy import deepcopy
from random import randint, choice
from time import time, sleep
import json
from pynput import keyboard
from colorama import Fore, Style


# END MAIN IMPORT

# MAIN VARIABLES
command = 'cls' if name == 'nt' else 'clear'
script_directory = dirname(abspath(__file__))
json_directory = join(script_directory, 'config.json')

# END MAIN VARIABLES

# MAIN GAME FUNCTIONS

def move(board, direction):
    if direction == 'l':
        for i in range(len(board)):
            for j in range(1, len(board)):
                while j > 0:
                    if board[i][j-1] == 0:
                        board[i][j-1], board[i][j] = board[i][j], board[i][j-1]

                    j -= 1    

    if direction == 'r':
        for i in range(len(board)):
            for j in range(-2, (len(board) * -1) - 1, -1):
                while j < -1:
                    if board[i][j+1] == 0:
                        board[i][j+1], board[i][j] = board[i][j], board[i][j+1]

                    j += 1    
    
    if direction == 'u':
        for i in range(len(board[0])):
            for j in range(1, len(board)):
                while j > 0:
                    if board[j-1][i] == 0:
                        board[j-1][i], board[j][i] = board[j][i], board[j-1][i]

                    j -= 1   

    if direction == 'd':
        for i in range(len(board[0])):
            for j in range(-2, (len(board) * -1) - 1, -1):
                while j < -1:
                    if board[j+1][i] == 0:
                        board[j+1][i], board[j][i] = board[j][i], board[j+1][i]

                    j += 1    
   
    return board

def merge(board, direction, value):
    if direction == 'l':
        for i in range(len(board)):
            for j in range(1, len(board)):
                while j > 0:
                    if board[i][j-1] == board[i][j] and board[i][j-1] != 0:
                        board[i][j-1] *= value
                        board[i][j] = 0

                    j -= 1    

    if direction == 'r':
        for i in range(len(board)):
            for j in range(-2, (len(board) * -1) - 1, -1):
                while j < -1:
                    if board[i][j+1] == board[i][j] and board[i][j+1]!= 0:
                        board[i][j+1] *= value
                        board[i][j] = 0

                    j += 1    

    if direction == 'u':
        for i in range(len(board[0])):
            for j in range(1, len(board)):
                while j > 0:
                    if board[j-1][i] == board[j][i] and board[j-1][i] != 0:
                        board[j-1][i] *= value
                        board[j][i] = 0

                    j -= 1   

    if direction == 'd':
        for i in range(len(board[0])):
            for j in range(-2, (len(board) * -1) - 1, -1):
                while j < -1:
                    if board[j+1][i] == board[j][i] and board[j][i] != 0:
                        board[j+1][i] *= value
                        board[j][i] = 0

                    j += 1                                              
                        
    return board      

def check_empty(board):
    empty = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                empty.append((i, j))

    return empty   

def add_value(board, empty, value):
    if empty:
        value = value if randint(1, 100) >= 90 else value**2
        coor = choice(empty)
        board[coor[0]][coor[1]] = value

    return board        

def game_over(board, old_board, empty, value):
    if empty:
        return False
    
    temp = deepcopy(board)
    temp = move(merge(move(board, 'l'), 'l', value), 'l')
    if temp != old_board:
        return False
    
    temp = deepcopy(board)
    temp = move(merge(move(board, 'r'), 'r', value), 'r')
    if temp != old_board:
        return False
    
    temp = deepcopy(board)
    temp = move(merge(move(board, 'u'), 'u', value), 'u')
    if temp != old_board:
        return False
    
    temp = deepcopy(board)
    temp = move(merge(move(board, 'd'), 'd', value), 'd')
    if temp != old_board:
        return False
    
    return True

def find_max(board):
    m = 0
    for line in board:
        m = max(m, max(line))

    return len(str(m)) 

def create_board(height, width, value):
    board = []
    for i in range(height):
        board.append([0] * width)

    board[0][0] = value      
    return board   

# END MAIN GAME FUNCTIONS

# MAIN GAME GRAPHICS
def print_board(board, values):
    m = find_max(board)
    for line in board:
        print('|', end="")
        for value in line:
            if value in values.keys():
                print(values[value] + ' '*(m-len(str(value))) + '|', end="")

            elif value == 0:
                print(' '*m + '|', end="")

            else:
                print(f"{Fore.RED}{value}{Style.RESET_ALL}{' '*(m-len(str(value))) + '|'}", end="")        

        print()   

def get_value_templates(value):
    values = {
        value: f'{Fore.WHITE}2{Style.RESET_ALL}',
        value**2: f'{Fore.LIGHTYELLOW_EX}4{Style.RESET_ALL}',
        value**3: f'{Fore.LIGHTGREEN_EX}8{Style.RESET_ALL}',
        value**4: f'{Fore.GREEN}16{Style.RESET_ALL}',
        value**5: f'{Fore.YELLOW}32{Style.RESET_ALL}',
        value**6: f'{Fore.CYAN}64{Style.RESET_ALL}',
        value**7: f'{Fore.BLUE}128{Style.RESET_ALL}',
        value**8: f'{Fore.LIGHTMAGENTA_EX}256{Style.RESET_ALL}',
        value**9: f'{Fore.MAGENTA}512{Style.RESET_ALL}',
        value**10: f'{Fore.LIGHTRED_EX}1024{Style.RESET_ALL}',
        value**11: f'{Fore.RED}2048{Style.RESET_ALL}',
    }

    return values

# END MAIN GAME GRAPHICS

# MAIN GAME SETTINGS
def settings(value, height, width, delay, form):
    while True:
        system(command)
        form_text = 'Keyboard' if form == 1 else 'Console'
        choice = input(f'Settings\n\n1.Change value: {value}\n2.Change height: {height}\n3.Change width: {width}\n4.Change delay(keyboard special): {delay}s\n5.Change form: {form_text}\n6.Exit\n: ').strip()
        if choice == '1':
            while True:
                system(command)
                choice = input(f'Settings\n\nPrevious value: {value}\nNew value: ').strip()
                if choice:
                    if choice.isdigit():
                        if int(choice) > 1:
                            value = int(choice)
                            break

                        else:
                            print('\nValue must be greater than 1')
                            input('Continue...')

                    else:
                        print('\nValue must be a whole number')
                        input('Continue...')

                else:
                    print('\nValue must be entered')
                    input('Continue...')

        elif choice == '2':
            while True:
                system(command)
                choice = input(f'Settings\n\nPrevious height: {height}\nNew height: ').strip()
                if choice:
                    if choice.isdigit():
                        if int(choice) > 1:
                            height = int(choice)
                            break

                        else:
                            print('\nHeight must be greater than 1')
                            input('Continue...')

                    else:
                        print('\nHeight must be a whole number')
                        input('Continue...')

                else:
                    print('\nHeight must be entered')
                    input('Continue...')

        elif choice == '3':
            while True:
                system(command)
                choice = input(f'Settings\n\nPrevious width: {width}\nNew width: ').strip()
                if choice:
                    if choice.isdigit():
                        if int(choice) > 1:
                            width = int(choice)
                            break

                        else:
                            print('\nWidth must be greater than 1')
                            input('Continue...')

                    else:
                        print('\nWidth must be a whole number')
                        input('Continue...')

                else:
                    print('\nWidth must be entered')
                    input('Continue...')

        elif choice == '4':
            while True:
                system(command)
                choice = input(f'Settings\n\nPrevious delay: {delay}s\nNew delay(in seconds): ').strip()
                if choice:
                    try:
                        choice = float(choice)
                        if choice > 0.2:
                            delay = choice
                            if choice < 0.5:
                                print(f'\n{Fore.RED}Delay under 0.5 seconds may cause bugs{Style.RESET_ALL}')
                                input('Continue...')
                            break

                        else:
                            print('\nDelay must be greater than 0.2')
                            input('Continue...')

                    except:
                        print('\nDelay must be a number')
                        input('Continue...')

                else:
                    print('\nDelay must be entered')
                    input('Continue...')

        elif choice == '5':
            while True:
                system(command)
                choice = input(f'Settings\n\nPrevious form: {form_text}\nNew form(Console: 0, Keyboard: 1): ').strip()
                if choice:
                    if choice.isdigit():
                        if int(choice) in [0, 1]:
                            form = int(choice)
                            break

                        else:
                            print('\nInvalid number for the form')
                            input('Continue...')

                    else:
                        print('\nForm must be entered as a whole number')
                        input('Continue...')

                else:
                    print('\nForm must be entered')
                    input('Continue...')

        elif choice == '6':
            break

        else:
            print(f'\nNo such option')
            input('Continue...')

    return value, height, width, delay, form

# END MAIN GAME SETTINGS

# MAIN GAME START
def start_game(value, height, width):
    values = get_value_templates(value)
    board = create_board(height, width, value)

    while True:
        system(command)
        print_board(board, values)
        direction = input('\n\nu(up), d(down), l(left), r(right): ').strip().lower()
        if direction in ['u', 'd', 'l', 'r']:
            old_board = deepcopy(board)
            board = move(board, direction)
            board = merge(board, direction, value)
            board = move(board, direction)
            empty = check_empty(board)

            if board != old_board:
                board = add_value(board, empty, value)

            if game_over(deepcopy(board), deepcopy(board), empty, value):
                break

        else:
            print(f'\nInvalid direction')
            input('Continue...')
        
    system(command)        
    print_board(board, values)
    print(f'\n\n{Fore.RED}GAME OVER!!!{Style.RESET_ALL}')
    sleep(2)
    input('\nContinue...')

## KEYBOARD    
keys = {
    keyboard.Key.up: 'u',
    keyboard.Key.down: 'd',
    keyboard.Key.left: 'l',
    keyboard.Key.right: 'r',
}

def on_press(key, value, board, listener):
    if key in keys.keys():
        direction = keys[key]
        old_board = deepcopy(board)
        new_board = move(deepcopy(board), direction)
        new_board = merge(deepcopy(new_board), direction, value)
        new_board = move(deepcopy(new_board), direction)
        empty = check_empty(new_board)

        if new_board != old_board:
            new_board = add_value(new_board, empty, value)

        if game_over(new_board, deepcopy(new_board), empty, value):
            listener.stop()

    else:
        return board
     
    return new_board

def start_game_keyboard(value, height, width, delay):
    values = get_value_templates(value)
    board = create_board(height, width, value)

    last_key_time = 0

    def on_press_wrapper(key):
        nonlocal board, last_key_time, delay

        current_time = time()
        if current_time - last_key_time < delay:
            return
        
        last_key_time = current_time

        board = on_press(key, value, board, listener)
        system(command)
        print_board(board, values)

    with keyboard.Listener(on_press=on_press_wrapper) as listener:
        system(command)
        print_board(board, values)
        print('\n\nPress arrow keys to control:')
        listener.join()

    system(command)        
    print_board(board, values)
    print(f'\n\n{Fore.RED}GAME OVER!!!{Style.RESET_ALL}')
    sleep(2)
    input('\nContinue...')

## END KEYBOARD    

# END MAIN GAME START

# config.json CONTROL
def save(value, height, width, delay, form):
    temp = {
        'values' : {
            'value' : value,
            'height' : height,
            'width' : width,
            'delay' : delay,
            'form' : form
        }
    }
    
    with open(json_directory, 'w') as f:
        f.write(json.dumps(temp))

def load():
    try:
        with open(json_directory, 'r') as f:
            temp = json.loads(f.read())
            value = temp['values']['value']
            height = temp['values']['height']
            width = temp['values']['width']
            delay = temp['values']['delay']
            form = temp['values']['form']

            if int(value) < 1:
                raise ValueError('Value must be bigger than 1')
            
            if int(height) < 1:
                raise ValueError('Height must be bigger than 1')
            
            if int(width) < 1:
                raise ValueError('Width must be bigger than 1')
            
            if float(delay) < 0.2:
                raise ValueError('Delay must be bigger than 0.2')
            
            if int(form) not in [0, 1]:
                raise ValueError('Form must be 0 or 1')
    
    except Exception as e:
        value = 2
        height = 4
        width = 4
        delay = 0.4
        form = 1
        print(f'Erorr ocurred: {e}')
        input('Continue...')

    return value, height, width, delay, form

# END config.json CONTROL

# MAIN CONTROL
def main():
    value, height, width, delay, form = load()
    while True:
        system(command)
        choice = input(f'Console 2048\n\n1.Start\n2.Settings\n3.Exit\n: ').strip()
        if choice == '1':
            if form:
                start_game_keyboard(value, height, width, delay)

            else:
                start_game(value, height, width)

        elif choice == '2':
            value, height, width, delay, form = settings(value, height, width, delay, form)
            save(value, height, width, delay, form)

        elif choice == '3':
            break

        else:
            print(f'\nNo such option')
            input('Continue...')            

main()    
