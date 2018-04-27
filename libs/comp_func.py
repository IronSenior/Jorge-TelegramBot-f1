#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import shutil
from constantes import db_path

#Obviamente este path es provisional y en cada equivo debe cambiar (se pondrá el definitivo en el servidor)

def create_comp(cid):
	#Primero agregará la competición al archivo comps.json
	with open('%scomps.json'%(db_path), 'r') as jsonfile:
		comps = json.load(jsonfile)
		comps["comps"].append(cid)

	with open('%scomps.json'%(db_path), 'w') as outfile:
		json.dump(comps, outfile, indent=3)

	#La función creará una carpeta donde se van a almacenar todos los datos de esa competición
	#El path será la carpeta DB que hay en el mismo directorio que bot.py
	path = db_path + str(cid)
	os.mkdir(path)

	#Crea también los archivos json base que necesita la competición
	with open('%s/players.json'%(path), 'w') as outfile:
		data = { 'player_list' : [],}

		json.dump(data, outfile, indent=3)

	with open('%s/rank.json' %path, 'w') as outfile:
		data={}
		json.dump(data, outfile, indent=3)

	with open('%s/race.json' %path, 'w') as outfile:
		data={"race": 1}
		json.dump(data, outfile, indent=3)

	with open('%s/admins.json' %path, 'w') as outfile:
		data={"admin_id": []}
		json.dump(data, outfile, indent=3)

def existe_comp(cid):
	#La función comprueba si hay una competición creada en ese grupo
	#Para ello revisa las ids de las competiciones que hay creadas
	with open('%scomps.json'%(db_path), 'r') as jsonfile:
		comps = json.load(jsonfile)['comps']
		if cid in comps:
			return True
		else:
			return False

def delete_comp(cid, uid):
	#Esta función borra la competición que se haya creado en ese grupo
	#Para ello busca en el bucle la id de la lista del comps.json que coincide con la id del chat
	#Cuando la encuentra borra ese elemento de la lista
    with open('%scomps.json'%db_path, 'r') as compsfile:
        comps = json.load(compsfile)
        for com_id in comps["comps"]:
            if int(cid) == com_id:
                comps["comps"].remove(com_id)
	#Una vez borrada la id sobreescribe el diccionario de python en el comps.json
    with open('%scomps.json'%db_path, 'w') as compsfile:
        json.dump(comps, compsfile, indent=3)

    with open('%sall_admins.json' % db_path, 'r') as adminfile:
        admins = json.load(adminfile)
        del admins[str(uid)][str(cid)]

    with open('%sall_admins.json' % db_path, 'w') as adminfile:
        json.dump(admins, adminfile, indent=3)
    path = db_path + str(cid)
    shutil.rmtree(path)

def get_race_bycomp(cid):
	#Devuelve la información del circuito que toca correr en ese grupo
	path = db_path + str(cid)
	with open('%s/race.json'%(path), 'r') as racefile:
		races = json.load(racefile)
		race = races['race']

	with open('%sgp.json'%(db_path), 'r') as gpfile:
		gp = json.load(gpfile)

		actual_gp = gp[str(race)]

		return actual_gp

def plus_race_bycomp(cid):
	#Suma 1 al circuito de la competición
	path = db_path + str(cid)
	with open('%s/race.json'%(path), 'r') as racefile:
		races = json.load(racefile)
		races['race'] += 1

	with open('%s/race.json'%(path), 'w') as outfile:
		json.dump(races, outfile)

def add_admin(cid, uid, cname):
	# Esta función añade como admin en la competición al creador de la misma.
	#Primeramente añade el administrador al json de la competición
	path = db_path + str(cid)
	with open('%s/admins.json' % (path), 'r') as outfile:
		comp = json.load(outfile)
		comp['admin_id'].append(uid)

	with open('%s/admins.json' % (path), 'w') as outfile:
		json.dump(comp, outfile, indent=3)

	#Ahora se añade la id del admin al json general donde se almacenan todos los
	#administradores con sus respectivas competiciones y nombres de grupo
	with open('%sall_admins.json' % (db_path), 'r') as outfile:
		all_admins = json.load(outfile)
		uid = str(uid)
		#If y Elif permite que si un mismo usuario es administrador de varios chats,
		#en el json se guarden varios cid y cname para el mismo uid
		if uid not in all_admins:
			all_admins.update ({uid : {cid : cname}})
		elif uid in all_admins:
			all_admins[uid].update ({cid : cname})

	with open('%sall_admins.json' % (db_path), 'w') as outfile:
		json.dump(all_admins, outfile, indent = 3)
	# El admin de la competición será el único capaz de borrar la misma y de terminar las carreras en curso o penalizar.

def comp_list():
	with open('%scomps.json' % db_path, 'r') as compfile:
		lst = json.load(compfile)['comps']
		ret = []
		for item in lst:
			ret.append(str(item))
	return ret

def name(adminid, compid, newname):
	with open('%sall_admins.json' % db_path, 'r') as adminfile:
		data = json.load(adminfile)
	data[adminid][compid] = newname
	with open('%sall_admins.json' % db_path, 'w') as adminfile:
		json.dump(data, adminfile, indent=3)