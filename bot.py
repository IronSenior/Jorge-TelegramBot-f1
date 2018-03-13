#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

from libs import comp_func as comp
from libs import user_func as user
import private as tk
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
    cid = m.chat.id #Chat_id

    if cid > 0:
        send(m, "Error!! Debes crear la competición en un grupo")

    elif cid < 0:
        if comp.create(cid):
            send(m, "La competición se ha creado")

        #db = database_functions()
        #db.competiciones()
    else:
            print "Se produjo un fallo E:001"


bot.polling()