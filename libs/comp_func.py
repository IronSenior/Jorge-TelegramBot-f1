#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

def create(chat_id):
	path = "/home/pepe/Escritorio/Bot-V2.0/DB/%i"%(chat_id)
	try:
		os.mkdir(path)
	except:
		return False

	with open('%s/players.json'%(path), 'w') as outfile:
		data = {"players": {}}
		json.dump(data, outfile)

	return True
