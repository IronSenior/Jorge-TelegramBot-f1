# -*-coding: utf-8 -*-
# !/usr/bin/env python
import json
from constantes import db_path
import aux


def penal_func(penal, uid):
        # Primero se comprueba que el usuario que va a penalizar sea el admin.
	with open('%s/admins.json' % (path), 'r') as outfile:
		comp = json.load(outfile)
		admin = comp['admin_id']
		if uid not in admin:
			return False

        with open('%s/players.json' % path, 'r') as outfile:
            comp = json.load(outfile)
            players = comp['player_list']
        # Carga el JSON y almacena la lista de jugadores en players para comprobar
        # si el usuario es miembro de la competición.
            if uid not in players:
                return False
        # Carga el JSON y adquiere el tiempo del jugador al que se va a penalizar.

        with open('%s/players.json' % path, 'r') as outfile:
            comp = json.load(outfile)
            time = comp[str(uid)]['lr_time']

        # Transforma el string time en una lista para modificar por separado min, seg y mil.

        minutes = time.split(":")[0]
        seconds = time.split(":")[1]
        miles = time.split(":")[2]
        seconds = seconds + penal

        # Si los segundos totales sobrepasan los 60, se modificarán los minutos.
        if(seconds>=60):
            minutes = minutes + 1
            seconds = seconds - 60

        if(len(str(segundos))==1):
            time = str(minutes) + ":" + "0" + str(seconds) + ":" + str(miles)
        else
            time = str(minutes) + ":" + str(seconds) + ":" + str(miles)


        with open('%s/players.json' % path, 'w') as outfile:
            comp[str(uid)]['lr_time'] = time
            json.dump(comp, outfile, indent=3)
        # Añade la penalización al tiempo marcado por el jugador y se vuelca en el JSON.
