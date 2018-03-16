# -*-coding: utf-8 -*-
# !/usr/bin/env python
import json
from constantes import db_path


def add_time(cid, uid, time):
    path = db_path + str(cid)
    if is_time(time):
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
            json.dump(comp, outfile)
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
    time.split(':')
    milis = 1000*(60*int(time[0])+int(time[1]))+int(time[3])
    return milis
