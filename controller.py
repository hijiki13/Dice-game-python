# Реализовать любую программу (например игра "Кости") с помощью паттерна MVC у которой есть консольный вариант (view) и графический (view2). 
#--------------------------------------
import model as m
# import view as v
import view2 as v


def user_roll():
    try:
        m.bet_points = int(v.get_bet_p())
        m.user_num = int(v.get_bet_n())
    except ValueError:
        return 'Not a number'

    if m.bet_points > m.score or m.user_num not in range(1, 7):
        return 'Invalid bet'

    return m.check(m.user_num)

def play():
    while m.score > 0:
        roll_it = user_roll()
        if isinstance(roll_it, bool):
            if roll_it:
                v.show_res(True, m.score)
            else:
                v.show_res(False, m.score)
        else:
            v.show_msg(roll_it)
        
        try:
            if not v.confirm():
                return
        except:
            v.btn_pressed.set(1)
            v.confirm()

    v.show_msg('No more points!')
    v.exit()
    
if __name__ == '__main__':
    v.start()