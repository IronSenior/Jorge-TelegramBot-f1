#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

from libs import comp_func as comp
from libs import user_func as user
from libs import time_func as timef
from libs.keyboard import *
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
            bot.send_message(cid, keyboard_message(cid), reply_markup = keyboard_team)
    else:
            print "Se produjo un fallo E:001"

@bot.callback_query_handler(func = lambda team: team.data in ["mercedes", "red_bull", "williams", "ferrari", "mclaren", "force_india", "toro_rosso", "lotus", "sauber", "marussia"])
def join_in(team):
    cid = team.message.chat.id
    uid = team.from_user.id
    mid = team.message.message_id
    unick = team.from_user.username
    uteam = team.data
    if comp.existe_comp(cid):
        if user.existe_user(uid, cid):
            if user.team_full(cid, uteam):
                message = "Ese equipo esta lleno " + unick + ", elige uno con menos de 2 pilotos"
                bot.send_message(team.message.chat.id, message)
            else:
                if(user.change_team(cid, uid, uteam)):
                    bot.edit_message_text(keyboard_message(cid), cid, mid, reply_markup = keyboard_team)
        else:
            if user.team_full(cid, uteam):
                message = "Ese equipo esta lleno " + unick + ", elige uno con menos de 2 pilotos"
                bot.send_message(team.message.chat.id, message)

            else:
                user.join_in(cid, uid, unick, uteam)
                bot.edit_message_text(keyboard_message(cid), cid, mid, reply_markup = keyboard_team)
    else:
        send(m, "No hay competición en este grupo todavía")
        send(m, "Puedes empezar una con /st_comp")

@bot.message_handler(commands=['dl_comp'])
def dl_competition(m):
    cid = m.chat.id
    if comp.existe_comp(cid):
        comp.delete_comp(cid)
        send(m, "La competición ha sido eliminada")
    else:
        send(m, "No existe competición todavía")
        send(m, "Puedes empezar una con /st_comp")

@bot.message_handler(commands=['time'])
def time(m):
    cid = m.chat.id
    uid = m.from_user.id
    uname = m.from_user.first_name
    #time = telebot.util.extract_arguments(m.text)
    time = m.text.split()[1]
    if comp.existe_comp(cid):
        if timef.add_time(cid, uid, time):
            msg = uname + " ha agregado su tiempo"
            send(m, msg)

        else:
            send(m, "No se ha podido agregar el tiempo [Error de formato]")
    else:
        send(m, "No hay ninguna competición en este grupo")
        send(m, "Puedes empezar una con /st_comp")


@bot.message_handler(commands=['race_info'])
def next_race(m):
    cid = m.chat.id

    if comp.existe_comp(cid):
        race = comp.get_race_bycomp(cid)

        sendMarkdownMessage(cid, """
            🎟 *Próxima Carrera* 🎟

            *Nombre: * {}
            *Vueltas: * {}

        """.format(race['nombre'], race['long']))

        bot.send_photo(cid, "%s"%(race['image']))

    else:
        send(m, "No hay ninguna competición en este grupo")
        send(m, "Puedes empezar una con /st_comp")

@bot.message_handler(commands=['end_race'])
def end_race(m):
    cid = m.chat.id

    if comp.existe_comp(cid):
        send(m, "La carrera ha terminado")
        #Aqui sumaremos los puntos y todos los tiempos se pondran en 0
        comp.plus_race_bycomp(cid)
        next_race(m)

    else:
        send(m, "No hay ninguna competición en este grupo")
        send(m, "Puedes empezar una con /st_comp")


bot.polling()
