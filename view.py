import controller as c
from dice import dice, show_dice

def show_res(res, score):
    show_dice(*dice[c.m.win_num])
    if res:
        print(f'You win! Score: {score}')
    else:
        print(f'You lose! Score: {score}')

def start():
    print('Lets play! You have 500 points.')

def exit(forced = False):
    if forced:
        print('You have no points left.')
    else:
        print('Goodbye!')