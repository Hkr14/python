from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import gather
from datetime import datetime, timedelta
from io import BytesIO
from math import atan2, cos, radians, sin, sqrt
from os import execvp
from random import randint
from re import findall
from re import sub as re_sub
from sys import executable
import aiofiles
import speedtest
import os
import requests
import time
import string
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
@Client.on_message(filters.command(["disney"], ["/", "."]))
async def xi(_, message: Message):
  with open(file='plugins/usuarios/gold.txt',mode='r+',encoding='utf-8') as archivo:
    x = archivo.readlines()
    if str(message.from_user.id) + '\n' in x or message.chat.id in idchat:
      data = message.text.split(" ", 2)

  def getRandomString(length):
    pool = string.ascii_lowercase + string.digits
    return "".join(random.choice(pool) for i in range(length))

  def getRandomText(length):
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))
    
  def generate():
    nick = getRandomText(8)
    passw = getRandomString(12)
    email = nick + "@" + "gmail" + ".com"
    
    
    headers = {
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-US",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json",
        "Host": "global.edge.bamgrid.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "X-Bamsdk-Platform": "web",
        "X-Bamsdk-Version": "5.0.0",
        "X-Forwarded-For": getRandomString(12),
        "X-Forwarded-Proto": "https",
        "X-Forwarded-Server": "global.edge.bamgrid.com",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    payload = {
        "email": email,
        "password": passw,
        "confirmPassword": passw,
        "birthDay": random.randint(1, 28),
        "birthMonth": random.randint(1, 12),
        "birthYear": random.randint(1970, 2000),
        "firstName": getRandomText(6),
        "lastName": getRandomText(6),
        "gender": "MALE" if random.randint(0, 1) else "FEMALE",
        "legalAcceptedDate": "2020-05-01T00:00:00.000Z",
        "termsAcceptedDate": "2020-05-01T00:00:00.000Z",
        "emailOptIn": True,
        "subscription": {
            "offerId": "standardAnnual",
            "marketingOptIn": True,
            "affiliateMarketingOptIn": True,
            "paymentMethodId": "pm_adyen_cc",
            "paymentMethodType": "creditCard",
            "creditCard": {
                "cardholderName": getRandomText(6) + " " + getRandomText(6),
                "cardNumber": "4737011411712804",
                "expirationMonth": "12",
                "expirationYear": "2024",
                "securityCode": "755"
            }
        }
    }
    
    r = requests.post(
        'https://global.edge.bamgrid.com/register',
        headers=headers,
        json=payload)
        
    if r.status_code == 200:
        if r.json()['status'] == "SUCCESS":
            text = f"""
Auto Disney+ Created! ✅
🍏 Premium-»  Annual
🍏 Email-» <b>{email}</b>
🍏 Password-»<code>{passw}</code>"""  
             
             
            return (text)
        else:
            #Details available in r.json()["errors"]
            #print(r.json()["errors"])
            return (False, "Could not create the account, some errors occurred")
    else:
      return (False,
                "Could not load the page. Response code: " + str(r.status_code))
                
  return await message.reply(generate())          