#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telebot import *
import json
from constantes import db_path

#Esta función contiene la estructura del mensaje con el que va el teclado de elección de equipo.
#En ella se llama a team_members una vez por cada equipo y devuelve el mensaje completo
def keyboard_message(cid):
    mensaje = '''Estos son los equipos de la competicion y los pilotos de cada uno de ellos:
    Mercedes:%s
    Red Bull:%s
    Williams:%s
    Ferrari:%s
    McLaren:%s
    Force India:%s
    Toro Rosso:%s
    Lotus:%s
    Sauber:%s
    Marussia:%s''' %(team_members(cid, "mercedes"),
                    team_members(cid, "red_bull"),
                    team_members(cid, "williams"),
                    team_members(cid, "ferrari"),
                    team_members(cid, "mclaren"),
                    team_members(cid, "force_india"),
                    team_members(cid, "toro_rosso"),
                    team_members(cid, "lotus"),
                    team_members(cid, "sauber"),
                    team_members(cid, "marussia"))
    return mensaje

#Esta función devuelve una cadena con los usernames que hay en cada equipo separados por un espacio
def team_members(cid, team):
    path = db_path + str(cid)
    pilotos = ""
    with open('%s/players.json' % (path), 'r') as playersfile:
        players = json.load(playersfile)
        for userid in players['player_list']:
            if team == players[str(userid)]['team']:
                pilotos += " " + players[str(userid)]['name']
    return pilotos


#Nombre del teclado, se llama a él desde bot.py
keyboard_team = types.InlineKeyboardMarkup()

#Añade los botones con su texto, y el valor que devuelve cada botón cuando es clickado
keyboard_team.add(types.InlineKeyboardButton("Mercedes", callback_data = "mercedes"),
                 types.InlineKeyboardButton("Red Bull", callback_data = "red_bull"),
                 types.InlineKeyboardButton("Williams", callback_data = "williams"),
                 types.InlineKeyboardButton("Ferrari",  callback_data = "ferrari"),
                 types.InlineKeyboardButton("McLaren", callback_data = "mclaren"),
                 types.InlineKeyboardButton("Force India", callback_data = "force_india"),
                 types.InlineKeyboardButton("Toro Rosso", callback_data = "toro_rosso"),
                 types.InlineKeyboardButton("Lotus", callback_data = "lotus"),
                 types.InlineKeyboardButton("Sauber", callback_data = "sauber"),
                 types.InlineKeyboardButton("Marussia", callback_data = "marussia")
)


def get_keyboardAdmin(uid):
    #Esta función devuelve un teclado
    keyboard_comps = types.InlineKeyboardMarkup()
    with open("%sall_admins.json" % db_path, 'r') as alladminsfile:
        uid = str(uid)
        all_admins = json.load (alladminsfile)
        for userid in all_admins:
            for chatid in all_admins[userid]:
                chat_name = all_admins[uid][str(chatid)]
                keyboard_comps.add(types.InlineKeyboardButton("%s" % chat_name, callback_data=chatid))
    return keyboard_comps

def get_keyboardOptions(cid):
    keyboard_opts = types.InlineKeyboardMarkup()
    opt = ['Penalizar', 'Cambiar nombre', 'Eliminar competición']
    for option in opt:
        keyboard_opts.add(types.InlineKeyboardButton(option, callback_data='{}/{}'.format(option, int(cid))))
    return keyboard_opts

def get_keyboardPlayers(cid):
    keyboard_players = types.InlineKeyboardMarkup()
    path = db_path + str(cid)
    with open('%s/players.json' % path, 'r') as playersfile:
        data = json.load(playersfile)
        id_list = data['player_list']
        for pid in id_list:
            name = data[str(pid)]['name']
            keyboard_players.add(types.InlineKeyboardButton(name, callback_data='{}/{}'.format(pid, int(cid))))
    return keyboard_players


def get_keyboardPenal(cid, uid):
    keyboard_penal = types.InlineKeyboardMarkup()
    penals = ['2', '5', '10', '15']
    for elem in penals:
        keyboard_penal.add(types.InlineKeyboardButton(elem, callback_data='{}/{}/{}'.format(elem, cid, uid)))
    return keyboard_penal


def empty():
    return types.InlineKeyboardMarkup()