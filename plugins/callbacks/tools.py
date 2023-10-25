from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _Call_Tools, _Call_Gateways_buttons

@Client.on_callback_query(filters.regex("Tools"))
async def tools(client, message):
    await message.edit_message_text(_Call_Tools, reply_markup= _Call_Gateways_buttons)
 
from pyrogram import Client, filters
from pyrogram.types import Message    
from pulpos.plantillas import _ifgates, _botongates

@Client.on_callback_query(filters.regex("Gates"))
async def Gates(client, message):
    await message.edit_message_text(_ifgates, reply_markup= _botongates)
    return
  
  
from pyrogram import Client, filters
from pyrogram.types import Message    
from pulpos.plantillas import _gauth, _botongatesas

@Client.on_callback_query(filters.regex("Auth"))
async def Auth(client, message):
    await message.edit_message_text(_gauth, reply_markup= _botongatesas)
    return 
  
from pyrogram import Client, filters
from pyrogram.types import Message    
from pulpos.plantillas import _gcharged, _botongatesch

@Client.on_callback_query(filters.regex("Charged"))
async def Charged(client, message):
    await message.edit_message_text(_gcharged, reply_markup= _botongatesch)
    return 

from pyrogram import Client, filters
from pyrogram.types import Message    
from pulpos.plantillas import _gmass, _botongatesmas 

@Client.on_callback_query(filters.regex("Mass"))
async def Mass(client, message):
    await message.edit_message_text(_gmass, reply_markup= _botongatesmas)
    return   