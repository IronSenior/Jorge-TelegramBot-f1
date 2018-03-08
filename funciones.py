# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import private as tuko
import time
import random
import csv

token = tuko.tuko()
bot = telegram.Bot(token=token)
updater = Updater(token=token)

dispatcher = updater.dispatcher

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
	name = competition[0]
	inicio = ['player_id','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','Tpoints']

	with open('./competitions/competitions.csv', 'a') as f:
		writer = csv.writer(f, delimiter=",")
		writer.writerow(competition)

	with open('./competitions/%s.csv'%(name), 'a') as f:
		writer = csv.writer(f, delimiter=",")
		writer.writerow(inicio)

	
def add_player(chat_id, player):
	row = [player,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']

	comp = get_comp(chat_id)

	with open('./competitions/%s.csv'%(comp), 'a') as f:
		writer = csv.writer(f, delimiter=",")
		writer.writerow(row)

def get_comp(chat_id):
	with open("./competitions/competitions.csv", 'rb') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=",")
		for row in reader:
			name = row['name']
			chat = row['chat_id']
			if int(chat) == int(chat_id):
				return name