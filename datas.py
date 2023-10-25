import re



INCORRECT_CARD = '**INGRESE BIEN SU CCARD**'
EMPTY_CARD = '**Para usarlos copie o escribe el comando, pegue la cc é envié el comando `cc - aa - mm - cvv` \n\n👨‍💻ᴛᴇᴀᴍ             • [ 𝗽𝗼𝗰𝘂𝗽𝘆 𓅂 ] • \n𝗽𝗼𝗶𝗻𝘁𝘀 𝗰𝗼𝗺𝘂𝗻𝗶𝘁𝘆 𝗽𝘆𝘁𝗵𝗼𝗻 𓅂.**'
INVALID_CARD = '**LA CARD NO ES VALIDA.**'
SHORT_CARD = '**CC ES INCORRECTA.**'
INCORRECT_MONTH = '**MES DEL CARD ES INCORRECTO**'
INCORRECT_YEAR = '**AÑO DEL CARD ES INCORRECTO**'
INCORRECT_CVV = '**CVV DEL CARD ES INCORRECTO**'



def get_data(data):
    input = re.findall(r"[0-9]+", data)
    try:
        if len(input) == 0:
            raise UnicodeError
        cc = input[0]
        mes = input[1]
        ano = input[2]
        ano1 = input[2]
        cvv = input[3]
        if len(input) == 3:
            cc = input[0]
            mes = input[1][:2]
            ano = input[1][2:]
            ano1 = input[1][2:]
            cvv = input[2]
        if len(mes) > 2:
            ano = cvv
            cvv = mes
            mes = ano1
    except UnicodeError:
        return EMPTY_CARD
    except Exception as e:
        return EMPTY_CARD
    else:
        if int(cc[0]) in [1, 2, 7, 8, 9, 0]:
            return INVALID_CARD
        elif int(len(cc))not in [15, 16]:
            return SHORT_CARD
        elif int(len(mes)) not in [1, 2, 4] or len(mes) == 2 and mes > '12' or len(mes) == 2 and mes < '01' or len(mes) != 2 or (len(mes) == 1 and int(mes) > 12 or int(mes) < 1):
            return INCORRECT_MONTH
        elif int(len(ano)) not in [2, 4] or len(ano) < 2 or len(ano) == 2 and ano < '21' or len(ano) == 4 and ano < '2021' or len(ano) == 2 and ano > '29' or len(ano) == 4 and ano > '2029' or len(ano) > 4 or len(ano) == 3:
            return INCORRECT_YEAR
        elif int(cc[0]) == 3 and len(cvv) != 4 or len(cvv) < 3 or len(cvv) > 4:
            return INCORRECT_CVV
        else:
            if len(mes) == 1:
                mes = '0' + str(mes)
            if len(ano) == 2:
                ano = '20' + str(ano)
            return (cc, mes, ano, cvv)



def find_between( data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None


def get_response(text):
    if 'Thank you' in text or 'Your order is confirmed' in text:
        r_text, r_logo, r_respo = "Charged $4", "✅", 'Charged'
        return r_text, r_logo, r_respo,
    text1 = find_between(text, '<p class="notice__text">','</p></div></div>')
    text = text1 if text1 else text
    if 'ZIP code does not match billing address' in text or "2059" in text or "2060" in text :
        r_text, r_logo, r_respo = "ZIP INCORRECT", "✅", 'Charged'
    elif "2001"  in text:
        r_text, r_logo, r_respo = "LOW FUNDS", "✅", 'Charged'
    elif "Security code was not matched by the processor" in text:
        r_text, r_logo, r_respo = "CCN LIVE", "✅", 'CCN Match'
    elif '"seller_message": "Payment complete."' in text or '"cvc_check": "pass"' in text or 'thank_you' in text or '"type":"one-time"' in text or '"state": "succeeded"' in text or "Your payment has already been processed" in text or '"status": "succeeded"' in text or 'Thank' in text:
        r_text, r_logo, r_respo = "Charged $4", "✅", 'Charged'
    else:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'Rejected'
    r_text1 = text1.replace('-','') if text1 else r_text
    return r_text1,r_logo,r_respo