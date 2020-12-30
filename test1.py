import telebot
import random
import requests
import _json
bot = telebot.TeleBot('888054888:AAH5_zHICdF1iedKINYBW55hFm0QWuJf3v8')


def current_weather():

    try:

        api_key = "f4179114c9232e69087c46fa5ae4fa2b"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Ufa,RU"
        complete_url = base_url + "q=" + city_name + "&APPID=" + api_key
        response = requests.get(complete_url,
                                params={'units': 'metric', 'lang': 'ru'})
        x = response.json()

        y = x["main"]
        z = x["weather"]
        weather_description = 'В Уфе сейчас ' + str(z[0]['description']) + '! \n\n'
        wind_speed = 'Скорость ветра: ' + str(x["wind"]["speed"]) + 'м/с\U0001F300	'
        current_temp = 'Где мой мозг...Тебе ведь так ничего не понятно...\U0001F644 \n\n\U0001F321В градусах это, примерно: ' + str(y["temp"]) + '\xb0C \n'
        feels_like = '(Но желтые медведи ощущают это как ' + str(y["feels_like"]) + '\xb0C)' + '\n'
        min_temp = 'Минимальная температура сегодня: ' + str(y["temp_min"]) + '\xb0C'
        max_temp = 'Максимальная температура сегодня: ' + str(y["temp_max"]) + '\xb0C'

        xxx = weather_description + current_temp + '\n' + feels_like + '\nЕще немного информации: \U0001F325\n\n' + min_temp + '\n' + max_temp + '\n' + wind_speed
    except Exception as e:
        print("Exception (weather):", e)
        pass
    return xxx


dance = ['Я хочу танцевать свои танцы!', 'Криминаль-кри-криминаль...', 'Я не для актёрского мастерства создана',
         'Виливиливон', 'Алиса, а давай ты замору больше не будешь писать?', 'А почему легенда всего 7 минут?']
laughter = ['Всё, все посмеялись?', 'Ты не должна смеяться! Мы же подружки!!!', 'Я сейчас не хотела смеяться!',
            'Опять я шут!..']
sad = ['Я не резиновая!', 'Я под музыку не плачу', 'Настроение: плакать и быть красивой.',
       'Ожидания не всегда ожидаются', 'Меня снова гасят!', 'Я устала от недоверия и лжи', 'Я не продажная!',
       'Нет, ну вы нормальные, нет?']
bear = ['Я желтый медведь', 'Я теперь люблю пчёл', 'Я серьёзная девушка', 'Сама ты Найля!', 'Я все мемы понимаю!',
        'Я подожду! Я всех Подожду!', 'МАКСИМАЛЬНО!', 'Я буду спать в своей вожатской!']


@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.chat.id,
                         'Привет, Я - Бот Нелечки Рашитовнчки. \nЯ умею круто танцевать и мило ругаться.\n Выбери подходящую эмоцию и я отправлю тебе свою коронную фразу! \n*танцую по виливиливонски*')
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
    elif message.text == "Погода":
        bot.send_message(message.chat.id, current_weather())
    else:
        bot.send_message(message.chat.id,
                         'Ты меня не ценишь! \nА поздороваться? \nУ тебя пять минут, считаю до трёх! \n(Напиши "Привет")',
                         reply_markup=keyboard1)


@bot.message_handler(content_types=['photo'])
def start_message(message):
    bot.send_message(message.chat.id, 'Извините, мне нужно учиться. \nУ меня нет времени смотреть на твои картинки...')


keyboard1 = telebot.types.ReplyKeyboardMarkup(False, False)
keyboard1.add('Привет', '\U0001F483', '\U0001F603', '\U0001F625', '\U0001F43B', 'Погода')

bot.polling()
