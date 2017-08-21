import telegram
import utils as ut
from telegram.ext import Updater, CommandHandler, \
MessageHandler, Filters

#token do @BotFather
my_token = ""

def start(bot,update):
	update.message.reply_text("allons-y!")

def help(bot, update):
	update.message.reply_text("Help! I need somebody HELP!")	

def error(bot,update,error):
	print(error)

def dolar(bot, update):
	dolar = ut.getDolar()
	update.message.reply_text("Cotação de hoje: R$ {}".format(dolar))

def menu(bot,update):
	update.message.reply_text(ut.get_menu())

updater = Updater(my_token)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("help",help))
dp.add_handler(CommandHandler("dolar",dolar))
dp.add_handler(CommandHandler("menu",menu))
dp.add_error_handler(error)

updater.start_polling()

updater.idle()