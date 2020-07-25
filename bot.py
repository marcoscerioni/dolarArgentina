from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
from valores import *
from auth import token

updater = Updater(token=token, use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    user = update.message.from_user
    logger.info('El usuario %s puso start', user.first_name)
    name = user.first_name
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Bienvenido " + name + ", "
                             "al Bot de la criptomenda DAI"
                             " en Argentina \n\n"
                             "Los comandos disponibles son: \n"
                             "/start - Instrucciones del Bot. \n"
                             "/valordai - Valor del DAI.\n"
                             "/calc NUMERO - Calcula la cantidad que DAI que "
                             'obtendrias en cada exchange. \n'
                             "/mejordaidolar - Mejor opción para comprar DAI y"
                             " luego venderlo a dólares. \n"
                             "/dolarcrypto - Muestra el valor en el que se"
                             " comprarian dólares.\n"
                             "Otra opción para ver los comando es presionar"
                             " la tecla '/' y ahi aparecerán los comandos")


def valordai(update, context):
    user = update.message.from_user
    logger.info('El usuario %s puso valordai', user.first_name)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=valoresCompra())


def calc(update, context):
    user = update.message.from_user
    logger.info('El usuario %s puso calc', user.first_name)
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
    logger.info('El usuario %s puso mejorDaiDolar', user.first_name)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=daiADolar())


def dolarcrypto(update, context):
    user = update.message.from_user
    logger.info('El usuario %s puso dolarcrypto', user.first_name)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=valorDelDolar())


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('valordai', valordai))
updater.dispatcher.add_handler(CommandHandler('calc', calc))
updater.dispatcher.add_handler(CommandHandler('mejordaidolar', mejorDaiDolar))
updater.dispatcher.add_handler(CommandHandler('dolarcrypto', dolarcrypto))


updater.start_polling()
updater.idle()
