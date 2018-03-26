# -*-coding: utf-8 -*-
# !/usr/bin/env python
import json
from constantes import db_path
import aux


def add_admin(cid, uid):
    # Esta función añade como admin en la competición al creador de la misma.
    path = db_path + str(cid)
    with open('%s/admins.json' % (path), 'r') as outfile:
		comp = json.load(outfile)
		admin = comp['admin_id']
		admin.append(uid)

	with open('%s/admin.json' % (path), 'w') as outfile:
		json.dump(admin, outfile, indent=3)
    # El admin de la competición será el único capaz de borrar la misma y de terminar las carreras en curso o penalizar.
