#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from database_func import *
import private as tk
import time
import random



#CONFIGURACIÓN DE TELEGRAM
token = tk.tuko()
bot = telegram.Bot(token=token)
updater = Updater(token=token)
dispatcher = updater.dispatcher



#Simplifica el enviar
def send(message, bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=message)

#Crea una competicion
def new_competition(bot, update, args):

    if len(args) == 0:
        send("Error!! Hulio", bot, update)

    elif args[0]:
        nombre = str(args[0])
        chat_id = int(update.message.chat_id)

        data = [str(nombre),int(chat_id)]

        db = database_functions()
        db.competiciones()


    else:
            print "Existe un fallo"






competition_handler = CommandHandler('start_competition', new_competition, pass_args=True)
dispatcher.add_handler(competition_handler)

updater.start_polling()
