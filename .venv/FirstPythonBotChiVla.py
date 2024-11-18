import telebot

token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])

def echo(message):
#    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Ба! Знакомые все лица!")


bot.polling(none_stop=True)