import random
from pyrogram import Client, filters

from datos import admin

FILE_PATH = "plugins/usuarios/keys.txt"

app = Client

@app.on_message(filters.command("claim",["/", "."]))
async def claim_key(client, message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:

            zipcode = message.text[len('/claim '):]
            
            if len(zipcode) < 2:
                    return await message.reply("<b>⎚ Usar <code>/claim Kimura-3739-xxxxx</code></b>")
            if not zipcode:
                return await message.reply("<b>⎚ Usar <code>/claim RaceXt-3739-xxxxx</code></b>")
                
            with open(FILE_PATH, "r") as f:
                keys = f.read().splitlines()

            key = keys.pop(random.randint(0, len(keys)-1))
            print(key+' aprovada 🟢')
        

            if len(keys) == 0:
                await message.reply("<b>⎚ Key tomada por otro usuario.</b>")
                return

            
            with open(FILE_PATH, "w") as f:
                f.write("\n".join(keys))


            with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
                        x = archivo.readlines()
                        
                        archivo.write('{}\n'.format(message.from_user.id))

            text=f"""<b>
❀ 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗣𝗹𝗮𝗻 

❀ 𝗦𝘁𝗮𝘁𝘂𝘀         𝗞𝗲𝘆 𝗔𝗽𝗿𝗼𝘃𝗮𝗱𝗮 🟢
❀ 𝗞𝗲𝘆            <code>•RaceXtChk claim </code>
❀ 𝗨𝘀𝘂𝗮𝗿𝗶𝗼     <code>{message.from_user.first_name} </code>
❀ 𝗜𝗱               <code> {message.from_user.id}</code> 
❀ 𝗘𝘀𝘁𝗮𝘁𝘂𝘀      <code>Premium </code>  
❀ 𝗧𝗮𝗸𝗲𝗻   <code>0.1 s</code>
━━━━━━━━━━
❀ 𝗖𝗿𝗲𝗮𝘁𝗲: <b><a href="tg://resolve?domain=SarceDev[Owner]">OWNER</a></b></b>"""
            await client.send_video(message.chat.id, "https://i.gifer.com/8TcO.gif" , f'{text}')
        
        else:
            return await message.reply(f'<b>⎚ Registrese <code>/register</code></b>')
    



