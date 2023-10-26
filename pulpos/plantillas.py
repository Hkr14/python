from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

_start = """<b><a href="tg://resolve?domain=RaceXtChkBot">RaceXtBot • [🤖]</a>\n\n¡Hola! Soy RaceXtChkBot Estoy A Tus Ordenes ¿Quieres Conocer Mis funciones? Primero Debes Registrarte Con /register\n\nPodras Utilizar Mis Gstes Y herramientas Gratis Solo En El Grupo Oficial Muchas Gracias.

－－－－－－－－－－－－－－
[ BOT STAFF ]
⊗Creador: <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
⊗Admin: <b><a href="tg://resolve?domain=ImCharmeleon">SarceDev[Owner]</a></b>
⊗Creador: <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
⊗Admin:
</b>
"""


_cmd = """<b><b><a href="tg://resolve?domain=RaceXtChkBot">RaceXtChkBot</a></b>

Para conocer mis comandos y funciones
presiona los botones y navega en las herramientas y Gates 
━━━━━━━━━
𝙏𝙤𝙩𝙖𝙡 𝙂𝙖𝙩𝙚𝙨                  <code>[12] ✅</code></b>

𝙏𝙤𝙩𝙖𝙡 𝙏𝙤𝙤𝙡𝙨                   <code>[8] ✅</code></b>

━━━━━━━━━
<b><a href="tg://resolve?domain=Sarcehkr">SarveDev[Owner]</a>
</b>
"""

_comancmd = """[𝚃𝙴𝙰𝙼 𝚁𝙰𝙲𝙴𝚇𝚃𝙲𝙷𝙺]\n<b>Gracias por usar nuestro bot, esperemos que sea de su agrado.



Presiona Los Botones Para Navegar y Conocer Mis Gates y Herramientas


</b>"""


_botoncmds = InlineKeyboardMarkup(

    [

        [
            InlineKeyboardButton("GATES ",callback_data="gates"),
            InlineKeyboardButton("TOOLS ",callback_data="tools")
        ],
        [
            InlineKeyboardButton("EXIT ❌",callback_data="exit")
        ]
    
    ]

)

_cmdbotons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton( 
                            "Gates",
                            callback_data="Gates"
                        ),                     
                        InlineKeyboardButton(
                            "Tools",
                            callback_data="Tools"
                        ),
                    ],
                    [
                        InlineKeyboardButton( 
                            "Owner",
                            url="https://t.me/Sarcehkr"),
                    ],
                ]
            )

_ifgates = """
━━━━[𝙍𝙖𝙘𝙚𝙓𝙩𝘾𝙝𝙠𝘽𝙤𝙩]━━━━

※𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘼𝙪𝙩𝙝
※𝘼𝙘𝙩𝙞𝙫𝙤𝙨             [2]
※𝘼𝙥𝙖𝙜𝙖𝙙𝙤𝙨        [2]

※𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘾𝙝𝙖𝙧𝙜𝙚𝙙
※𝘼𝙘𝙩𝙞𝙫𝙤𝙨             [4]
※𝘼𝙥𝙖𝙜𝙖𝙙𝙤𝙨        [3]

※𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝙈𝙖𝙨𝙨
※𝘼𝙘𝙩𝙞𝙫𝙤𝙨             [0]
※𝘼𝙥𝙖𝙜𝙖𝙙𝙤𝙨        [1]
    
<b>[Aviso]:</b> Se Irán Agregando Nuevos Gates...."""

_botongates = InlineKeyboardMarkup(



    [

        [
            InlineKeyboardButton("AUTH",callback_data="Auth"),
            InlineKeyboardButton("CHARGED",callback_data="Charged"),
            InlineKeyboardButton("MASS",callback_data="Mass")
        ]
    
    ]

)

_gauth = """
╔━━「𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘼𝙪𝙩𝙝」━━╗

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Denver [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /rp cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅
- - - - - - - - - - - - - -
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Medellin [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /md cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯ Stripe Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅
- - - - - - - - - - - - - -
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Auth [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /auth cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅
- - - - - - - - - - - - - -
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Italia [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /bra cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Braintree Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Actualizacion⚠️
- - - - - - - - - - - - - -
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Brasil [Free]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /bs cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Actualizacion⚠️
- - - - - - - - - - - - -"""

_botongatesas = InlineKeyboardMarkup(



    [

        [
            InlineKeyboardButton("Atras",callback_data="home"),
            InlineKeyboardButton("CHARGED",callback_data="Charged"),
            InlineKeyboardButton("MASS",callback_data="Mass")
        ]
    
    ]

)
_gcharged = """
━━「𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝘾𝙝𝙖𝙧𝙜𝙚𝙙」━━

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Rusia [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /rt cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Charged
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Bogota [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /bg cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Charged
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Roma [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /bo cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Braintree
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  ACTIVO✅

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Francia [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /ac cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Braintree
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  OFF❌

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Manchester [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /stp cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Charged
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Arabia [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /sh cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Shopify
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  OFF❌


𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Paypal [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /pp cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Paypal
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Actualizacion⚠️"""



_botongatesch = InlineKeyboardMarkup(

    [

        [
            InlineKeyboardButton("Atras",callback_data="home"),
            InlineKeyboardButton("AUTH",callback_data="Auth"),
            InlineKeyboardButton("MASS",callback_data="Mass")
        ]
    
    ]

)

_gmass = """
╔━━「𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 MASS」━━╗


𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  MASS STRIPE [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /mass cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  OFF❌
- - - - - - - - - - - - -"""

_botongatesmas = InlineKeyboardMarkup(



    [

        [
            InlineKeyboardButton("Atras",callback_data="home"),
            InlineKeyboardButton("AUTH",callback_data="Auth"),
            InlineKeyboardButton("CHARGED",callback_data="Charged")
        ]
    
    ]

)

_Call_Gateways = """<b>🟢Gates | Gateway 🟢</b>


━━━━━━━━━
⎚ Xilisio | Stripe Auth <code>[FREE]</code>
⎚ Usar <code>/xi card</code> [ 🟢 ]
━━━━━━━━━
⎚ Mass | Stripe Auth <code>[PREMIUM]</code>
⎚ Usar <code>/mass cards</code> [ 🔴 ]
━━━━━━━━━
⎚ Alga | Stripe Auth <code>[PREMIUM]</code>
⎚ Usar <code>/cr card</code> [ 🔴 ]
━━━━━━━━━
⎚ Yupi | Stripe Auth <code>[PREMIUM]</code>
⎚ Usar <code>/yu card</code> [ 🟢 ]
━━━━━━━━━

━━━━━━━━━
</b>"""

_Call_Tools = """<b><a 🟢Herramientas | Tools 🟢</b>

⎚ Bin - <code>FREE</code>
⎚ Usar <code>/bin 456789</code>
━━━━━━━━━
⎚ Gen Ccs - <code>FREE</code>
⎚ Usar <code>/gen 456789|rnd|rdn|rdn</code> 
━━━━━━━━━
⎚ Gen Mass Ccs <code>FREE</code>
⎚ Usar <code>/genmass 456789|rnd|rnd|rnd</code>
━━━━━━━━━
⎚ Tu informacion - <code>FREE</code>
⎚ Usar <code>/info </code>
━━━━━━━━━
⎚ Info Del bot user - <code>FREE</code>
⎚ Usar <code>/me</code>
━━━━━━━━━
⎚ Rand - <code>FREE</code>
⎚ Usar <code>/rand </code> 
━━━━━━━━━
⎚ Rand Pais - <code>FREE</code>
⎚ Usar <code>/rdn ar</code>
━━━━━━━━━
⎚ Zip code Postal - <code>FREE</code>
⎚ Usar <code>/zip 10020</code>
━━━━━━━━━
</b>"""

_Call_Gateways_buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Atras ",
                    callback_data="home"
                ),
                InlineKeyboardButton(
                    "Cerrar",
                    callback_data="exit"
                ),
        ]
        ]
    )
