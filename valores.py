import numpy as np
from apis import *
# import time

exchanges = ['Buenbit', 'Satoshi', 'Ripio', 'Qubit']

nombres = dict.fromkeys([0, 1, 2, 3], exchanges[0])
nombres.update(dict.fromkeys([4, 5, 6, 7], exchanges[1]))
nombres.update(dict.fromkeys([8, 9, 10, 11], exchanges[2]))
nombres.update(dict.fromkeys([12, 13, 14, 15], exchanges[3]))


def valoresCompra():
    espacio = "            "
    mensaje = "Los valores del DAI en cada exchange son los siguientes:\n\n "
    mensaje += "           Buenbit\n"
    mensaje += "----------------------------\n"
    mensaje += "  Compra           Venta\n"
    mensaje += " $" + str('%.2f' % buenbit_com_pes) + espacio + '$'
    mensaje += str('%.2f' % buenbit_ven_pes) + "\n"
    mensaje += " USD " + str('%.2f' % buenbit_com_dol) + "           " + 'USD '
    mensaje += str('%.2f' % buenbit_ven_dol) + "\n"
    mensaje += "----------------------------\n"
    mensaje += "\n\n"

    mensaje += "       SatoshiTango\n"
    mensaje += "----------------------------\n"
    mensaje += "  Compra           Venta\n"
    mensaje += " $" + str('%.2f' % satoshi_com_pes) + espacio + '$'
    mensaje += str('%.2f' % satoshi_ven_pes) + "\n"
    mensaje += " USD " + str('%.2f' % satoshi_com_dol) + "           " + 'USD '
    mensaje += str('%.2f' % satoshi_ven_dol) + "\n"
    mensaje += "----------------------------\n"
    mensaje += "\n\n"

    mensaje += "              Ripio\n"
    mensaje += "----------------------------\n"
    mensaje += "   Compra           Venta\n"
    mensaje += "  $" + str('%.2f' % compra_ripio) + espacio + '$'
    mensaje += str('%.2f' % venta_ripio) + "\n"
    mensaje += "  USD -" + "                " + 'USD -\n'
    mensaje += "----------------------------\n"
    mensaje += "\n\n"

    mensaje += "              Qubit\n"
    mensaje += "----------------------------\n"
    mensaje += "   Compra           Venta\n"
    mensaje += "  $" + str('%.2f' % qubitComPes) + espacio + '$'
    mensaje += str('%.2f' % qubitVenPes) + "\n"
    mensaje += "  USD " + str('%.2f' % qubitCompDol) + "          "
    mensaje += 'USD -\n'
    mensaje += "----------------------------\n"
    return mensaje


inversion = 1000
comision = 0.99  # (100 - 1) / 100. Comision 1%


def compraDAI(inv):
    pesos = inv
    daiB = pesos / buenbit_com_pes
    daiS = inv * 0.9888 / satoshi_com_pes * comision  # comision de 1.12%
    daiR = inv / compra_ripio * comision
    daiQ = pesos / qubitComPes
    return daiB, daiS, daiR, daiQ


def ventaDAIPesos():
    daiB, daiS, daiR, daiQ = compraDAI(inversion)
    BenB = daiB * buenbit_ven_pes
    BenS = daiB * satoshi_ven_pes * comision
    BenR = daiB * venta_ripio * comision
    BenQ = daiB * qubitVenPes

    SenB = (daiS - 0.1) * buenbit_ven_pes
    SenS = daiS * satoshi_ven_pes * comision
    SenR = (daiS - 0.1) * venta_ripio * comision
    SenQ = (daiS - 0.1) * qubitVenPes

    RenB = (daiR - comisionDai) * buenbit_ven_pes
    RenS = (daiR - comisionDai) * satoshi_ven_pes * comision
    RenR = daiR * venta_ripio * comision
    RenQ = (daiR - comisionDai) * qubitVenPes

    QenB = daiQ * buenbit_ven_pes
    QenS = daiQ * satoshi_ven_pes * comision
    QenR = daiQ * venta_ripio * comision
    QenQ = daiQ * qubitVenPes

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
    BenS = daiB * satoshi_com_dol * comision

    SenB = (daiS - 0.1) * buenbit_com_dol
    SenS = daiS * satoshi_com_dol * comision

    RenB = (daiR - comisionDai) * buenbit_com_dol
    RenS = (daiR - comisionDai) * satoshi_com_dol * comision

    QenB = daiQ * buenbit_com_dol
    QenS = daiQ * satoshi_com_dol * comision

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
    buenbit = buenbit_com_pes / buenbit_ven_dol
    satoshi = satoshi_com_pes / satoshi_ven_dol
    qubit = qubitCompDolardirecto
    mensaje = 'Precio del Dólar en:\n\n'
    mensaje += "Buenbit  $" + str('%.4f' % buenbit) + '\n' +\
               "  NO FUNCIONA ACTUALMENTE"
    mensaje += "Satoshi  $" + str('%.4f' % satoshi) + '\n'
    mensaje += "Qubit     $" + str('%.4f' % qubit)
    return mensaje
