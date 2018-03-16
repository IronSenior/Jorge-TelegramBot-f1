# -*-coding: utf-8 -*-
import json
from constantes import db_path
'''
Deberíamos dejar db_path definido en un archivo concreto e importarlo
en el resto, tenerlo en varios por separado es un coñazo
'''


def add_time(cid, uid, time):
    path = db_path + str(cid)
    if is_time(time):
        with open('%s/players.json' % path, 'r') as outfile:
            comp = json.load(outfile)
            players = comp['player_list']
            if uid not in players:
                return False
        with open('%s/players.json' % path, 'w') as outfile:
            comp[str(uid)]['lr_time'] = time
            json.dump(comp, outfile)
        return True
    else:
        return False


def is_time(time):
    lst = time.split(':')
    print lst
    if len(lst) == 3:
        return lst[0].isdigit() & lst[1].isdigit() & lst[2].isdigit()
    else:
        return False
