#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import funciones as func
import private as tuko
import sqlite3
import time
import random
import csv

#//////////////////////////////////////////////////////////////////////////////////

#CONFIGURACIÓN DE TELEGRAM
token = tuko.tuko()
bot = telegram.Bot(token=token)
updater = Updater(token=token)

dispatcher = updater.dispatcher

#CONFIGURACIÓN DE DB
try:
	db = sqlite3.connect("./BaseDatos")
	#db = sqlite3.connect(':memory:')

	cursor = db.cursor()
	print "La base de datos se abrió correctamente"
except:
	print "Error con la base de datos"

#//////////////////////////////////////////////////////////////////////////////////

#Simplifica el enviar
def send(message, bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=message)

#Crea una competicion
def new_competition(bot, update, args):
	if args == []:
		send("Error!! Tienes que decirme el nombre de la competición", bot, update)

	elif args[0]:
		nombre = str(args[0])
		chat_id = update.message.chat_id

		if func.existe_comp(chat_id):
			send("En este chat ya hay una competición", bot, update)
		else:
			competition = [nombre,chat_id]
			func.crear_comp(competition)
			send("Has comenzado la competición con éxito", bot, update)
			send("Ahora todos se pueden unir", bot, update)

#Te añade a la competición del chat
def new_player(bot, update, args):
	#En el futuro no pedirá el nombre y lo cogera de telegram
	#print update.message.user_name

	if args == []:
		send("Dime un nombre para la clasificación")

	elif args[0]:
		comp = update.message.chat_id
		id_player = args[0]
		permiso = func.get_comp(comp)

		if permiso:
			func.add_player(comp, id_player)
			send("Te has unido con exito", bot, update)

		else:
			send("Error! No existe una competición todavía")




competition_handler = CommandHandler('start_competition', new_competition, pass_args=True)
matricula_handler = CommandHandler('join_in', new_player, pass_args=True)


dispatcher.add_handler(competition_handler)
dispatcher.add_handler(matricula_handler)


updater.start_polling()