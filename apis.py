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
comisionDai = promedio * 0.1790313 / 8730


# Satochi DAI pesos.
cont = obtenerJson(satoshiPesos)
satoshi_com_pes = float(cont['data']['ticker']['DAI']['ask'])
satoshi_ven_pes = float(cont['data']['ticker']['DAI']['bid'])


# Satoshi DAI Dolares.
cont = obtenerJson(satoshiDolar)
satoshi_com_dol = float(cont['data']['ticker']['DAI']['ask'])
satoshi_ven_dol = float(cont['data']['ticker']['DAI']['bid'])



# Ripio DAI pesos (tiene solo pesos)
cont = obtenerJson(ripio)
ripioLista = cont[2]
compra_ripio = float(ripioLista['buy_rate'])
venta_ripio = float(ripioLista['sell_rate'])


# BuenBit DAI pesos
cont = obtenerJson(buenbit)
buenbit_com_pes = float(cont['object']['daiars']['selling_price'])
buenbit_ven_pes = float(cont['object']['daiars']['purchase_price'])


# BuenBit DAI dolares
buenbit_com_dol = float(cont['object']['daiusd']['selling_price'])
buenbit_ven_dol = float(cont['object']['daiusd']['purchase_price'])


# Qubit DAI
cont = obtenerJson(qubitC)
qubitCompDol = float(cont['DAI'][1])  # Compra DAI con dolares
qubitComPes = float(cont['DAI'][2])   # Compra DAI con pesos

# Qubit Dolar
cont = obtenerJson(qubitC)
try:
    qubitCompDolardirecto = float(cont['USD'][2])  # Compra dolares
except KeyError:
    qubitCompDolardirecto = 0



cont = obtenerJson(qubitV)
# qubitDaiDol = cont['DAI'][1]  # Venta DAI con dolares, pero no lo hacen.
qubitVenPes = float(cont['DAI'][2])  # Venta DAI en pesos

# Qubit dolares
cont = obtenerJson(qubitD)
qubitCompraDol = float(cont['buy_price'])
qubitVentaDol = float(cont['sell_price'])


# Decrypto DAI con Pesos
cont = obtenerJson(decrypto)
decrCDP = float(cont['data'][3]['dca'])  # Compra DAI Pesos
decrVDP = float(cont['data'][3]['dcb'])  # Venta DAI Pesos

# Decrypto DAI con Dolares
decrCDD = float(cont['data'][2]['dca'])  # Compra DAI Pesos
decrVDD = float(cont['data'][2]['dcb'])  # Venta DAI Pesos


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

print(decrCDP,  decrVDP, decrCDD, decrVDD)
