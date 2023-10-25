import json
import requests
import time
import asyncio

from asyncio import sleep
from pyrogram import Client, filters
#from configs import Config                         # aqui dice que de configs importe lan classe config
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(["buy"], ["/", "."]))
async def binio(_, m: Message):
    await m.reply(f'''
⭕RaceXtchk_WEB Y BOT⭕
    〰〰GATES 〰〰 
----------------------------
✅MEDELLIN
⚠AMAZON MX
⚠AMAZON CO
⚠AMAZON IT
⚠AMAZON BR
✅MASS
✅ROMA
✅RUSIA
✅PAYPAL
✅RACECHK
✅BOGOTA
✅MANCHESTER
------------------------
   ⭕PRECIOS⭕
💰1 semana 150 mx  
💰15 dias 220 mx
💰30 dias 300 mx
---------------------------
🏦METODOS DE PAGO 🏦
---------------------------
✅TRANFERENCIA MX
🪪646180146011951001
🏦STP
💰Sarce
--------------------''')