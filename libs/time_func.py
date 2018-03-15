# -*-coding: utf-8 -*-
import json
from comp_func import db_path
'''
Deberíamos dejar db_path definido en un archivo concreto e importarlo
en el resto, tenerlo en varios por separado es un coñazo
'''


def add_time(cid, uid, time):
    path = db_path + cid
    if is_time(time):
        with open('%splayers.json' % path, 'r') as outfile:
            comp = json.load(outfile)
            players = comp['player_list']
            if uid not in players:
                return False
        with open('%splayers.json' % path, 'w') as outfile:
            comp[str(uid)]['lr_time'] = time
            json.dump(comp, outfile)
        return True


def is_time(time):
    lst = time.split(':')
    print lst
    if len(lst) == 3:
        return lst[0].isdigit() & lst[1].isdigit() & lst[2].isdigit()
    else:
        return False
