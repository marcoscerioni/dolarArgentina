from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ParseMode
import logging
import numpy as np
from valores import *
from auth import *
from apis import *

updater = Updater(token=token, use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso start', user.full_name, user.username)
    name = user.first_name
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Bienvenido* " + name + "*, "
             "al Bot del CryptoDolar"
             " en Argentina \n\n"
             "Los comandos disponibles son: \n"
             "*/start* - Instrucciones del Bot. \n"
             "*/valordai* - Valor del DAI en cada exchange.\n"
             # "*/calc* NUMERO - Calcula la cantidad que DAI que "
             # 'obtendrias en cada exchange. \n'
             "*/daidolar* - Todas las opciones de comprar DAI,"
             " pasarlo a cualquier exchange y comprar dólares.\n"
             "*/dolar* - Imagen con los valores del Dólar actualizado.\n"
             "*/otras* - Valor de comprar BTC o USDT y venderlo a dólares.\n\n"
             "Otra opción para ver los comando es *presionar la tecla '/'.*",
         parse_mode=ParseMode.MARKDOWN)


def valordai(update, context):
    buenbitC, qubitC, satoshiC, ripioC, decryptoC = cDPCom()
    buenbitV, qubitV, satoshiV, ripioV, decryptoV = vDPCom()

    user = update.message.from_user
    logger.info('El usuario %s (%s) puso valordai', user.full_name, user.username)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        '```'
        '\n    Valor DAI en cada exchange\n'
        '|          Compra   |    Venta   |\n'
        '|-------------------|------------|\n'
        '|BuenBit  $ ' + str('%.2f' % buenbitC) + '  |  $ ' +\
            str('%.2f' % buenbitV) + '  |\n'
        '|Qubit    $ ' + str('%.2f' % qubitC) + '  |  $ ' +\
            str('%.2f' % qubitV) + '  |\n'
        '|Satoshi  $ ' + str('%.2f' % satoshiC) + '  |  $ ' +\
            str('%.2f' % satoshiV) + '  |\n'
        '|Ripio    $ ' + str('%.2f' % ripioC) + '  |  $ ' +\
            str('%.2f' % ripioV) + '  |\n'
        '|Decrypto $ ' + str('%.2f' % decryptoC) + '  |  $ ' +\
            str('%.2f' % decryptoV) + '  |\n'
        '```',
        parse_mode=ParseMode.MARKDOWN
)


# def calc(update, context):
#     user = update.message.from_user
#     logger.info('El usuario %s (%s) puso calc', user.full_name, user.username)
#     if (len(context.args) == 1):
#         try:
#             input = int(context.args[0])
#             context.bot.send_message(chat_id=update.effective_chat.id,
#                                      text=opcionDai(input))
#         except ValueError:
#             context.bot.send_message(chat_id=update.message.chat_id,
#                                      text='Por favor, ingresa solo un numero. '
#                                      'Por ejemplo /calc 500')
#     else:
#         context.bot.send_message(chat_id=update.message.chat_id,
#                                  text='Por favor, ingresa solo un valor. '
#                                  'Por ejemplo /calc 10000')


def daidolar(update, context):
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso daidolar', user.full_name, user.username)
    baS, baD, qaS, qaD, saS, saD, raS, raD, daD, daS = daiDolar()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='*Comprar DAI y venderlo a dólares:*\n\n'
             '``` \n' +\
             'De Buenbit a Satoshi:     $ ' + str('%.4f' % baS) + '\n'
             'De Buenbit a Decrypto:    $ ' + str('%.4f' % baD) + '\n'
             'De Qubit a Satoshi:       $ ' + str('%.4f' % qaS) + '\n'
             'De Qubit a Decrypto:      $ ' + str('%.4f' % qaD) + '\n'
             'De Satoshi a Satoshi:     $ ' + str('%.4f' % saS) + '\n'
             'De Satoshi a Decrypto:    $ ' + str('%.4f' % saD) + '\n'
             'De Ripio a Satoshi:       $ ' + str('%.4f' % raS) + '\n'
             'De Ripio a Decrypto:      $ ' + str('%.4f' % raD) + '\n'
             'De Decrypto a Satoshi:    $ ' + str('%.4f' % daD) + '\n'
             'De Decrypto a Decrypto:   $ ' + str('%.4f' % daS) + '```\n',
        parse_mode=ParseMode.MARKDOWN
        )


def dolar(update, context):
    dolarT()
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso dolar', user.full_name, user.username)
    if os.path.exists('images/fig1.png'):
        context.bot.send_photo(chat_id=update.effective_chat.id, 
                               photo=open('images/fig1.png', 'rb'))


def otras(update, context):
    user = update.message.from_user
    dBTC, dUSDT, sBTC = otrasCrypto()
    logger.info('El usuario %s (%s) puso otras', user.full_name, user.username)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
         '*Valor de comprar BTC o USDT y venderlo a dólares:*\n'
         '\n``` \n' +\
         'Decrypto BTC a dólares    $' + str('%.4f' % dBTC) + '\n'
         'Decrypto USDT a dólares   $' + str('%.4f' % dUSDT) + '\n\n'
         'Satoshi BTC a dólares     $' + str('%.4f' % sBTC) + '```\n',
         parse_mode=ParseMode.MARKDOWN)




updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('valordai', valordai))
updater.dispatcher.add_handler(CommandHandler('daidolar', daidolar))
updater.dispatcher.add_handler(CommandHandler('dolar', dolar))
updater.dispatcher.add_handler(CommandHandler('otras', otras))


updater.start_polling()
updater.idle()
