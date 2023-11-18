from pyrogram import Client
from Plugin.databesas import *
from Plugin.api import *
import os 

SUDO = 6673736816 # admin or sudo id
CHANNLS_BOT = ['UI_XB'] # bot channls 


if not os.path.exists('./.session'):
    os.mkdir('./.session')

if not os.path.exists('./.databesas'):
    os.mkdir('./.databesas')

app = Client(
    '.session/rad',
    bot_token=TG_BOT_TOKEN, # API_KEY 
    api_hash=API_HASH, # UserBot api_hahs
    api_id=API_ID # UserBot api_id 
)

datas, apiV = databesas(), TempMailApi()


