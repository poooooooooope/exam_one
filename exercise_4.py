import telebot

TOKEN = "2147276455:AAFVbY2f1jE2m_H76h0-yN56PsiD_86Vbvo"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, Enter a word or text")

@bot.message_handler(content_types=['text'])
def reply_to_text(message):
    bot.reply_to(message, message.text)
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    # vowels = ('aeiouy')
    count = 0

    for i in message.text:
        if i == vowels:
           count += 1

    bot.reply_to(message, count)



bot.infinity_polling()