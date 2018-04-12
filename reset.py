# -*-coding:utf-8 -*-
# ! /usr/bin/env python

import shutil
import libs.constantes as c

option = raw_input('¡Atención! Esto borrará la base de datos, ¿estás seguro de que quieres continuar?(Y/N)')
if option.upper() == 'Y':
    try:
        shutil.rmtree(c.db_path+'/')
    except():
        print('No hay base de datos')
