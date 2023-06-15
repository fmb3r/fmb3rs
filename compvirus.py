#https://drive.google.com/drive/folders/1HkDuI3OQoNoT3sQjr8sj9Rx0WwnwKTaM?usp=share_link

from tkinter import *

window = Tk()
window.geometry('900x400')
window.title('LOTTERY')
window.config(bg = 'black')
window.resizable(width=False, height=False)


def on_close():
    text.config(text = 'Чтобы забрать выйгрыш необходимо внести 1000руб', font = ('Courier New', 18))
    window.protocol("WM_DELETE_WINDOW", on_close)

text = Label(text = 'ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!!!!!', fg = 'pink', bg = 'black', font = ('Courier New', 34))
text.place(x = 100, y = 100, width = 700, height = 100)

win = Button(text = 'ПОЛУЧИТЬ ВЫЙГРЫШ!', fg = 'white', bg = 'black', font = ('Courier New', 34), command = on_close)
win.place(x = 100, y = 200, width = 700, height = 100)

timer = Label(text = '6', fg = 'green', bg = 'black', font = ('Courier New', 34))

window.mainloop()