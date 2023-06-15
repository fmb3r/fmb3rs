# window = Tk()
# window.title('окно')
# window.geometry('500x500+400+400')
# count = 0
# def change_count():
#     global count
#     count += 1
#     lab['text'] = count
#
# lab = Label(window, text = 'чел, выйди', bg = 'white', fg = '#432', font = '16')
# lab.place(x = 100, y = 100)
#
# btn = Button(text = 'выйти', bg = 'black', fg = 'white', font = '16', command = change_count)
# btn.place(x = 200, y = 200)
#
#
# window.mainloop()

from tkinter import *
import requests
from datetime import datetime
from bs4 import BeautifulSoup

window=Tk()
window.geometry('800x600')
window.title("exchanges rates every day")

today = datetime.today()
today=today.strftime('%d/%m/%Y')
payload={'date req': today}

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
responce = requests.get(url, params=payload)
xml = BeautifulSoup(responce.content, 'lxml')

def get_course(id):
    return xml.find('valute', {'id': id}).value.text

# img = PhotoImage(file = '')

usd_course = Label(window, text='S '+ get_course('R012345'), font='Arial 16')
usd_course.place(x=400, y=350)

window.mainloop()