#https://drive.google.com/drive/folders/1HkDuI3OQoNoT3sQjr8sj9Rx0WwnwKTaM?usp=share_link

from tkinter import *

window = Tk()
window.geometry('900x300')
window.title('DANGEROUS')
window.config(bg = 'black')
window.resizable(width=False, height=False)


def on_close():
    print('a')
    if int(timer['text']) > 0:
        timer['text'] = int(timer['text']) - 1
        timer.place(x = 250, y = 25, width = 400, height = 100)
        window.after(1000, on_close)
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(str(width) + 'x' + str(height))
    photo = PhotoImage(file = 'skelet.gif')
    label = Label(image = photo, bg = 'black')
    label.image = photo
    label.place(width = width, height = height)

#window.protocol("WM_DELETE_WINDOW", on_close)


text = Label(text = 'ВАШ КОМПЬЮТЕР ЗАРАЖЕН!!!!', fg = 'green', bg = 'black', font = ('Courier New', 34))
text.place(x = 100, y = 100, width = 700, height = 100)

timer = Label(text = '6', fg = 'green', bg = 'black', font = ('Courier New', 34))

window.mainloop()