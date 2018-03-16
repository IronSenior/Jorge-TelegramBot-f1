import os
import json


def inicio_bot():
	os.mkdir("DB")

	with open('./DB/comps.json', 'w') as outfile:
		data = {"comps": []}
		json.dump(data, outfile)

	print "Carpeta y archivo de inicio creados"

inicio_bot()