import model as m
import view as v


def user_roll():
    try:
        m.bet_points = int(input('Your bet (points): '))
        m.user_num = int(input('On (dice number): '))
    except ValueError:
        return 'Not a number'

    if m.bet_points > m.score or m.user_num not in range(1, 6):
        return 'Invalid bet'

    return m.check(m.user_num)

def confirm():
    if input('Again? (q-exit) '):
        return False
    return True

def play():
    while m.score > 0:
        roll_it = user_roll()
        if isinstance(roll_it, bool):
            if roll_it:
                v.show_res(True, m.score)
            else:
                v.show_res(False, m.score)
        else:
            print(roll_it)
            
        if not confirm():
            return
    v.exit(True)

if __name__ == '__main__':
    v.start()
    play()
    v.exit()