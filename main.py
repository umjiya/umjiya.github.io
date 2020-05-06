import telebot

bot = telebot.TeleBot("1231301013:AAGhXUTrqY2yvFs8cNA3kzS2tC376tre-4w")

@bot.message_handler(content_types=["text", "sticker"])
def Welcome(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, "Добро пожаловать,<b>{0.first_name}</b>\nМеня зовут <b>{1.first_name}</b>!\nДавай общаться!".format(message.from_user,bot.get_me()),parse_mode='html')
def common(message):
    
if __name__ == '__main__':
     bot.infinity_polling()
