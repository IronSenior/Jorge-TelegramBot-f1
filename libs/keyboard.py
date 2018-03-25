from telebot import *
import json
from constantes import db_path

def keyboard_message(cid):
    mensaje = '''Estos son los equipos de la competicion y los pilotos de cada uno de ellos:
    Mercedes:%s
    Red Bull:%s
    Williams:%s
    Ferrari:%s
    McLaren:%s
    Force India:%s
    Toro Rosso:%s
    Lotus:%s
    Sauber:%s
    Marussia:%s''' %(team_members(cid, "mercedes"),
                    team_members(cid, "red_bull"),
                    team_members(cid, "williams"),
                    team_members(cid, "ferrari"),
                    team_members(cid, "mclaren"),
                    team_members(cid, "force_india"),
                    team_members(cid, "toro_rosso"),
                    team_members(cid, "lotus"),
                    team_members(cid, "sauber"),
                    team_members(cid, "marussia"))
    return mensaje

def team_members(cid, team):
    path = db_path + str(cid)
    pilotos = ""
    with open('%s/players.json' % (path), 'r') as playersfile:
        players = json.load(playersfile)
        for userid in players['player_list']:
            if team == players[str(userid)]['team']:
                pilotos += " " + players[str(userid)]['name']
    return pilotos


keyboard_team = types.InlineKeyboardMarkup()

keyboard_team.add(types.InlineKeyboardButton("Mercedes", callback_data = "mercedes"),
                 types.InlineKeyboardButton("Red Bull", callback_data = "red_bull"),
                 types.InlineKeyboardButton("Williams", callback_data = "williams"),
                 types.InlineKeyboardButton("Ferrari",  callback_data = "ferrari"),
                 types.InlineKeyboardButton("McLaren", callback_data = "mclaren"),
                 types.InlineKeyboardButton("Force India", callback_data = "force_india"),
                 types.InlineKeyboardButton("Toro Rosso", callback_data = "toro_rosso"),
                 types.InlineKeyboardButton("Lotus", callback_data = "lotus"),
                 types.InlineKeyboardButton("Sauber", callback_data = "sauber"),
                 types.InlineKeyboardButton("Marussia", callback_data = "marussia")
)
