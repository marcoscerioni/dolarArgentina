import numpy as np
from apis import *
# import time

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
    satoshi = satoshiVDP * 0.99  # Comision del 1% la compra. (solo Transferencia)
    ripio = ripioVDP * 0.99      # Comision del 1% la compra.
    decrypto = decrVDP * 0.9965  # Comision del 0.35% la compra.
    return buenbit, qubit, satoshi, ripio, decrypto



def daiDolar():
    # Vender DAI en todos los exchanges. Mejor opción.
    buenbit, qubit, satoshi, ripio, decrypto = cDPCom()
    baS = buenbit * satoshiVDD * 0.99
    baD = buenbit * decrVDD * 0.9965 * 0.988  # Sacar USD 1.2%

    qaS = (qubit - 0.7) * satoshiVDD * 0.99
    qaD = (qubit - 0.7) * decrVDD * 0.9965 * 0.988  # Sacar USD 1.2%

    saS = satoshi * satoshiVDD * 0.99
    saD = (satoshi - 0.5) * decrVDD * 0.9965 * 0.988  # Sacar USD 1.2%

    raS = (ripio - comRipio) * satoshiVDD * 0.99
    raD = (ripio - comRipio) * decrVDD * 0.9965 * 0.988  # Sacar USD 1.2%

    daD = decrypto * decrVDD * 0.9965 * 0.988  # Sacar USD 1.2%
    daS = decrypto * satoshiVDD * 0.99

    return baS, baD, qaS, qaD, saS, saD, raS, raD, daD, daS


inversion = 1000
comision = 0.99  # (100 - 1) / 100. Comision 1%


def compraDAI(inv):
    pesos = inv
    daiB = pesos / bbCDP
    daiS = inv * 0.9888 / satoshiCDP * comision  # comision de 1.12%
    daiR = inv / ripioCDP * comision
    daiQ = pesos / qubitCDP
    return daiB, daiS, daiR, daiQ


def ventaDAIPesos():
    daiB, daiS, daiR, daiQ = compraDAI(inversion)
    BenB = daiB * bbVDP
    BenS = daiB * satoshiVDP * comision
    BenR = daiB * ripioVDP * comision
    BenQ = daiB * qubitVDP

    SenB = (daiS - 0.1) * bbVDP
    SenS = daiS * satoshiVDP * comision
    SenR = (daiS - 0.1) * ripioVDP * comision
    SenQ = (daiS - 0.1) * qubitVDP

    RenB = (daiR - comRipio) * bbVDP
    RenS = (daiR - comRipio) * satoshiVDP * comision
    RenR = daiR * ripioVDP * comision
    RenQ = (daiR - comRipio) * qubitVDP

    QenB = daiQ * bbVDP
    QenS = daiQ * satoshiVDP * comision
    QenR = daiQ * ripioVDP * comision
    QenQ = daiQ * qubitVDP

    return BenB, BenS, BenR, BenQ, SenB,
    SenS, SenR, SenQ, RenB, RenS, RenR, RenQ,
    QenB, QenS, QenR, QenQ


valoresPesos = ventaDAIPesos()
indicePesos = np.argmax(valoresPesos)
maximo = max(valoresPesos)


def daiAPesos():
    comprar = nombres[indicePesos]
    vender = exchanges[indicePesos % 4]
    mensaje = ''
    pesosCambiados = max(valoresPesos)
    if(pesosCambiados > inversion):
        mensaje += 'Compra DAI en ' + comprar +\
                   ' y vende DAI a pesos en ' + vender
        diferencia = (pesosCambiados / inversion - 1) * 100
        mensaje += ' Vas a ganar' + str(round(diferencia, 2)) +\
                   '% en pesos'
    return mensaje


def venDaiaDolar():
    daiB, daiS, daiR, daiQ = compraDAI(inversion)
    BenB = daiB * buenbit_com_dol
    BenS = daiB * satoshiCDD * comision

    SenB = (daiS - 0.1) * buenbit_com_dol
    SenS = daiS * satoshiCDD * comision

    RenB = (daiR - comRipio) * buenbit_com_dol
    RenS = (daiR - comRipio) * satoshiCDD * comision

    QenB = daiQ * buenbit_com_dol
    QenS = daiQ * satoshiCDD * comision

    return (BenB, BenS, 0, 0, SenB, SenS, 0, 0, RenB, RenS, 0, 0, QenB, QenS)


def daiADolar():
    valores = venDaiaDolar()
    comprar = nombres[np.argmax(valores)]
    vender = exchanges[np.argmax(valores) % 4]
    mensaje = 'La mejor opción de comprar DAIs y venderlo a dólares es:\n\n' +\
        'Comprar DAI en ' + comprar + ' y venderlo en ' + vender
    return mensaje


def opcionDai(inv):
    daiB, daiS, daiR, daiQ = compraDAI(inv)
    mensaje = 'Con una inversión de $ ' + str(inv) + ' obtenes en: \n\n'
    mensaje += 'Buenbit ---- ' + str('%.4f' % daiB) + ' DAI\n'
    mensaje += 'Satoshi ---- ' + str('%.4f' % daiS) + ' DAI\n'
    mensaje += 'Ripio ------- ' + str('%.4f' % daiR) + ' DAI\n'
    mensaje += 'Qubit ------ ' + str('%.4f' % daiQ) + ' DAI\n'
    return mensaje


def valorDelDolar():
    buenbit = bbCDP / buenbit_ven_dol
    satoshi = satoshiCDP / satoshiVDD
    qubit = qubitCompDolardirecto
    mensaje = 'Precio del Dólar en:\n\n'
    mensaje += "Buenbit  $" + str('%.4f' % buenbit) +\
               "   NO FUNCIONA ACTUALMENTE\n"
    mensaje += "Satoshi  $" + str('%.4f' % satoshi) + '\n'
    mensaje += "Qubit     $" + str('%.4f' % qubit) +\
               "   NO FUNCIONA ACTUALMENTE \n"
    mensaje += '\n                 Dolar \n'
    mensaje += '          Compra    |   Venta'
    mensaje += 'Oficial: ' + str(dolarCOf) + str(dolarVOf)
    mensaje += 'Blue' + str(dolarCBl) + str(dolarVBl)
    return mensaje


import plotly.graph_objects as go
import os



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

dolarT()
