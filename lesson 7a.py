import os
from gtts import gTTS
from pygame import mixer #pip install pygame --pre
import time

my_file = open('f.txt', 'r')
my_text = my_file.read()
my_file.close()

mixer.init()
tts = gTTS(text = my_text, lang = 'en')
tts.save('audio_1.mp3')
mixer.music.load('audio_1.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)
mixer.music.unload()