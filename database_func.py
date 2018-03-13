#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3

class database_functions():
    def write_on_db(self,query):
        try:
            db_file = sqlite3.connect("database.db")
            cursor = db_file.cursor()
        except:
            print "Error con la base de datos"

        cursor.execute(query)
        cursor.commit()
        cursor.close()

    def competiciones(self):
        query_competiticiones = '''CREATE TABLE IF NO EXISTS COMPETICIONES
            (ID INT PRIMARY KEY			NOT NULL,
                NAME 				TEXT 	NOT NULL)'''
        self.write_on_db(query_competiticiones)


    def crear_competicion(self,competition_data):
        print ("Crear competicion")
        self.competiciones()
        name = str(competition_data[0])
        chat_id = int(competition_data[1])
        create_table_query = '''CREATE TABLE ?
                            (ID INT PRIMARY KEY			NOT NULL,
                            PLAYER_ID			TEXT 	NOT NULL,
                            C1 					TEXT 	NOT NULL,
                            C2 					TEXT 	NOT NULL,
                            C3 					TEXT 	NOT NULL,
                            C4 					TEXT 	NOT NULL,
                            C5 					TEXT 	NOT NULL,
                            C6  				TEXT 	NOT NULL,
                            C7 					TEXT 	NOT NULL,
                            C8 					TEXT 	NOT NULL,
                            C9 					TEXT 	NOT NULL,
                            C10 				TEXT 	NOT NULL,
                            C11 				TEXT 	NOT NULL,
                            C12  				TEXT 	NOT NULL,
                            C13 				TEXT 	NOT NULL,
                            C14 				TEXT 	NOT NULL,
                            C15 				TEXT 	NOT NULL,
                            C16    				TEXT 	NOT NULL,
                            C17 				TEXT 	NOT NULL,
                            C18 				TEXT 	NOT NULL,
                            C19 				TEXT 	NOT NULL,
                            TOTAL_SCORE 		INT 	NOT NULL)''' % (name)

        write_competitions_query = "INSERT INTO COMPETICIONES (ID, NAME) VALUES (%i, '%s')"%(chat_id, str(name))


