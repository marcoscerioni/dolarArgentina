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
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Bienvenido* " + name + "*, "
                             "al Bot de la criptomenda DAI"
                             " en Argentina \n\n"
                             "Los comandos disponibles son: \n"
                             "*/start* - Instrucciones del Bot. \n"
                             "*/valordai* - Valor del DAI.\n"
                             "*/calc* NUMERO - Calcula la cantidad que DAI que "
                             'obtendrias en cada exchange. \n'
                             "*/mejordaidolar* - Mejor opción para comprar DAI y"
                             " luego venderlo a dólares. \n"
                             "*/dolarcrypto* - Muestra el valor en el que se"
                             " comprarian dólares.\n"
                             "Otra opción para ver los comando es presionar"
                             " la tecla '/'. ",
                             parse_mode=ParseMode.MARKDOWN)


def valordai(update, context):
    user = update.message.from_user
    logger.info('El usuario %s (%s) puso valordai', user.full_name, user.username)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=valoresCompra())


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


def dolarcrypto(update, context):
    user = update.message.from_user
    esp = '           $ '
    satoshi = satoshi_com_pes / satoshi_ven_dol
    logger.info('El usuario %s (%s) puso dolarcrypto', user.full_name, user.username)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='*\nPrecio del Dólar:*\n\n'
                             
        '                       *Compra     |     Venta     |         Variación*\n'

        '*Oficial*' + esp + str('%.3f' % dolarCOf) +\
                    esp + str('%.3f' % dolarVOf) +\
                    esp + str('%.2f' % dolarVarOf) + '\n'
        '*Impuesto PAIS*' + '     $ ' +\
                        str('%.3f' % (dolarCOf * 1.3)) +\
                        esp + str('%.3f' % (dolarVOf * 1.3)) +\
                        esp + str('%.2f' % (dolarVarOf * 1.3)) + '\n'

         '*Blue*' + '              $ ' +\
                  str('%.2f' % dolarCBl) +\
                  esp + str('%.2f' % dolarVBl) +\
                  esp + str('%.2f' % dolarVarBl) + '\n'
         '*C.C.L.*' + '            $ ' +\
                    str('%.2f' % dolarCCCL) +\
                    esp + str('%.2f' % dolarVCCL) +\
                    esp + str('%.2f' % dolarVarCCL) + '\n'
         '*Bolsa*' + '             $ ' +\
                   str('%.2f' % dolarCBol) +\
                   esp + str('%.2f' % dolarVBol) +\
                   esp + str('%.2f' % dolarVarBol) + '\n'

         '\n\n\n*Decrypto DAI*' + '      $ ' + '\n'
         '*Decrypto USDT*' + '     $ ' + '\n'
         '*SatoshiTango*' + '      $ ' + str('%.4f' % satoshi) + '\n'
         '*BuenBit*' + '              ' + 'MOMENTANEAMENTE NO PERMITIDO\n'
         "*Qubit Brokers*" + "       " + "MOMENTANEAMENTE NO PERMITIDO\n",
         parse_mode=ParseMode.MARKDOWN)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('valordai', valordai))
updater.dispatcher.add_handler(CommandHandler('calc', calc))
updater.dispatcher.add_handler(CommandHandler('mejordaidolar', mejorDaiDolar))
updater.dispatcher.add_handler(CommandHandler('dolarcrypto', dolarcrypto))


updater.start_polling()
updater.idle()
