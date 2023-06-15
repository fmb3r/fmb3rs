import requests
import random
from bs4 import BeautifulSoup

def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content

    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_ = 'p-2 clearfix'))
    print(fact.text)
    print(fact.a.attrs['href'])

def get_fest():
    response = requests.get('https://kudago.com/nsk/festival/')
    response = response.content

    html = BeautifulSoup(response, 'lxml')
    fest = random.choice(html.find_all(class_='p-2 clearfix'))

    print(fest.text)
    print(fest.a.attrs['href'])

user_wish = input('Чем вы хотели бы заняться? ')
if 'факт' == user_wish:
    get_fact()
elif 'фестиваль' == user_wish:
    get_fest()
else:
    print('Может лучше все таки остаться дома?!')
