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
		if uid not in players:
			players.append(uid)
		else:
			return False
	with open('%s/players.json' % (path), 'w') as f:
		json.dump(comp, f)
	return True
