from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
# import main

# @Client.on_message(filters.text & filters.private)
@Client.on_message(filters.new_chat_members)
async def entrar(Client, message):
    await message.reply_text(f"""<b>
⎚ Bienvedo {message.from_user.first_name}
⎚ Me llamo  <a href="tg://resolve?domain=RaceXtChkBot">RaceXtChk</a>
⎚ Puedes usarme escribe <code>/start</code>
⎚ Puedes Ver los Precios Escribe <code>/buy</code>
</b>""")
    
@Client.on_message(filters.left_chat_member)
async def end(Client, message):
    await message.reply_text(f"""<b>
⎚ Hasta luego numero <code>{message.from_user.id}</code>
⎚ vuelve pronto <3</b>
""")