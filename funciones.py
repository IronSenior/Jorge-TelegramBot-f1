#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
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


def send(message, bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=message)

def existe_comp(chat_id):
	existe = False
	with open("./competitions/competitions.csv", 'rb') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=",")
		for row in reader:
			chat = row['chat_id']
			if int(chat) == int(chat_id):
				existe = True
	return existe


def crear_comp(competition):
	name = str(competition[0])
	chat_id = int(competition[1])
	#inicio = ['player_id','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','Tpoints']

	#with open('./competitions/competitions.csv', 'a') as f:
	#	writer = csv.writer(f, delimiter=",")
	#	writer.writerow(competition)

	#with open('./competitions/%s.csv'%(name), 'a') as f:
	#	writer = csv.writer(f, delimiter=",")
	#	writer.writerow(inicio)

	print "Las tablas van a ser creadas"
	print name
	print str(chat_id)

	cursor.execute('''INSERT INTO COMPETICIONES (ID, NAME) VALUES (%i, %s)'''%(chat_id, string_to_string(name)))

	print ("Linea añadida")

	cursor.execute('''CREATE TABLE %s
				(ID INT PRIMARY KEY			NOT NULL,
				PLAYER_ID			TEXT 	NOT NULL,
				C1 					TEXT 	NOT NULL,
				C2 					TEXT 	NOT NULL,
				C3 					TEXT 	NOT NULL,
				C4 					TEXT 	NOT NULL,
				C5 					TEXT 	NOT NULL,
				C6  				TEXT 	NOT NULL,
				C7 					TEXT 	NOT NULL,
				C8 					TEXT 	NOT NULL,
				C9 					TEXT 	NOT NULL,
				C10 				TEXT 	NOT NULL,
				C11 				TEXT 	NOT NULL,
				C12  				TEXT 	NOT NULL,
				C13 				TEXT 	NOT NULL,
				C14 				TEXT 	NOT NULL,
				C15 				TEXT 	NOT NULL,
				C16    				TEXT 	NOT NULL,
				C17 				TEXT 	NOT NULL,
				C18 				TEXT 	NOT NULL,
				C19 				TEXT 	NOT NULL,
				TOTAL_SCORE 		INT 	NOT NULL)'''%(name))

	print ("Tabla creada")


	
def add_player(chat_id, player):
	#row = [player,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']

	comp = get_comp(chat_id)
	player = str(player)

	#with open('./competitions/%s.csv'%(comp), 'a') as f:
	#	writer = csv.writer(f, delimiter=",")
	#	writer.writerow(row)

	cursor.execute('''INSERT INTO %s (ID, PLAYER_ID, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19,
				TOTAL_SCORE) VALUES (1, %s, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 0)''' %(comp, player))


def get_comp(chat_id):
	with open("./competitions/competitions.csv", 'rb') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=",")
		for row in reader:
			name = row['name']
			chat = row['chat_id']
			if int(chat) == int(chat_id):
				return name


def start_db():
	cursor.execute('''CREATE TABLE COMPETICIONES
				(ID INT PRIMARY KEY			NOT NULL,
				NAME 				TEXT 	NOT NULL)''')


def string_to_string(palabra):
	palabra = "'" + palabra + "'"
	return palabra

#start_db()

#competition = ['generico', 401038769]

#crear_comp(competition)