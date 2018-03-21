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

def existe_comp(cid):
	#La función comprueba si hay una competición creada en ese grupo
	#Para ello revisa las ids de las competiciones que hay creadas
	with open('%scomps.json'%(db_path), 'r') as jsonfile:
		comps = json.load(jsonfile)['comps']
		if cid in comps:
			return True
		else:
			return False

def delete_comp(cid):
	#Esta función borra la competición que se haya creado en ese grupo
	#Para ello busca en el bucle la id de la lista del comps.json que coincide con la id del chat
	#Cuando la encuentra borra ese elemento de la lista
	with open('%scomps.json'%(db_path), 'r') as compsfile:
		comps = json.load(compsfile)
		for com_id in comps["comps"]:
			if cid == int(com_id):
				comps["comps"].remove(com_id)
	#Una vez borrada la id sobreescribe el diccionario de python en el comps.json
	with open('%scomps.json'%(db_path), 'w') as compsfile:
		json.dump(comps, compsfile, indent=3)
	#Por ultimo borra la carpeta que se crea cuando se crea una competicion y su contenido
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


