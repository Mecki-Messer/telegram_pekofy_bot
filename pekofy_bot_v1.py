import re
import logging
import random

import telegram
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext
from telegram.ext import Filters

#Pekofy_Bot is able to pekofy the last message that was sent into a chat!

#basic setup
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#insert your api token here!
apiToken=""

#Bot setup
updater = Updater(token=apiToken, use_context=True)
dispatcher = updater.dispatcher

#Other vars
#Not flexible enough, need RegEx for multiple chars (. ? !)
delimiter = "."
delimiterRE = ""
pekofied = False
lastMessage = ""

#PekoStats!
goodBotCount = 0
cuteBotCount = 0
badBotCount = 0
pekofiedCount = 0

#pekofy method
def peko(message):
    pekofiedMessage = ""
    
    tokens = message.split(delimiter)

    for s in tokens:
        s += " peko! "
        pekofiedMessage += s

    return pekofiedMessage

def magicPekoBall():
    pass

#Bot logic starting here!
#Methods
def start(update : Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Am Peko-Bot, will pekofy!")

def pekofy(update : Update, context: CallbackContext):
    global pekofied
    context.bot.send_message(chat_id=update.effective_chat.id, text=peko(lastMessage))
    pekofied = True

def storeLast(update : Update, context: CallbackContext):
    global lastMessage
    global pekofied
    
    lastMessage = update.message.text
    
    if "good bot" in update.message.text and pekofied==True:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Thank you peko!")
        pekofied = False
    if "cute bot" in update.message.text and pekofied==True:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ehehe, you are cute as well peko!")
        pekofied = False
            
    

#Handlers
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

pekofy_handler = CommandHandler("pekofy", pekofy)
dispatcher.add_handler(pekofy_handler)

lastMsg_handler = MessageHandler(Filters.text & (~Filters.command), storeLast)
dispatcher.add_handler(lastMsg_handler)

#Run Bot!
updater.start_polling()
