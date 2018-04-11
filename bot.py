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
    #Este comando crea la competición y manda el seleccionador de equipos
    cid = m.chat.id #Chat_id
    cname = m.chat.title #Nombre del chat
    uid = m.from_user.id

    #Para comprobar si el chat es un grupo o no, miramos su id (los grupos tienen id negativa)
    if cid > 0:
        send(m, "Error!! Debes crear la competición en un grupo")
    elif cid < 0:
        if comp.existe_comp(cid):
            send(m, "Ya hay una competción en este grupo")
        else:
            comp.create_comp(cid)
            send(m, "La competición se ha creado")
            #Manda el mensaje de los equipos con el teclado cuando se crea la competición
            bot.send_message(cid, keyboard_message(cid), reply_markup = keyboard_team)
            #Establece al creador de la competición como administrador de la misma
            comp.add_admin(cid, uid, cname)
            #Abre el chat privado con el admin
            bot.send_message(uid, "Desde este chat, podrás administrar tus competiciones usando /my_comps")
    else:
            print "Se produjo un fallo E:001"

#Maneja las respuestas del teclado, entra cada vez que alguien clicka una opción
@bot.callback_query_handler(func = lambda team: team.data in ["mercedes", "red_bull", "williams", "ferrari", "mclaren", "force_india", "toro_rosso", "lotus", "sauber", "marussia"])
def join_in(team):
    cid = team.message.chat.id
    uid = team.from_user.id
    mid = team.message.message_id
    unick = team.from_user.username
    uteam = team.data #Equivale al valor de la lista que se corresponde con el botón clickado
    if comp.existe_comp(cid):
        if user.existe_user(uid, cid):
            if user.team_full(cid, uteam):
                message = "Ese equipo esta lleno " + unick + ", elige uno con menos de 2 pilotos"
                bot.send_message(team.message.chat.id, message)
            else:
                #Si el usuario que clicka ya está en la competición y el equipo
                #que selecciona no está lleno, lo cambia de equipo
                if(user.change_team(cid, uid, uteam)):
                    #Actualiza el mensaje que acompaña al teclado, su estructura está
                    #en libs/keyboard.py
                    bot.edit_message_text(keyboard_message(cid), cid, mid, reply_markup = keyboard_team)
        else:
            if user.team_full(cid, uteam):
                message = "Ese equipo esta lleno " + unick + ", elige uno con menos de 2 pilotos"
                bot.send_message(team.message.chat.id, message)

            else:
                #Para un usuario nuevo, que selecciona un equipo que no está lleno
                #mete los campos necesarios en la base de datos
                user.join_in(cid, uid, unick, uteam)
                #Actualiza el mensaje que acompaña al teclado, su estructura está
                #en libs/keyboard.py
                bot.edit_message_text(keyboard_message(cid), cid, mid, reply_markup = keyboard_team)
    else:
        bot.send_message(team.message.chat.id, "No hay competición en este grupo todavía")
        bot.send_message(team.message.chat.id, "Puedes empezar una con /st_comp")

@bot.message_handler(commands=['dl_comp'])
def dl_competition(m):
    #Este comando permite eliminar una competición
    cid = m.chat.id
    uid = m.from_user.id
    uname = m.from_user.first_name
    if comp.existe_comp(cid):
        if user.is_admin(cid, uid):
            comp.delete_comp(cid, uid)
            send(m, "La competición ha sido eliminada")
        else:
            message = uname + " no tiene permisos para realizar esa operación"
            send(m, message)

    else:
        send(m, "No existe competición todavía")
        send(m, "Puedes empezar una con /st_comp")

@bot.message_handler(commands=['time'])
def time(m):
    cid = m.chat.id
    uid = m.from_user.id
    uname = m.from_user.first_name
    # time = telebot.util.extract_arguments(m.text)
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
    #Este comando nos dará información sobre la próxima carrera
    cid = m.chat.id

    if comp.existe_comp(cid):
        race = comp.get_race_bycomp(cid)

        sendMarkdownMessage(cid, """
            🎟 *Próxima Carrera* 🎟

            *Nombre: * {}
            *Vueltas: * {}

        """.format(race['nombre'], race['long']))

        bot.send_photo(cid, "%s"%(race['image']))


@bot.message_handler(commands=['pen'])
def penalizar(m):
    cid = m.chat.id
    uid = m.from_user.username


@bot.message_handler(commands=['end_race'])
def end_race(m):
    #Este comando es uno de los mas importantes
    #Dará por terminada la carrera, sumará los puntos e imprimirá la clasificación
    #También dejará todos los tiempos a 0 de nuevo
    cid = m.chat.id
    uid = m.from_user.id
    uname = m.from_user.username

    if comp.existe_comp(cid):
        if user.is_admin(cid, uid):
            send(m, "La carrera ha terminado")
            #Comprobamos si todos han metido su tiempo (Falta)
            #Damos los puntos a los jugadores
            timef.give_points(cid)
            #Manda un mensaje con el podium (Falta)
            #Imprime la clasificación de la competición (Falta)
            comp.plus_race_bycomp(cid)
            next_race(m)
        else:
            message = uname + " no tiene permisos para realizar esa operación"
            send(m, message)


    else:
        send(m, "No hay ninguna competición en este grupo")
        send(m, "Puedes empezar una con /st_comp")


@bot.message_handler(commands=['my_comps'])
def my_comps(m):
    #Primer paso de la herramienta que permite administrar una competición
    cid = m.chat.id
    uid = m.from_user.id

    if cid > 0:
        if user.have_comps(uid): #Mira si es admin de alguna competicion
            keyboard_comps = get_keyboardAdmin(uid) #Devuelve un teclado con las competiciones
            bot.send_message(cid, "Selecciona la competción a administrar", reply_markup = keyboard_comps)
            
            #Habrá que esperar una respuesta y seguir
        else:
            send(m, "No eres administrador de ninguna competición")
    else:
        send(m, "Ese comando solo puede usarse desde un chat privado")


@bot.callback_query_handler(func=lambda callback: comp.existe_comp(callback.data))
def send_options(callback):
    print(callback.data)
    cid = callback.message.chat.id
    keyboard_opts = get_keyboardOptions()
    bot.send_message(cid, "Elige una opción", reply_markup=keyboard_opts)


bot.polling()
