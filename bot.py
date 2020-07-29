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
             "*/valordai* - Valor del DAI.\n"
             "*/calc* NUMERO - Calcula la cantidad que DAI que "
             'obtendrias en cada exchange. \n'
             "*/mejordaidolar* - Mejor opción para comprar DAI y"
             " luego venderlo a dólares. \n"
             "*/dolar* - Muestra imagen con los valores del Dólar actualizado"
             "*/dolarcrypto* - Muestra el valor en el que se"
             " comprarian dólares con criptomendas.\n"
             "Otra opción para ver los comando es presionar"
             " la tecla '/'. ",
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


def calc(update, context):
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso calc', user.full_name, user.username)
    if (len(context.args) == 1):
        try:
            input = int(context.args[0])
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=opcionDai(input))
        except ValueError:
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Por favor, ingresa solo un numero. '
                                     'Por ejemplo /calc 500')
    else:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text='Por favor, ingresa solo un valor. '
                                 'Por ejemplo /calc 10000')


def daidolar(update, context):
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso daidolar', user.full_name, user.username)
    baS, baD, qaS, qaD, saS, saD, raS, raD, daD, daS = daiDolar()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='*Comprar DAI y venderlo a dólares:*\n\n'
             '```De Buenbit a Satoshi:     USD ' + str('%.4f' % baS) + '\n'
             'De Buenbit a Decrypto:    USD ' + str('%.4f' % baD) + '\n'
             'De Qubit a Satoshi:       USD ' + str('%.4f' % qaS) + '\n'
             'De Qubit a Decrypto:      USD ' + str('%.4f' % qaD) + '\n'
             'De Satoshi a Satoshi:     USD ' + str('%.4f' % saS) + '\n'
             'De Satoshi a Decrypto:    USD ' + str('%.4f' % saD) + '\n'
             'De Ripio a Satoshi:       USD ' + str('%.4f' % raS) + '\n'
             'De Ripio a Decrypto:      USD ' + str('%.4f' % raD) + '\n'
             'De Decrypto a Satoshi:    USD ' + str('%.4f' % daD) + '\n'
             'De Decrypto a Decrypto:   USD ' + str('%.4f' % daS) + '```\n',
        parse_mode=ParseMode.MARKDOWN
        )


def dolar(update, context):
    dolarT()
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso dolar', user.full_name, user.username)
    if os.path.exists('images/fig1.png'):
        context.bot.send_photo(chat_id=update.effective_chat.id, 
                               photo=open('images/fig1.png', 'rb'))


def dolarcrypto(update, context):
    user = update.message.from_user
    satoshi = satoshiCDP / satoshiVDD
    logger.info('El usuario %s (%s) puso dolarcrypto', user.full_name, user.username)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
         '\n*Decrypto DAI*' + '      $ ' + '\n'
         '*Decrypto USDT*' + '     $ ' + '\n'
         '*SatoshiTango*' + '      $ ' + str('%.4f' % satoshi) + '\n'
         '*BuenBit*' + '              ' + ' NO PERMITIDO\n'
         "*Qubit Brokers*" + "       " + " NO PERMITIDO\n",
         parse_mode=ParseMode.MARKDOWN)




updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('valordai', valordai))
updater.dispatcher.add_handler(CommandHandler('calc', calc))
updater.dispatcher.add_handler(CommandHandler('daidolar', daidolar))
updater.dispatcher.add_handler(CommandHandler('dolar', dolar))
updater.dispatcher.add_handler(CommandHandler('dolarcrypto', dolarcrypto))


updater.start_polling()
updater.idle()
