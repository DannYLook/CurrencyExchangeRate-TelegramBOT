from datetime import datetime
import telebot
from pycbrf import ExchangeRates


bot = telebot.TeleBot('token')

@bot.message_handler(commands= ['start'])
def start(message):

    markup = telebot.types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True)
    itembt1 = telebot.types.KeyboardButton("USD")
    tembt2 = telebot.types.KeyboardButton("EUR")
    markup.add(itembt1, tembt2)
    bot.send_message(chat_id = message.chat.id, text = "Hello! What's the course today?", reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def message(message):

    message_norm = message.text.strip().lower()

    if message_norm in ['usd', 'eur']:
        rates = ExchangeRates(datetime.now())

        bot.send_message(chat_id = message.chat.id, text = f"{message_norm.upper()} курс - {float(rates[message_norm.upper()].rate)}", parse_mode = "html")

bot.polling(none_stop = True)