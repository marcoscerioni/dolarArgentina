from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ParseMode
import logging
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
    buenbit, qubit, satoshi, ripio, decrypto = compraComision()
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso valordai', user.full_name, user.username)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        '*Valor DAI en cada exchange:*\n'
        '|            Compra  |    Venta    |'
        '|--------------------|-------------|'

        '*BuenBit*   ' + str('%.2f' % buenbit) + '\n '+\
        '*Qubit*     ' + str('%.2f' % qubit) + '\n '+\
        '*Satoshi*   ' + str('%.2f' % satoshi) + '\n '+\
        '*Ripio*    ' + str('%.2f' % ripio) + '\n '+\
        '*Decrypto*  ' + str('%.2f' % decrypto),
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


def mejorDaiDolar(update, context):
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso mejorDaiDolar', user.full_name, user.username)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=daiADolar())


def dolar(update, context):
    dolarT()
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso dolar', user.full_name, user.username)
    if os.path.exists('images/fig1.png'):
        context.bot.send_photo(chat_id=update.effective_chat.id, 
                               photo=open('images/fig1.png', 'rb'))


def dolarcrypto(update, context):
    user = update.message.from_user
    satoshi = satoshiCDP / satoshi_ven_dol
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
updater.dispatcher.add_handler(CommandHandler('mejordaidolar', mejorDaiDolar))
updater.dispatcher.add_handler(CommandHandler('dolar', dolar))
updater.dispatcher.add_handler(CommandHandler('dolarcrypto', dolarcrypto))


updater.start_polling()
updater.idle()
