import json
import html
from values import *
import requests
import time
import platform
import asyncio
from bs4 import BeautifulSoup
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



@Client.on_message(filters.command(["sh"], ["/", "."]))
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
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
              'Accept': 'application/json, text/plain, */*',
              'Accept-Language': 'es-ES,es;q=0.8,en-gb;q=0.5,en;q=0.3',
              'Referer': 'https://us.dockers.com/collections/sale-clothing/products/v-neck-tee-shirt-slim-fit-a17590004?objectId=41433636110497&activeIndex=shopify_products_price_asc&queryId=cb341f8f73871762a8f166c6b7931652',
              'Origin': 'https://us.dockers.com',
              'Alt-gbed': 'us.dockers.com',
              'Connection': 'keep-alive',
            # 'Cookie': 'AKA_A2=A; WCXSID=3045454278153918967279757603; TLTSID=00003045454278153918967279757603; ajs_anonymous_id=%22b077bbcf-7f51-4a94-8c2d-52a4629a8f5d%22; AMCV_B7FF1CFE5330995F0A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C19408%7CMCMID%7C61365190381223431572855965869978278853%7CMCAAMLH-1677452526%7C4%7CMCAAMB-1677452526%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1676854927s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19415%7CvVersion%7C4.4.0; RT="z=1&dm=dockers.com&si=1aac40a9-df76-4ArKvohoDv1EnBbQtxfDP32BzpTyM2QTm1y9rjNs3Rysgu4Ku5rK2nKbP1GVGo5kxZFZ7x7iaHzLwGijEg9QXyXJUWZA31S=110tfi7t&cl=9f7&ul=9fm&hd=af1"; AMCVS_B7FF1CFE5330995F0A490D45%40AdobeOrg=1; _gcl_au=1.1.1867624994.1676847727; s_cc=true; s_sq=leviseulevi-gb-prod%252Clevilsalse-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253DGlobal%252520Country%252520Picker%2526link%253DUnited%252520States%2526region%253Ddata-drilldown-5%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; keep_alive=dfeb2922-c784-4ArKvohoDv1EnBbQtxfDP32BzpTyM2QTm1y9rjNs3Rysgu4Ku5rK2nKbP1GVGo5kxZFZ7x7iaHzLwGijEg9QXyXJUWZA31S.dockers.com%2F; _landing_page=%2F; _y=9b34099d-5e17-4bca-ba29-a128225417f6; _s=b71be3ae-887a-418f-a1de-61b888db4b44; _shopify_y=9b34099d-5e17-4bca-ba29-a128225417f6; _shopify_s=b71be3ae-887a-45PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ24FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQR498Z; _shopify_sa_p=; amp_f24a38=o0vWrK_7zbauH3Y3mFodcf...1gplujph4.1gplumci6.0.0.0; _ga_RZYPECQ40Y=GS1.1.1676847736.1.1.1676847822.0.0.0; _ga=GA1.2.96749726.1676847737; redirect_geolocation={%22continentCode%22:%22NA%22%2C%22continentName%22:%22North%20America%22%2C%22countryCode%22:%22US%22%2C%22countryName%22:%22United%20States%22}; BVBRANDID=15bd0a17-77ce-4c9b-b07c-f2d175ada1e1; BVBRANDSID=29726ba3-d01f-4153-9f50-25569b46b0de; _ALGOLIA=anonymous-811be9d7-8fee-45PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ24FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQRdWlkPU5tVXlaakZtWldNdE9ESXdZeTAwTURObExUaGlNV1V0TVdFM09EWTJZemN4WldObA; cart=2cb5837248fd0b27345a6108ceba72a5; cart_ts =1676847830; cart_sig=57b69311d05031f88d453a304ba6b0da; cart_ver=gcp-gb-central1%3A9; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Feb+19+2023+18%3A03%3A52+GMT-0500+(hora+est%C3%A1ndar+de+Per%C3%BA)&version=202211.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0004%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false; _sctr=1|1676782800000; _gid=GA1.2.446374268.1676847741; user_id=anonymous-811be9d7-8fee-472f-ae8e-3762086a0f27; crl8.fpcuid=35955e4e-6cae-405c-8d89-5fad57d30de2; _fbp=fb.1.1676847747806.389613000; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2NzY4NDc3NTAsInZhbHVlIjoiaHR0cHM6Ly91cy5kb2NrZXJzLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly91cy5kb2NrZXJzLmNvbS9jb2xsZWN0aW9ucy9tZW5zLWJpZy10YWxsLWNsb3RoaW5nIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjc2ODQ3ODMwLCJ2YWx1ZSI6Imh0dHBzOi8vdXMuZG9ja2Vycy5jb20vIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vdXMuZG9ja2Vycy5jb20vY29sbGVjdGlvbnMvbWVucy1iaWctdGFsbC1jbG90aGluZyJ9fQ==; IR_gbd=dockers.com; IR_5411=1676847829974%7C0%7C1676847829974%7C%7C; IR_PI=80b6d27c-b0a9-11ed-9db3-3d4bd797de61%7C1676934155512; irclickid=~1X38541693812VY3238c5WXWYNQRWSKPLOECDsunkjia~71ZVRNE; _gat_gtag_UA_203062948_2=1; _uetsid=7590cbf0b0a911edbaef5d1a9cd647ac; _uetvid=7590abc0b0a911ed859ba70f62bcb39e; cart_currency=USD; OptanonAlertBoxClosed=2023-02-19T23:03:52.833Z',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
              
            }
            data = {
              'Shirts & Outerwear': 'M',
              'id': '41433636110497',
              'properties[_max_inventory]': '22',
              'properties[_pc9]': 'A17590004',
              
            }
            res = requests.post('https://us.dockers.com/cart/add.js', data=data)
            print(res.text)
            if (int(res.text.find('Cart Error')) > 0):
              data = {
                'Shirts & Outerwear': 'XL',
                'id': '41433636569249',
                'properties[_max_inventory]': '23',
                'properties[_pc9]': 'A17590004',
              }
              res = requests.post('https://us.dockers.com/cart/add.js', data=data)
              if (int(res.text.find('Cart Error')) > 0):
                return "Stock Problem!"
              
              data = {
                  'quantity': '1',
                  'checkout': 'Go to Checkout',
                }
                
              res1 = requests.post('https://us.dockers.com/cart',data=data)
              print(res1.text)
                