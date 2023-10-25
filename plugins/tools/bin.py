import requests 
from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _cmdbotons, _cmd

@Client.on_message(filters.command(["bin"], ["/", "."]))
async def cmds(client, message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            BIN = message.text[len("/bin"): 11]

            if len(BIN) < 7:
                return await message.reply("<b>❀ 𝗨𝘀𝗮𝗿 <code>/bin 456789</code></b>")
            if not BIN:
                return await message.reply("<b>❀ 𝗨𝘀𝗮𝗿 <code>/bin 456789</code></b>")
            inputm = message.text.split(None, 1)[1]
            bincode = 6
            BIN = inputm[:bincode]
            req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()
            if 'bin' not in req:
                await message.reply_text(f'<b>❀ 𝗕𝗶𝗻 ⇾ no encontrado <code>{BIN} ❌</code></b>')
                
            else:
                brand = req['brand']
                country = req['country']
                country_name = req['country_name']
                country_flag = req['country_flag']
                country_currencies = req['country_currencies']
                bank = req['bank']
                level = req['level']
                typea  = req['type']

                await message.reply_text(f"""
               <b>
❀ 𝗕𝗶𝗻 ⇾  <code>{BIN}</code>  <b>{country}|{country_flag}|{country_name}</b>

<b>❀ 𝗦𝘁𝗮𝘁𝘂𝘀 ⇾ Aprovado ✅</b>
❀ 𝗗𝗮𝘁𝗮 ⇾ {brand}-{typea}-{level}
<b>❀ 𝗕𝗮𝗻𝗸</b> ⇾  {bank}

<b>❀ 𝗧𝗮𝗸𝗲 </b>⇾<code> 1.6</code> (segund)
━━━━━━━━━━━━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[OWNER]</a></b>
</b>
                """)
    
        else:
            return await message.reply(f'<b>❀ Registrese <code>/register</code></b>')
    