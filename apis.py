import requests
import json
from auth import *


def obtenerJson(url):
    r = requests.get(url)
    cont = json.loads(r.content)
    return cont


# Obtener comision Ripio
cont = obtenerJson(ripioComision)
promedio = 291 * ((cont['fastestFee'] + cont['halfHourFee'] + cont['hourFee']) / 3)
comRipio = promedio * 0.1790313 / 8730


# Satochi pesos.
cont = obtenerJson(satoshiPesos)
satoshiCDP = float(cont['data']['ticker']['DAI']['ask'])  # Compra DAI Pesos
satoshiVDP = float(cont['data']['ticker']['DAI']['bid'])  # Venta DAI Pesos

satoshiCBP = float(cont['data']['ticker']['BTC']['ask'])  # Compra BTC Pesos
satoshiVBP = float(cont['data']['ticker']['BTC']['bid'])  # Venta BTC Pesos

# Satoshi Dolares.
cont = obtenerJson(satoshiDolar)
satoshiCDD = float(cont['data']['ticker']['DAI']['ask'])  # Compra DAI Dolares
satoshiVDD = float(cont['data']['ticker']['DAI']['bid'])  # Venta DAI Dolares

satoshiVBD = float(cont['data']['ticker']['BTC']['bid'])  # Venta BTC Dolares
satoshiVBD = float(cont['data']['ticker']['BTC']['bid'])  # Venta BTC Dolares



# Ripio DAI pesos (tiene solo pesos)
cont = obtenerJson(ripio)
ripioLista = cont[2]
ripioCDP = float(ripioLista['buy_rate'])
ripioVDP = float(ripioLista['sell_rate'])


# BuenBit DAI pesos
cont = obtenerJson(buenbit)
bbCDP = float(cont['object']['daiars']['selling_price'])
bbVDP = float(cont['object']['daiars']['purchase_price'])


# BuenBit DAI dolares
buenbit_com_dol = float(cont['object']['daiusd']['selling_price'])
buenbit_ven_dol = float(cont['object']['daiusd']['purchase_price'])


# Qubit DAI
cont = obtenerJson(qubitC)
qubitCompDol = float(cont['DAI'][1])  # Compra DAI con dolares
qubitCDP = float(cont['DAI'][2])   # Compra DAI con pesos

# Qubit Dolar
cont = obtenerJson(qubitC)
try:
    qubitCompDolardirecto = float(cont['USD'][2])  # Compra dolares
except KeyError:
    qubitCompDolardirecto = 0



cont = obtenerJson(qubitV)
# qubitDaiDol = cont['DAI'][1]  # Venta DAI con dolares, pero no lo hacen mas.
qubitVDP = float(cont['DAI'][2])  # Venta DAI en pesos

# Qubit dolares
cont = obtenerJson(qubitD)
qubitCompraDol = float(cont['buy_price'])
qubitVentaDol = float(cont['sell_price'])


# Decrypto DAI con Pesos
cont = obtenerJson(decrypto)
decrCDP = float(cont['data'][3]['dca'])  # Compra DAI Pesos
decrVDP = float(cont['data'][3]['dcb'])  # Venta DAI Pesos

# Decrypto DAI con Dolares
decrCDD = float(cont['data'][2]['dca'])  # Compra DAI Dolares
decrVDD = float(cont['data'][2]['dcb'])  # Venta DAI Dolares

# Decrypto BTC con Pesos
decrCBP = float(cont['data'][1]['dca'])  # Compra BTC Pesos
decrVBP = float(cont['data'][1]['dcb'])  # Venta BTC Pesos

# Decrypto BTC con Dolares
decrCBD = float(cont['data'][0]['dca'])  # Compra BTC Dolares
decrVBD = float(cont['data'][0]['dcb'])  # Venta BTC Dolares

# Decrypto USDT con Pesos
decrCUP = float(cont['data'][7]['dca'])  # Compra USDT Pesos
decrVUP = float(cont['data'][7]['dcb'])  # Venta USDT Pesos

# Decrypto USDT con Dolares
decrCUD = float(cont['data'][4]['dca'])  # Compra USDT Dolares
decrVUD = float(cont['data'][4]['dcb'])  # Venta USDT Dolares


# Dolar Oficial
cont = obtenerJson(dolar)
dolarCOf = float((cont[0]['casa']['compra']).replace(',','.')) # Dolar oficial compra
dolarVOf = float((cont[0]['casa']['venta']).replace(',','.')) # Dolar oficial venta
dolarVarOf = float((cont[0]['casa']['variacion']).replace(',','.')) # Dolar oficial variacion

# Dolar Blue
dolarCBl = float((cont[1]['casa']['compra']).replace(',','.')) # Dolar blue compra
dolarVBl = float((cont[1]['casa']['venta']).replace(',','.')) # Dolar blue venta
dolarVarBl = float((cont[1]['casa']['variacion']).replace(',','.')) # Dolar blue variacion

# Dolar Contado con liqui
dolarCCCL = float((cont[3]['casa']['compra']).replace(',','.')) # Dolar blue compra
dolarVCCL = float((cont[3]['casa']['venta']).replace(',','.')) # Dolar blue venta
dolarVarCCL = float((cont[3]['casa']['variacion']).replace(',','.')) # Dolar blue variacion

# Dolar Bolsa
dolarCBol = float((cont[4]['casa']['compra']).replace(',','.')) # Dolar blue compra
dolarVBol = float((cont[4]['casa']['venta']).replace(',','.')) # Dolar blue venta
dolarVarBol = float((cont[4]['casa']['variacion']).replace(',','.')) # Dolar blue variacion
