from tkinter import *

window = Tk()
window.geometry('700x500')
window.title('Самый сложный тест по Marvel')

label_title = Label(text = 'Тестирование по вселенной Marvel',
                    font = ('Arial', 24), fg = 'white', bg = 'black')
label_title.place(width = 700, height = 50, x = 0, y = 0)

facts = [
    {'text' : 'Человеческое имя Халка - Брюс Беннет',
     'right' : 1},
    {'text': 'Уоллт Дисней является создателем вселенной Marvel',
     'right' : 0},
    {'text' : 'Выдуманный город Дженова является родиной Черной Пантеры',
     'right' : 0},
    {'text' : 'До появления костюма супер героя, Человек Муровей занимался воровством',
     'right' : 1}
]

cur_q = 0
points = 0
def check():
    global cur_q, points
    answer = var.get()
    if bool(answer) == facts[cur_q]['right']:
        points += 1
    if cur_q < len(facts)-1:
        cur_q += 1
        fact['text'] = facts[cur_q]['text']
    else:
        points_label = Label(text = 'Вы набрали ' + str(points) + ' очков',
                    font = ('Arial', 34), fg = 'red', bg = 'white')
        points_label.place(x = 0, y = 0, width = 700, height = 250)
        if points >= len(facts)/2:
            label_happy.place(x = 0, y = 250, width = 700, height = 250)
        else:
            label_sad.place(x = 0, y = 250, width = 700, height= 250)

fact = Message(text = facts[cur_q]['text'], font = ('Arial', 14), width = 680,
                borderwidth = 0)
fact.configure(justify = CENTER)
fact.place(x = 10, y = 60)
var = IntVar()
false = Radiobutton(text = 'Ложь', variable = var, value = 0)
false.place(x = 20, y = 89)
true = Radiobutton(text = 'Правда', variable = var, value = 1)
true.place(x = 100, y = 89)
b = Button(text = 'Ответить', font = ('Arial', 24), fg = 'black', command = check)
b.place(x = 50, y = 120)

pic_happy = PhotoImage(file = 'happy.png')
label_happy = Label(image = pic_happy)

pic_sad = PhotoImage(file = 'sad.png')
label_sad = Label(image = pic_sad)

window.mainloop()