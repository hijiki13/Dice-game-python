import tkinter as tk
import controller as c

# title of window
window = tk.Tk()
window.title('Play Dice')

# title inside window
start = tk.Label(text='Lets play!', fg="cyan", bg="grey8", width=50, height=2)
start.grid(row=0, columnspan=2, sticky='n', pady=(0, 10))

# bet input 1 (points)
lbl_bet_p = tk.Label(text='Your bet (points):', width=30)
ent_bet_p = tk.Entry(width=30)
lbl_bet_p.grid(row=1, columnspan=2, column=0, pady=(10, 0))
ent_bet_p.grid(row=2, columnspan=2, column=0, pady=(0, 10))

# bet input 2 (number)
lbl_bet_n = tk.Label(text='On (number):')
ent_bet_n = tk.Entry(width=30)
lbl_bet_n.grid(row=3, columnspan=2, column=0, pady=(10, 0))
ent_bet_n.grid(row=4, columnspan=2, column=0, pady=(0, 10))

# button and var for button wait
btn_pressed = tk.IntVar()
btn = tk.Button(text='Roll', fg='grey8', bg='cyan', width= 10, command=c.play)
btn.grid(row=9, column=0, columnspan=2, sticky='s', pady=(10, 5))

# Results
lbl_win = tk.Label(text='Number on dice: ', width=12)
lbl_win_num = tk.Label(text='', width=2)
lbl_res = tk.Label(text='')
lbl_score = tk.Label(text='Score: ', width=12)
lbl_score_val = tk.Label(text='', width=2)
lbl_score_val.bind('change')
lbl_msg = tk.Label(text='')
# display result
lbl_win.grid(row=5, column=0, sticky='e', pady=5)
lbl_win_num.grid(row=5, column=1, sticky='w', pady=5)
lbl_res.grid(row=6, column=0, columnspan=2, pady=5)
lbl_score.grid(row=7, column=0, sticky='e', pady=5)
lbl_score_val.grid(row=7, column=1, sticky='w', pady=5)
lbl_msg.grid(row=8, column=0, columnspan=2)

# for controller
def get_bet_p():
    return ent_bet_p.get()

def get_bet_n():
    return ent_bet_n.get()

def show_res(won, score):
    lbl_win_num['text'] = f'{c.m.win_num}'
    if won:
        lbl_res['text'] = '~~~~~~~~~~~~~~~~You Win!~~~~~~~~~~~~~~~~'
    else:
        lbl_res['text'] = '~~~~~~~~~~~~~~~~You Lose!~~~~~~~~~~~~~~~'
    lbl_score_val['text'] = f'{score}'

def show_msg(msg):
    lbl_msg['text'] = f'{msg}'
    lbl_msg.after(1500, empty_msg)

def empty_msg():
    lbl_msg['text'] = ''

def confirm():
    btn.wait_variable()

def start():
    window.mainloop()

def exit():
    btn.destroy()
    window.after(1500, window.destroy)