#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

def join_in(user_id):
	with open('%s/players.json'%(path), 'r') as f:
		players = json.load(f)
		for player in players:
			if player.name =


