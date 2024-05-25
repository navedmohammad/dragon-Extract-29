#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6936886870:AAEPSWnNkdf0LyvviM2GGx0VfI3i7s4qN9I")
    API_ID = int(os.environ.get("API_ID", "20483216"))
    API_HASH = os.environ.get("API_HASH", "2518170d3dd939b3f2893cb0aae805c4")
    AUTH_USERS = os.getenv("AUTH_USERS", "5565741405")

