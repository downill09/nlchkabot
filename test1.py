import telebot
import random

bot = telebot.TeleBot('888054888:AAH5_zHICdF1iedKINYBW55hFm0QWuJf3v8')

dance = ['Я хочу танцевать свои танцы!','Криминаль-кри-криминаль...','Я не для актёрского мастерства создана','Виливиливон','Алиса, а давай ты замору больше не будешь писать?','А почему легенда всего 7 минут?']
laughter = ['Всё, все посмеялись?','Ты не должна смеяться! Мы же подружки!!!','Я сейчас не хотела смеяться!','Опять я шут!..']
sad = ['Я не резиновая!','Я под музыку не плачу','Настроение: плакать и быть красивой.','Ожидания не всегда ожидаются','Меня снова гасят!','Я устала от недоверия и лжи','Я не продажная!','Нет, ну вы нормальные, нет?']
bear = ['Я желтый медведь','Я теперь люблю пчёл','Я серьёзная девушка','Сама ты Найля!','Я все мемы понимаю!','Я подожду! Я всех Подожду!','МАКСИМАЛЬНО!','Я буду спать в своей вожатской!']
@bot.message_handler(content_types=['text'])
def start_message(message):

    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.chat.id,'Привет, Я - Бот Нелечки Рашитовнчки. \nЯ умею круто танцевать и мило ругаться.\n Выбери подходящую эмоцию и я отправлю тебе свою коронную фразу! \n*танцую по виливиливонски*')
    elif message.text == "\U0001F483":
        bot.send_message(message.chat.id, dance[random.randrange(0, 6)])
    elif message.text == "\U0001F603":
        bot.send_message(message.chat.id, laughter[random.randrange(0, 4)])
    elif message.text == "\U0001F625":
        bot.send_message(message.chat.id, sad[random.randrange(0, 8)])
    elif message.text == 'че' or message.text == 'Че' or message.text == 'Чё' or message.text == 'чё' or message.text == 'ЧЕ' or message.text == 'ЧЁ':
        bot.send_message(message.chat.id, 'ВАЧЁ!')
    elif message.text == "\U0001F43B":
        bot.send_message(message.chat.id, bear[random.randrange(0, 8)])
    else:
        bot.send_message(message.chat.id, 'Ты меня не ценишь! \nА поздороваться? \nУ тебя пять минут, считаю до трёх! \n(Напиши "Привет")', reply_markup=keyboard1)

@bot.message_handler(content_types=['photo'])
def start_message(message):
    bot.send_message(message.chat.id, 'Извините, мне нужно учиться. \nУ меня нет времени смотреть на твои картинки.')

keyboard1=telebot.types.ReplyKeyboardMarkup(True,False)
keyboard1.row('Привет','\U0001F483','\U0001F603','\U0001F625','\U0001F43B')

bot.polling()