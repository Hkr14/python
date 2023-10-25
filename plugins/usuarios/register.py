from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(["register"], ["/", "."]))
async def register(_, m: Message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(m.from_user.id) + '\n' in x:
            return await m.reply(f'<b>❀ 𝗨𝘀𝘂𝗮𝗿𝗶𝗼 𝘆𝗮 𝗲𝘀𝘁𝗮 𝗿𝗲𝗴𝗶𝘀𝘁𝗿𝗮𝗱𝗼.</code></b>')
        else:
            archivo.write('{}\n'.format(m.from_user.id))
            return await m.reply(f'<b>❀𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗼 𝗖𝗼𝗿𝗿𝗲𝗰𝘁𝗼 <code>{m.from_user.id} </code></b>')