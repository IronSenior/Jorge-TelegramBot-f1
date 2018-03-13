#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

from libs import *
from database_func import *
import time
import random



#CONFIGURACIÓN DE TELEGRAM
token = tk.tk()
bot = telebot.TeleBot(token)


#Simplifica el enviar
def send(m, message_text):
    bot.send_message(m.chat.id, message_text)

#Crea una competicion
@bot.message_handler(commands=['start_competition'])
def new_competition(m):
    cid = int(m.chat.id) #Chat_id

    if cid > 0:
        send(m, "Error!! Debes crear la competición en un grupo")

    elif cid < 0:
        send(m, "La competición se ha creado")
        #db = database_functions()
        #db.competiciones()
    else:
            print "Existe un fallo"


bot.polling()