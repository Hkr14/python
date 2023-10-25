import json
import requests
import time
import asyncio
import pyrogram
from asyncio import sleep
from pyrogram import Client, filters
#from configs import Config                         # aqui dice que de configs importe lan classe config
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

import requests
import random

def get_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = response.json()["value"]
    return joke

@Client.on_message(filters.command(["risa"], ["/", "."]))
async def myacc(_, m: Message):
    joke = get_joke()
    await m.reply_text(joke)

