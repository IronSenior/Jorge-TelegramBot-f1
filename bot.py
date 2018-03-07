# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import funciones as func
import time
import random
import csv

token = 
bot = telegram.Bot(token=token)
updater = Updater(token=token)

dispatcher = updater.dispatcher


def send(message, bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=message)

def new_competition(bot, update, args):
	if args == []:
		send("Error!! Tienes que decirme el nombre de la competición y la password", bot, update)

	elif args[0] and args[1]:
		nombre = str(args[0])
		passwd = str(args[1])
		if func.existe_comp(nombre):
			send("Ese nombre no es válido o ya está en uso", bot, update)
		else:
			competition = [nombre, passwd]
			func.crear_comp(competition)
			send("Has comenzado la competición con éxito", bot, update)
			send("Ahora todos se pueden unir", bot, update)

def new_player(bot, update, args):
	comp = args[0]
	password = args[1]
	id_player = args[2]
	#permiso = func.passwd_comp(comp, password, id_player) 
	
	if True:
		func.add_player(comp, id_player)
		send("Jugador añadido", bot, update)

	else:
		send("Error! Ha introducido mal los datos de la competición")




competition_handler = CommandHandler('start_competition', new_competition, pass_args=True)
matricula_handler = CommandHandler('unirme', new_player, pass_args=True)

dispatcher.add_handler(competition_handler)
dispatcher.add_handler(matricula_handler)

updater.start_polling()