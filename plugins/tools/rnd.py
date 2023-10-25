import requests 
from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _cmdbotons, _cmd

@Client.on_message(filters.command("rand"))
async def cmds(client, message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            api = requests.get("https://randomuser.me/api/?nat=country&inc=name,location").json()

            mr = api["results"][0]["name"]["title"]
            nombre = api["results"][0]["name"]["first"]
            last = api["results"][0]["name"]["last"]
            loca = api["results"][0]["location"]["street"]["name"]
            nm = api["results"][0]["location"]["street"]["number"]
            city = api["results"][0]["location"]["city"]
            state = api["results"][0]["location"]["state"]
            country = api["results"][0]["location"]["country"]
            postcode = api["results"][0]["location"]["postcode"]
            latitude = api["results"][0]["location"]["coordinates"]["latitude"]
            longitude = api["results"][0]["location"]["coordinates"]["longitude"]
            
            await message.reply(f"""
        <b> 
⊗ 𝗙𝗮𝗸𝗲 𝗮𝗱𝗱𝗿𝗲𝘀
⊗ 𝗡𝗮𝗺𝗲 : <code>{mr} {nombre} {last}</code>
⊗ 𝗦𝘁𝗿𝗲𝗲𝘁 :  <code>{state}</code>
⊗ 𝗖𝗶𝘁𝘆 : <code>{city}</code>
⊗ 𝗦𝘁𝗮𝘁𝗲:<code> {loca} {nm}</code>
⊗ 𝗭𝗶𝗽 : <code> {postcode}</code>
⊗ 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 : <code>{country}</code>
⊗ 𝗖𝗵𝗲𝗸𝗲𝗱 𝗯𝘆 <code> @{message.from_user.username}[Rnd]</code>
━━━━━━━━━━━━━━
⊗ 𝗖𝗿𝗲𝗮𝘁𝗲 <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
 </b>""")
        else:
            return await message.reply(f'<b>⊗ Registrese <code>/register</code></b>')
    