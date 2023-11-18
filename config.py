from pyrogram import Client
from Plugin.databesas import *
from Plugin.api import *
import os 

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 21627756))

    API_HASH = os.environ.get("API_HASH", "fe77fbf0cae9f7f5ece37659e2466cf1")

SUDO = 6673736816 # admin or sudo id
CHANNLS_BOT = ['UI_XB'] # bot channls 


if not os.path.exists('./.session'):
    os.mkdir('./.session')

if not os.path.exists('./.databesas'):
    os.mkdir('./.databesas')

app = Client(
    '.session/rad',
    bot_token= TG_BOT_TOKEN, # API_KEY 
    api_hash= API_HASH, # UserBot api_hahs
    api_id= API_ID # UserBot api_id 
)

datas, apiV = databesas(), TempMailApi()


