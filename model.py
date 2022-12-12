from random import randint

score = 500
user_num = 6
win_num = 6
bet_points = 1

def roll():
    return randint(1, 7)

def check(user_num):
    global score
    global win_num
    win_num = roll()

    if user_num == win_num:
        score += bet_points*3
        return True
    else:
        score -= bet_points
        return False

if __name__ == "__main__":
    i = 0
    while i < 10:
        print(check(user_num))
        print(score)
        i += 1