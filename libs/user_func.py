# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from constantes import db_path


def join_in(uid, uname, cid):
	# Esta función permite al usuario unirse a la competición que hay creada en el grupo
	path = db_path + str(cid)
	with open('%s/players.json' % (path), 'r') as f:
		comp = json.load(f)
		players = comp['player_list']
		players.append(uid)

		data = {str(uid) : {'name': uname, 'position': 0, 'lr_time': "None"}}
		comp.update(data)

	with open('%s/players.json' % (path), 'w') as f:
		json.dump(comp, f)
	return True

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