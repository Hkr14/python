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
ADMIN_ID =  1924666696

@Client.on_message(filters.command(["credi"], ["/", "."]))
async def myacc(_, m: Message):
    if m.from_user.id != ADMIN_ID:# Reemplaza ADMIN_ID con el ID del usuario administrador
        await m.reply("Solo el administrador puede utilizar este comando.")
        return

    args = m.text.split()
    if len(args) != 3:
        await m.reply("Formato incorrecto. Usa /setrank [ID del usuario] [rango]")
        return

    user_id = int(args[1])
    rank = args[2]

    # Añade la lógica para verificar si el usuario es válido o si el rango es válido aquí

    with open("ranks.txt", "a") as f:
        f.write(f"{user_id}:{rank}\n")

    await m.reply(f"El rango de {user_id} ha sido establecido en {rank}.")
