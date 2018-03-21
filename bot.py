#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

from libs import comp_func as comp
from libs import user_func as user
from libs import time_func as timef
import private as tk
import time
import random



#CONFIGURACIÓN DE TELEGRAM
token = tk.tk()
bot = telebot.TeleBot(token)


#Simplifica el enviar
def send(m, message_text):
    bot.send_message(m.chat.id, message_text)

def sendMarkdownMessage(cid, message_text):
    bot.send_message(cid, message_text, parse_mode="Markdown")


#Crea una competicion
@bot.message_handler(commands=['st_comp'])
def new_competition(m):
    cid = m.chat.id #Chat_id
    if cid > 0:
        send(m, "Error!! Debes crear la competición en un grupo")
    elif cid < 0:
        if comp.existe_comp(cid):
            send(m, "Ya hay una competción en este grupo")
        else:
            comp.create_comp(cid)
            send(m, "La competición se ha creado")
    else:
            print "Se produjo un fallo E:001"



@bot.message_handler(commands=['join_in'])
def join_in(m):
    uid = m.from_user.id
    cid = m.chat.id
    uname = m.from_user.first_name
    if comp.existe_comp(cid):
        if user.existe_user(uid, cid):
            message = uname + " ya se habia unido antes"
            send(m, message)
        else:
            user.join_in(uid, uname, cid)
            message = uname + " se ha unido con exito"
            send(m, message)
    else:
        send(m, "No hay competición en este grupo todavía")


@bot.message_handler(commands=['dl_comp'])
def dl_competition(m):
    cid = m.chat.id
    if comp.existe_comp(cid):
        comp.delete_comp(cid)
        send(m, "La competición ha sido eliminada")
    else:
        send(m, "No existe competición todavía")


@bot.message_handler(commands=['time'])
def time(m):
    cid = m.chat.id
    uid = m.from_user.id
    uname = m.from_user.first_name
    #time = telebot.util.extract_arguments(m.text)
    time = m.text.split()[1]

    if timef.add_time(cid, uid, time):
        msg = uname + " ha agregado su tiempo"
        send(m, msg)

    else:
        send(m, "No se ha podido agregar el tiempo [Error de formato]")


@bot.message_handler(commands=['next_race'])
def next_race(m):
    cid = m.chat.id

    race = comp.get_race_bycomp(cid)

    sendMarkdownMessage(cid, """
        🎟 *Próxima Carrera* 🎟

        *Nombre: * {}
        *Vueltas: * {}

    """.format(race['nombre'], race['long']))

    bot.send_photo(cid, "%s"%(race['image']))




bot.polling()
