from datos import admin
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(["addpre"], ["/", "."]))
async def addpre(_, m: Message):
    with open('plugins/usuarios/admins.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(m.from_user.id) + '\n' in x:
            data = m.text.split(" ", 2)
            if len(data) < 2:
                await m.reply_text("<b>❀ Usar <code>/addpre dias-id-credit</code></b>")
                return
            
            ccs  = data[1]
            card = ccs.split("-")
            hola   = card[0]

            with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
                x = archivo.readlines()
                archivo.write('{}\n'.format(hola))

                await m.reply(f'<b>El usuario <code>{hola}</code> ahora es premium </b>')
        else:
            return await m.reply(f'<b>❀ Este comando es para admins</b>')
