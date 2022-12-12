import controller as c
from dice import dice, show_dice

def get_bet_p():
    return input('Your bet (points): ')

def get_bet_n():
    return input('On (dice number): ')

def show_msg(msg: str):
    print(msg)

def show_res(res, score):
    show_dice(*dice[c.m.win_num])
    if res:
        print(f'You win! Score: {score}')
    else:
        print(f'You lose! Score: {score}')

def confirm():
    if input('Again? (q-exit) '):
        return False
    return True

def start():
    print('Lets play! You have 500 points.')
    print()
    c.play()

def exit():
    print('Goodbye!')