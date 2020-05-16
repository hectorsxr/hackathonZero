# telegram-python-bot
from telegram.ext import Updater, CommandHandler

def main():
    #Instanciamos updater
    updater = Updater(token=open('./bot_token').read(), use_context=True)
    # Manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))
    # Manejador al comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))
    # Manejador al comando /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))
    # Empieza a padir notificaciones
    updater.start_polling()
    # Capturamo señal de parada
    updater.idle()

def start(update, context):
    update.message.reply_text('Holaaaa')

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    # args = [2, 2]
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text('El resultado es: ' + str(resultado))

main()