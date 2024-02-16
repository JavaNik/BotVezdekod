
import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType



token="тут_был_токен" 



bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


def blasthack(id, text):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

       if event.to_me:

   
          message = event.text.lower()
     
          id = event.user_id
    

          if message == 'привет':
            blasthack(id, 'Привет вездекодерам!')

          elif message == 'ку?':
              blasthack(id, 'Привет вездекодерам!' )

        

          else:
             blasthack(id, 'Не понимаю')
