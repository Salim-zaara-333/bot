import os
import telebot
from flask import Flask
from flask import request

from flask_sslify import SSLify
app = Flask(__name__)

bot = telebot.TeleBot("5960459666:AAGmFkCzbik_VUM1TFMLKWqI7iwOIb4PSD0")
start="Ahlan! 😎\nTo hack a Facebook account: press /hack_facebook\nTo hack a Messenger account: press /hack_messenger\nTo hack a Instagram account: press /hack_instagram"
    
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(chat_id=message.chat.id, text=str(start))
    #bot.reply_to(message, "/hackfacebook: 40$? /hackinstagram: 40$")
sslify= SSLify(app)
@bot.message_handler(content_types=['text'])
def check_input(message):
    if message.text == '/hack_facebook':
        bot.send_message(chat_id=message.chat.id, text='Hacking Facebook account: 60$\nContact @slimz')
    elif message.text == '/hack_messenger':
        bot.send_message(chat_id=message.chat.id, text='Hacking Messenger account: 40$ \nContact @slimz')
    elif message.text == '/hack_instagram':
        bot.send_message(chat_id=message.chat.id, text='Hacking Instagram account: 50$\nContact @slimz')
    else:
        bot.send_message(chat_id=message.chat.id, text='Invalid command')    

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
    #bot.reply_to(message, 'inbox @slimz')
    #bot.send_message(chat_id=message.chat.id, text=str(start))

bot.polling()
