import telebot  #pyTelegramBotAPI
import requests
from bs4 import BeautifulSoup
import random

token = '5987648179:AAEwti50mMnixnUxm9wtPHUj1OCLOAjr2t8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    welcome = "Привет! Я умею рассказывать стихи, интересные факты, показывать котиков"
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                 one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Факт")
    button2 = telebot.types.KeyboardButton("Стихотворение")
    button3 = telebot.types.KeyboardButton("Котики")
    button4 = telebot.types.KeyboardButton("Новогодние песни")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, welcome, reply_markup=keyboard)



@bot.message_handler(commands=['fact'])
def send_fact(message):
    responce = requests.get('https://i-fakt.ru')
    responce = responce.content
    html = BeautifulSoup(responce, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    bot.send_message(message.chat.id, fact.text)
    bot.send_message(message.chat.id, fact.a.attrs['href'])

@bot.message_handler(commands = ['cat'])
def send_cat(message):
    cat = open('cat'+str(random.randint(1,3))+'.jpg', 'rb')
    bot.send_photo(message.chat.id, cat)

@bot.message_handler(commands=['audio'])
def send_audio(message):
    songs = ['ABBA', 'Bon_Jovi', 'Dean_Martin']
    song = open('ABBA.mp3', 'rb')
    bot.send_audio(message.chat.id, song)

@bot.message_handler(commands = ['videogame'])
def send_videogame(message):
    quastion = ('В какой жанр видеоигр ты хочешь сыграть? - Action, Adventure, RPG, Shooter, Strategy, Survival')
    a = input(bot.send_message(message.chat.id, quastion))
    bot.send_message(message.chat.id, a)
    if a == 'Action':
        game_text = 'God of War'
        bot.send_message(message.chat.id, game_text)
    elif a == 'Adventure':
        game_text = 'Stray'
        bot.send_message(message.chat.id, game_text)
    elif a == 'RPG':
        game_text = 'Dark Souls III'
        bot.send_message(message.chat.id, game_text)
    elif a == 'Shooter':
        game_text = 'Counter-Strike: Global Offensive'
        bot.send_message(message.chat.id, game_text)
    elif a == 'Strategy':
        game_text = 'Expeditions: Rome'
        bot.send_message(message.chat.id, game_text)
    elif a == 'Survival':
        game_text = 'Minecraft'
        bot.send_message(message.chat.id, game_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_inline = telebot.types.InlineKeyboardButton("Перейти",
                                                       url='https://journal.tinkoff.ru/list/2022-best-games/')
    keyboard.add(button_inline)
    bot.send_message(message.chat.id, "Больше игр здесь", reply_markup=keyboard)

@bot.message_handler(commands = ['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и всё стихотворение"
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_inline = telebot.types.InlineKeyboardButton("Перейти",
                                                       url = 'https://stihi.ru/')
    keyboard.add(button_inline)
    bot.send_message(message.chat.id, "Больше стихотворений здесь", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.strip() == 'Факт':
        send_fact(message)
    elif message.text.strip() == 'Стихотворение':
        send_poem(message)
    elif message.text.strip() == 'Котики':
        send_cat(message)
    elif message.text.strip() == 'Новогодние песни':
        send_audio(message)

bot.polling()