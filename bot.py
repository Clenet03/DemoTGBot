import telegram
from telegram.ext import CommandHandler, Updater

bot = telegram.Bot(token='6059622568:AAGPmXR6M0XM8PI8CVW_z3tIU0dFCNaBbEw')
updater = telegram.Bot(token='6059622568:AAGPmXR6M0XM8PI8CVW_z3tIU0dFCNaBbEw')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, welcome to the bot")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)