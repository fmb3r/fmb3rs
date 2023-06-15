from tkinter import *
import random
from time import sleep

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points = 0
def check():
    global points
    b.place(x = random.randint(1, 550), y = random.randint(1, 350))
    points += 1
    label['text'] = points
    if points == 20:
        sleep(2)
        b.config(fg="black")


b = Button(text = 'нажми меня', font = ('Arial', 20), fg = 'red', command = check)
b.place(x = 200, y = 130)
label = Label(text = points, font = ('Arial', 20), fg = 'black')
label.place(x = 10, y = 10)

window.mainloop()