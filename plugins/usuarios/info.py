
import os
from datos import *
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["info"], ["/", "."]))
async def who_is(client, message):
    

    status_message = await message.reply_text(
        "`⊗  𝗕𝘂𝘀𝗰𝗮𝗻𝗱𝗼 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝗰𝗶𝗼𝗻`"
    )
    await status_message.edit(
        "`⊗  𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝗰𝗶𝗼𝗻 𝗲𝗻𝗰𝗼𝗻𝘁𝗿𝗮𝗱𝗮.`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    last_name = from_user.last_name or "<b>None</b>"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesn't Have A Valid DP]"
    message_out_str = f"""<b>❀ 𝗨𝘀𝗲𝗿 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

⊗  𝗡𝗼𝗺𝗯𝗿𝗲 : {from_user.first_name}    
⊗  𝗜𝗱 : <code>{from_user.id}</code>
⊗  𝗔𝗹𝗶𝗮𝘀 : @{username}
━━━━━━━━━━
⊗  Taken : <code>6.0 s</code>
⊗  𝗖𝗿𝗲𝗮𝘁𝗲: <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[OWNER]</a></b></b>
   </b> """
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            InlineKeyboardButton('𝗘𝗫𝗜𝗧', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            InlineKeyboardButton('E X I T', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
    await status_message.delete()
