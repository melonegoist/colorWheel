from tkinter import *
import sqlite3
from random import sample



sc = Tk()
sc.geometry("500x500")
sc.resizable(False, False)
sc.configure(bg = '#101010')
sc.title('color_wheel')

db = sqlite3.connect('db.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS colors (
    name TEXT
    )""")
db.commit()


def generator():
    global hex_code
    symbols = 'abcdef0123456789'
    hex_code = '#' + ''.join(sample(symbols, 6))
    display['bg'] = f'{hex_code}'
    lbl['text'] = f'{hex_code}'

def highlighter(event):
    lbl['fg'] = '#fb735a'

def off_highlighter(event):
    lbl['fg'] = '#e2a65d'

def copy():
    global hex_code
    sql.execute("""INSERT INTO colors(name)
    VALUES(?)""", (hex_code,))

    db.commit()

    

def move():
    sc2 = Toplevel()
    sc2.configure(bg = '#101010')
    sc2.title('color_list')
    sc2.geometry("150x200")
    # sc2.resizable(False, False)

    sql.execute("SELECT * FROM colors")
    db.commit()
    output = sql.fetchall()

    for i in range(0, len(output)):
        Label(sc2,
            text = f'{output[i][0]}',
            bg = '#101010',
            fg = 'white'

        ).place(x = 0, y = i*25)

        Canvas(sc2,
            bg = f'{output[i][0]}',
            highlightthickness = 0,
            width = 100,
            height = 25
        ).place(x = 50, y = i*25)
    


display = Canvas(
    width = 300,
    height = 200,
    bg = '#151010',
    highlightthickness= 0
)


display.place(x = 100, y = 100)


bttn = Button(
    text = 'Generate',
    bg = '#101010',
    fg = 'white',
    relief = 'flat',
    overrelief = 'solid',
    activebackground = '#101010',
    activeforeground = 'white',
    font = ('Times', 20),
    command = generator
)

lbl = Button(
    text = '',
    bg = '#101010',
    fg = '#e2a65d',
    font = ('Times', 20),
    relief = 'flat',
    overrelief = 'flat',
    activebackground = '#101010',
    activeforeground = 'white',
    command = copy
)

bttn_move = Button(
    text = 'list',
    bg = '#101010',
    fg = 'white',
    relief = 'flat',
    overrelief = 'solid',
    activebackground = '#101010',
    activeforeground = 'white',
    command = move
)

lbl.pack(side = 'bottom')

bttn.place(x = 185, y = 350)

bttn_move.place(x = 475, y = 475)



lbl.bind('<Enter>', highlighter)
lbl.bind('<Leave>', off_highlighter)
sc.mainloop()