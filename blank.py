import datetime
import telebot

# BOT
TOKEN = '6604421287:AAF-Y_rWfZ1N1NUDrKp1N9afMfelqsOKcuM'  # bot token from @BotFather
#обычно лучше сохранить токен в отдельный файл и ипортировать его
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def start(message):
    user = message.chat.id
    current_date = datetime.date.today()
    user_text = message.text
    if user_text == "Какой сегодня день?": #проверяем условие
        dateint = current_date.strftime("%Y-%m-%d") #сохраняем в доту
        day_of_week = current_date.strftime("%A") #сохраняем день недели
        response = f'Текущая дата ( в формате YYYY-MM-DD ): {dateint}\nДень недели: {day_of_week}' #вывод в виде ответа
        bot.reply_to(message, response)
    elif message.text == '/start': #ответ на команду старт
        bot.send_message(user, "Всем привет, я бот, который скажет тебе какой сегодня день")
        bot.send_message(user, 'Напиши фразу "Какой сегодня день?"')
    else:
        bot.reply_to(message, 'Неверная команда. Напиши "Какой сегодня день?"') #ответ на неверный текст

# Запускаем бота
bot.polling(none_stop=True)
