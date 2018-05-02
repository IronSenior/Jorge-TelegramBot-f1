# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from constantes import db_path


def join_in(cid, uid, unick, uteam):
	# Permite al usuario unirse a la competición que hay creada en el grupo
	path = db_path + str(cid)
	with open('%s/players.json' % (path), 'r') as f:
		comp = json.load(f)
		players = comp['player_list']
		players.append(uid)

		data = {str(uid) : {'name': unick, 'team': uteam, 'lr_time': "None"}}
		comp.update(data)

	with open('%s/players.json' % (path), 'w') as f:
		json.dump(comp, f, indent=3)

	with open('%s/rank.json' % path, 'r') as rank:
		rankd=json.load(rank)
		data = {uid: 0}
		rankd.update(data)
	with open('%s/rank.json' %path, 'w') as rank:
		json.dump(rankd, rank, indent=3)

	return True


#Esta función devuelve False cuando se le intenta asignar a un piloto
#el equipo en el que ya está metido. Devuelve True cuando no es el mismo
#y en ese, cambia el campo 'team' del json por el nuevo equipo seleccionado
def change_team(cid, uid, uteam):
	path = db_path + str(cid)
	with open('%s/players.json' % (path), 'r') as f:
		players = json.load(f)
		if players[str(uid)]['team'] == uteam:
			return False
		else:
			players[str(uid)]['team'] = uteam

	with open('%s/players.json' % (path), 'w') as f:
		json.dump(players, f, indent = 3)
		return True


#Esta función devuelve True cuando hay 2 pilotos en un mismo equipo (equipo lleno)
#y False en el caso contrario (equipo con 1 o 2 huecos libres)
def team_full(cid, uteam):
	path = db_path + str(cid)
	n_pilotos = 0
	with open('%s/players.json' % (path), 'r') as f:
		players = json.load(f)
		for userid in players['player_list']:
			if uteam == players[str(userid)]['team']:
				n_pilotos += 1

	if (n_pilotos == 2):
		 return True
	else:
		 return False


def existe_user(uid, cid):
	#la función comprueba si ese usuario se ha unido o no a la competición anterirormente
	path = db_path + str(cid)
	with open('%s/players.json' % (path), 'r') as f:
		comp = json.load(f)
		players = comp['player_list']

		if uid in players:
			return True
		else:
			return False


def is_admin(cid, uid):
	# Comprueba si el usuario es uno de los administradores de la carrera
	path = db_path + str(cid)
	with open('%s/admins.json' % (path), 'r') as outfile:
		comp = json.load(outfile)
		admin = comp['admin_id']
		if uid in admin:
			return True
		else:
			return False

def penal_func(lst):  # Recibe una lista con la estructura: [competicion, jugador, penalizacion]
	compid, pid, penal = lst[1], lst[2], int(lst[0])
	path = db_path+compid
	with open('%s/players.json' % path, 'r') as outfile:
		comp = json.load(outfile)
		time = comp[pid]['lr_time']
		name = comp[pid]['name']

	# Transforma el string time en una lista para modificar por separado min, seg y mil.

	minutes = int(time.split(":")[0])
	seconds = int(time.split(":")[1])
	miles = int(time.split(":")[2])
	seconds = seconds + penal

	# Si los segundos totales sobrepasan los 60, se modificarán los minutos.
	if(seconds>=60):
		minutes = minutes + 1
		seconds = seconds - 60

	if(len(str(seconds))==1):
		time = str(minutes) + ":" + "0" + str(seconds) + ":" + str(miles)
	else:
		time = str(minutes) + ":" + str(seconds) + ":" + str(miles)


	with open('%s/players.json' % path, 'w') as outfile:
		comp[pid]['lr_time'] = time
		json.dump(comp, outfile, indent=3)
	# Añade la penalización al tiempo marcado por el jugador y se vuelca en el JSON.
	return ('{} ha sido penalizado con {} segundos'.format(name, str(penal)))

def have_comps(uid):
	#Comprueba si el usuario es administrador de alguna competición
	uid = str(uid)
	with open ('%sall_admins.json' %db_path, 'r') as outfile:
		all_admins = json.load(outfile)
		if uid in all_admins:
			return True
		else:
			return False
