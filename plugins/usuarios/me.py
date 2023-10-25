from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(["me","yo","my","myacc"], ["/", "."]))
async def register(_, m: Message):
    user=m.from_user.first_name
    user_id =m.from_user.id
    seller = [1924666696, 1924666696]
    
    
    owner = [1924666696]
    

    admin = [1924666696]
    
    if m.from_user.id in owner or m.from_user.id in owner:
        await m.reply(f"""<b>
⊗ 𝗨𝘀𝗲𝗿 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

⊗ 𝗡𝗮𝗺𝗲            <code>{user} </code>
⊗ 𝗜𝗱                   <code>{user_id}</code>
⊗ 𝗖𝗿𝗲𝗱𝗶𝘁𝘀           <code>Infinito</code>
⊗ 𝗦𝘁𝗮𝘁𝘂𝘀           <code>𝗖𝗿𝗲𝗮𝗱𝗼𝗿 [ 𖨆 ]</code>
⊗ 𝗣𝗹𝗮𝗻               <code>𝗢𝘄𝗻𝗲𝗿 [ 𖨆 ]</code>
━━━━━━━━━━━━━━━━━━━━━━
⊗ 𝗖𝗿𝗲𝗮𝘁𝗲 <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
    </b>""")
    
    
    elif m.from_user.id in seller:
        await m.reply(f"""<b>
⊗ 𝗨𝘀𝗲𝗿 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

❀𝗡𝗮𝗺𝗲           <code>{user} </code>
⊗ 𝗜𝗱                <code> {user_id}</code>
⊗ 𝗖𝗿𝗲𝗱𝗶𝘁𝘀              <code>1000</code>
⊗ 𝗦𝘁𝗮𝘁𝘂𝘀          <code>𝗦𝗲𝗹𝗹𝗲𝗿𝘀</code>
⊗ 𝗣𝗹𝗮𝗻              <code>𝗡𝘂𝘃𝘀</code>
━━━━━━━━━━━━━━━━━━━━━━
⊗ 𝗖𝗿𝗲𝗮𝘁𝗲 <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
    </b>""")
     
    else:
       
        with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
            x = archivo.readlines()

            if str(m.from_user.id) + '\n' in x:            
                await m.reply(f"""<b>
❀𝗨𝘀𝗲𝗿 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

⊗ 𝗡𝗮𝗺𝗲              <code>{user} </code>
⊗ 𝗜𝗱                   <code> {user_id}</code>
⊗ 𝗖𝗿𝗲𝗱𝗶𝘁𝘀              <code>10</code>
⊗ 𝗦𝘁𝗮𝘁𝘂𝘀             <code>𝗔𝗰𝘁𝗶𝘃𝗼</code>
⊗ 𝗣𝗹𝗮𝗻                 <code>𝗣𝗿𝗲𝗺𝗶𝘂𝗺</code>
━━━━━━━━━━━━━━━━━━━━━━
⊗ 𝗖𝗿𝗲𝗮𝘁𝗲 <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
            </b>""")
                    
            else:
                await m.reply(f"""<b>
⊗ 𝗨𝘀𝗲𝗿 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

❀𝗡𝗮𝗺𝗲              <code>{user} </code>
⊗ 𝗜𝗱                   <code> {user_id}</code>
⊗ 𝗖𝗿𝗲𝗱𝗶𝘁𝘀              <code>0</code>
⊗ 𝗦𝘁𝗮𝘁𝘂𝘀             <code>𝗨𝘀𝗲𝗿</code>
⊗ 𝗣𝗹𝗮𝗻                 <code>𝗙𝗿𝗲𝗲</code>
━━━━━━━━━━━━━━━━━━━━━━
⊗ 𝗖𝗿𝗲𝗮𝘁𝗲 <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
    </b>""")