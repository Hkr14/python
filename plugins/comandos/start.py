from datos import video
from datos import *
from pyrogram import Client, filters,enums
from pyrogram.types import Message
from pulpos.plantillas import _start
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import asyncio

@Client.on_message(filters.command("start", ["/", "."]))
async def start(client, message):
    await message.reply_chat_action(enums.ChatAction.TYPING)
    m=await message.reply_sticker("CAACAgUAAxkBAAIFNGJSlfOErbkSeLt9SnOniU-58UUBAAKaAAPIlGQULGXh4VzvJWoeBA")
    await asyncio.sleep(1.5)
    await m.delete()
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
      x = archivo.readlines()
      if str(message.from_user.id) + '\n' in x:
       await client.send_video(message.chat.id, video=video, caption=_start)

      else:
            return await message.reply(f'<b>⎚ Registrese <code>/register</code></b>')
    