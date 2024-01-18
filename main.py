import telebot

bot = telebot.TeleBot('')

user_decision = {}

@bot.message_handler(commands=['start'])
def start(message):
    global user_decision
    user_decision = 0
    bot.send_message(message.chat.id, "Привет! Хочешь поиграть в мою квест-игру про хоббитов?\nЕсли да то жми /game и начинай свои приключения")

if __name__ == "__main__":
    bot.polling(none_stop=True)