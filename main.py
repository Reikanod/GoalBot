import telebot
import datetime
import  schedule
import sys
print(sys.prefix, '\n', sys.base_prefix)
TOKEN = open(r'..\personal_info\GoalBot', 'r').readline().strip()

bot = telebot.TeleBot(TOKEN)
channel_id = '-1002091453911'

# узнать дату, текст и объединить их
date = datetime.datetime.now()
months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа',
          'сентября', 'октября', 'ноября', 'декабря']
date = f'{date.day} {months[date.month - 1]}\n'
text = open(r'resourses\daily_text.txt', 'r', encoding='utf-8').read()
day_opener = date + text

@bot.message_handler(content_types=['text'])
def hello(message):
    bot.send_message(channel_id, day_opener)


def hi():
    bot.send_message(channel_id, day_opener)








bot.infinity_polling()
