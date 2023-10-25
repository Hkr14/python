from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _start 
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import random
from random import randint


@Client.on_message(filters.command("key", ["/", "."]))
async def start(client, message):
    with open(file='plugins/usuarios/admins.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            data = message.text.split(" ", 2)
            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/key dias-id-credit</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("-")
            dia   = card[0]
            user= card[1]
        
            cre = card[2]

            key = 'RaceXt''-'+str(randint(1000,9000))+'-'f'{user}''-'f'{cre}'
            print(key)
            archivo.write('{}\n\n'.format(key))

            text = f"""<b>
❀ 𝗞𝗲𝘆 𝗨𝘀𝗲𝗿
        
❀ 𝗞𝗲𝘆 :  𝗞𝗲𝘆 𝗔𝗽𝗿𝗼𝘃𝗮𝗱 
❀ 𝗖𝗿𝗲𝗱𝗶𝘁𝗼 : <Code>{cre}</code>
❀ 𝗜𝗱 : <code>{user}</code>
❀ 𝗗𝗶𝗮𝘀 : <code>{dia}</code>
━━━━━━━━━━
Key :<code>/claim {key}</code> 
━━
❀ 𝗧𝗮𝗸𝗲𝗻 : <code>0.1 s</code>
━━━━━━━━━━
❀ 𝗖𝗿𝗲𝗮𝘁𝗲: <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[OWNER]</a></b></b>"""
            with open(file='plugins/usuarios/keys.txt',mode='r+',encoding='utf-8') as archivo:
                        x = archivo.readlines()
                        
                        archivo.write('{}\n\n'.format(key))

            await client.send_photo(message.chat.id, "https://thumbs.gfycat.com/NauticalYoungAfricancivet-size_restricted.gif" , f'{text}',
                    reply_markup=InlineKeyboardMarkup(
                [
                    [
                
                        InlineKeyboardButton("𝗖𝗹𝗮𝗶𝗺 ", url="https://t.me/RacextChk_bot")
                        
                    ]
                    
                ]

            )
            
        )
            
        else:
            return await message.reply(f'<b>⎚Este comando es para admins Y Owner</b>')



