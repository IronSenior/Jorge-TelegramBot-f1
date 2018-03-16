#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from constantes import db_path

#Obviamente este path es provisional y en cada equivo debe cambiar (se pondrá el definitivo en el servidor)

def create_comp(cid):
	#Primero agragará la competición al archivo comps.json
	with open('%scomps.json'%(db_path), 'r') as jsonfile:
		comps = json.load(jsonfile)
		comps["comps"].append(cid)

	with open('%scomps.json'%(db_path), 'w') as outfile:
		json.dump(comps, outfile)

	#La función creará una carpeta donde se van a almacenar todos los datos de esa competición
	#El path será la carpeta DB que hay en el mismo directorio que bot.py
	path = db_path + str(cid)
	os.mkdir(path)

	#Crea también los archivos json base que necesita la competición
	with open('%s/players.json'%(path), 'w') as outfile:
		data = { 'player_list' : [],}

		json.dump(data, outfile)

def existe_comp(cid):
	#La función comprueba si hay una competición creada en ese grupo
	#Para ello revisa las ids de las competiciones que hay creadas
	with open('%scomps.json'%(db_path), 'r') as jsonfile:
		comps = json.load(jsonfile)['comps']
		if cid in comps:
			return True
		else:
			return False


