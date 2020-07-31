import numpy as np
from apis import *
import plotly.graph_objects as go
import os


exchanges = ['Buenbit', 'Satoshi', 'Ripio', 'Qubit']

nombres = dict.fromkeys([0, 1, 2, 3], exchanges[0])
nombres.update(dict.fromkeys([4, 5, 6, 7], exchanges[1]))
nombres.update(dict.fromkeys([8, 9, 10, 11], exchanges[2]))
nombres.update(dict.fromkeys([12, 13, 14, 15], exchanges[3]))


def cDPCom():
    # Compra de DAI en cada exchange.
    buenbit = bbCDP              # No tiene comisión BB.
    qubit = qubitCDP             # Para comprar no tiene comision.
    satoshi = satoshiCDP * 1.01  # Comision del 1% la compra.
    ripio = ripioCDP * 1.01      # Comision del 1% la compra.
    decrypto = decrCDP * 1.0035  # Comision del 0.35% la compra.
    return buenbit, qubit, satoshi, ripio, decrypto

def vDPCom():
    # Venta de DAI en cada exchange en PESOS.
    buenbit = bbVDP              # No tiene comisión BB.
    qubit = qubitVDP             # Para venta no tiene comision.
    satoshi = satoshiVDP * 1.01  # Comision del 1% la compra. (solo Transferencia)
    ripio = ripioVDP * 1.01      # Comision del 1% la compra.
    decrypto = decrVDP * 1.0035  # Comision del 0.35% la compra.
    return buenbit, qubit, satoshi, ripio, decrypto



def daiDolar():
    # Vender DAI en todos los exchanges. Mejor opción.
    buenbit, qubit, satoshi, ripio, decrypto = cDPCom()
    baB = buenbit / bbVDD
    baS = (buenbit / satoshiVDD) * 1.01
    baD = (buenbit / decrVDD) * 1.0035 * 1.012  # Sacar USD 1.2%

    qaB = (qubit - 0.7) / bbVDD
    qaS = ((qubit - 0.7) / satoshiVDD) * 1.01
    qaD = ((qubit - 0.7) / decrVDD) * 1.0035 * 1.012  # Sacar USD 1.2%

    saB = (satoshi - 0.5) / bbVDD
    saS = (satoshi / satoshiVDD) * 1.01
    saD = ((satoshi - 0.5) / decrVDD) * 1.0035 * 1.012  # Sacar USD 1.2%

    raB = (ripio - comRipio) / bbVDD
    raS = ((ripio - comRipio) / satoshiVDD) * 1.01
    raD = ((ripio - comRipio) / decrVDD) * 1.0035 * 1.012  # Sacar USD 1.2%

    daB = decrypto / bbVDD
    daD = (decrypto / decrVDD) * 1.0035 * 1.012  # Sacar USD 1.2%
    daS = (decrypto / satoshiVDD) * 1.01

    return baB, baS, baD, qaB, qaS, qaD, saB, saS, saD, raB, raS, raD, daB, daD, daS


def dolarT():
    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'
    fig = go.Figure(data=[go.Table(
    header=dict(
    values=['<b></b>','<b>Compra</b>','<b>Venta</b>','<b>Variación</b>'],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['right','center'],
    font=dict(color='white', size=15)
  ),
    cells=dict(
    values=[
      ['<b>Oficial</b>', '<b>Con 30%</b>', '<b>Blue</b>', '<b>C.C.L.</b>', '<b>Bolsa</b>'],
      [dolarCOf, '%.2f' % (dolarCOf * 1.3), dolarCBl, dolarCCCL, dolarCBol],
      [dolarVOf, '%.2f' % (dolarVOf * 1.3), dolarVBl, dolarVCCL, dolarVBol],
      [dolarVarOf, '%.2f' % (dolarVarOf * 1.3), dolarVarBl, dolarVarCCL, dolarVarBol]],
    line_color='darkslategray',
    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
    align = ['center', 'center'],
    font = dict(color = 'darkslategray', size = 15)
        ))
    ])
    fig.update_layout(title={
        'text':'Precio Dólar hoy',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
        })
    if not os.path.exists("images"):
        os.mkdir("images")
    fig.write_image("images/fig1.png")


def otrasCrypto():
    # Comprar BTC y venderlo a USD en Decrypto y retirarlo. 
    dBTC = ((decrCBP * 1.0035) / decrVBD) * 1.0035 * 1.012

    # Comprar USDT y venderlo a USD en Decrypto y retirarlo. 
    dUSDT = ((decrCUP * 1.0035) / decrVUD) * 1.0035 * 1.012

    # Comprar BTC y venderlo a USD en Decrypto y retirarlo. 
    sBTC = ((satoshiCBP * 1.01) / satoshiVBD) * 1.01

    return dBTC, dUSDT, sBTC

print(otrasCrypto())






