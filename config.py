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
    bot_token="6365930995:AAHMGYrrkZxCbOTSDj9NWbHjdnEgWfg9dwQ", # API_KEY 
    api_hash="fe77fbf0cae9f7f5ece37659e2466cf1", # UserBot api_hahs
    api_id="21627756" # UserBot api_id 
)

datas, apiV = databesas(), TempMailApi()


