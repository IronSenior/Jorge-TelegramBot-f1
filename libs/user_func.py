# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from constantes import db_path


def join_in(cid, uid, unick, uteam):
	# Esta función permite al usuario unirse a la competición que hay creada en el grupo
	path = db_path + str(cid)
	with open('%s/players.json' % (path), 'r') as f:
		comp = json.load(f)
		players = comp['player_list']
		players.append(uid)

		data = {str(uid) : {'name': unick, 'team': uteam, 'position': 0, 'lr_time': "None"}}
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
