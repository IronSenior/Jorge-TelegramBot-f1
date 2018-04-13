# -*-coding: utf-8 -*-
# !/usr/bin/env python
import json
from constantes import db_path
import aux


def add_time(cid, uid, time):
    path = db_path + str(cid)
    time = time.upper()
    if is_time(time) or time == 'DSQ':
        # Comprueba si la cadena está en el formato adecuado.
        with open('%s/players.json' % path, 'r') as outfile:
            comp = json.load(outfile)
            players = comp['player_list']
        # Carga el JSON y almacena la lista de jugadores en players para comprobar
        # si el usuario es miembro de la competición.
            if uid not in players:
                return False
        with open('%s/players.json' % path, 'w') as outfile:
            comp[str(uid)]['lr_time'] = time
            json.dump(comp, outfile, indent=3)
        # Modifica el campo correspondiente al tiempo del usuario en el archivo
        # cargado y lo vuelca en el JSON.
        return True
    else:
        return False


def is_time(time):
    lst = time.split(':')
    # Divide la cadena en ':', si la lista resultante tiene 3 elementos y todos
    # son números devuelve True, en caso contrario devuelve False.
    if len(lst) == 3:
        return lst[0].isdigit() & lst[1].isdigit() & lst[2].isdigit()
    else:
        return False


def to_milis(time):
    # Recibe una cadena en formato M:S:mm y devuelve un número entero de milésimas.
    # La usaremos para comparar con más comodidad.
    lst = time.split(':')
    milis = 1000*(60*int(lst[0])+int(lst[1]))+int(lst[2])
    return milis


def list_times(cid):
    # Devuelve una lista con los tiempos(ordenados) y un diccionario tiempo:id
    # Lo hacemos así porque los diccionarios no tienen índices.
    with open('%s/players.json' % (db_path+str(cid)), 'r')as rankfile:
        data = json.load(rankfile)
        dct = {}
        lst = []
        for key in data:
            if key.isdigit() and data[key]['lr_time'] != 'DSQ':
                dct.update({to_milis(data[key]['lr_time']): key})
                lst.append(to_milis(data[key]['lr_time']))
    lst = aux.sort(lst)
    return lst, dct


def give_points(cid):
    points = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)  # Puntuaciones según posición
    lst, dct = list_times(cid)
    with open('%s/rank.json' % (db_path+str(cid)), 'r') as rankfile:
        data = json.load(rankfile)
        for time in lst:
            index = lst.index(time)  # Al coger el índice estamos estableciendo el orden
            if index <= 10:
                data[dct[time]] += points[index]
    with open('%s/rank.json' % (db_path+str(cid)), 'w') as rankfile:
        json.dump(data, rankfile, indent=3)

def has_time(cid, uid):
    #Esta función comprueba si un usuario ha metido su tiempo
    with open('%s/players.json' % (db_path+str(cid)), 'r')as playersfile:
        players = json.load(playersfile)
        player_time = players[uid]["lr_time"]

        if (player_time != "0") and (player_time != "NONE"):
            return True


def all_times_defined(cid):
    #Esta función comprueba si todos los jugadores han metido su tiempo
    with open('%s/players.json' % (db_path+str(cid)), 'r')as playersfile:
        players = json.load(playersfile)

        for player in players["player_list"]:
            if not has_time(cid, player):
                return False
        return True

