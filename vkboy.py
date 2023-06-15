import random
from bot_course import *
from wiki import *
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = 'vk1.a.0T2UbyrMw1boZaTBUmlUScsOtksayJtVvwDssLlsdcfS9TO-X-UFFN8LYpGbuFwlAsyn_6z0SU04Vw8QRkhb4bDBQZ_nYIoA6orzg5lD7lwBUpsaDNMdO3MzffL2q8hOoDzoWqui6Vp0jhiPG3BYxOx-grEWKw0XULU12RATlOzt45PP1xe2CWiC6Yoaxfs7Se1zCrAUkoJIE02rbyXwQw'
vk_session = vk_api.VkApi(token = token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1, 10000000)
        if msg == 'курс':
            responce = f'{getCourse("R01235")} рублей за 1 доллар, {getCourse("R01239")} за 1 евро, ' \
                       f'{getCourse("R01035")} за 1 фунт'
        elif msg.startswith("вики"):
            article = msg[4:]
            responce = get_wiki_article(article)
        else:
            responce = "Неизвестная команда"
        vk.messages(user_id=user_id, random_id=random_id, message=responce[0:4096])

