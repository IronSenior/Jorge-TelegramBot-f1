# -*-coding: utf-8 -*-
# !/usr/bin/env python
import json
from constantes import db_path
import aux


def penal_func(penal, uid):

    if is_time(penal):
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
            time = time + penal
            json.dump(comp, outfile, indent=3)
        # Añade la penalización al tiempo marcado por el jugador, guardado en el archivo
        # cargado y lo vuelca en el JSON.
        return True
    else:
        return False
