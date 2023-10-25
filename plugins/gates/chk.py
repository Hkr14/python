import time
import requests
from pyrogram import Client
from pyrogram import filters
from datas import find_between, get_data, get_response
from random_address import real_random_address


from plugins.shopify import def_last, one_def, two_def
from rand_user import random_user_api





@Client.on_message(filters.command("chk",prefixes=['.','/','!','?'],case_sensitive=False) & filters.text)
async def start(_, message):
    
        message.text = message.reply_to_message.text if message.reply_to_message is not None else message.text
        data = get_data(message.text)
        assert isinstance(data, tuple), data.format(
            message.from_user.id, message.from_user.first_name)
        cc, mes, ano,cvv = data
        r =  requests.Session()
        a = one_def(r)
        
        auth_token, checkout_url = a
        await xx.edit("First Requests Completed")
        rand_user = random_user_api().get_random_user_info()
        addr = real_random_address()
        b = two_def(rand_user, addr, r, auth_token, checkout_url)
        assert b, " Error On Second requests"
        price, payment_gateway = b
        await xx.edit("Second Requests Completed")
        g = def_last(rand_user, r, cc, mes, ano, cvv, auth_token, checkout_url, price, payment_gateway)
        assert g, "Error On Last Requests"
        # await xx.edit("Last Requests Completed")
        r_text, r_logo, r_respo = get_response(g.text)
        mess = f"""
Card: `{cc}|{mes}|{ano}|{cvv}`
Response: {r_respo} {r_logo}
Message: {r_text}
Took: {int(time.time()) -  start_time}
"""
        await xx.edit(mess)
      
        await xx.edit(e)
       
        print(e)
        

