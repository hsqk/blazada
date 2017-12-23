token = '458733632:AAHzH3NtBMk2fvv4P0zb3Yr0qVUjnawew7k'

import telegram
import logging

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from blog.models import Trackee, Tracker

bot = telegram.Bot(token=token)


updater = Updater(token=token)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


def start(bot, update):
    """
    get chat id
    get mobile number
    update django trackers model, match number to chat id
    """
    try:
        bot.send_message(chat_id=update.message.chat_id, text="Hello! You'll receive a notification here when your tracked items have hit the desired prices. To check on your tracked items, enter /check")
        custom_keyboard = [[telegram.KeyboardButton("Send mobile number", request_contact=True)]]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True,)
        bot.send_message(chat_id=update.message.chat_id, text="To use this bot, please press the button below to let it use your mobile number. No spam, promise.", reply_markup=reply_markup)
    except Exception as error:
        print(repr(error))

def check(bot, update):
    try:
        tracker = Tracker.objects.get(chatId=update.message.chat_id)
        trackees = Trackee.objects.filter(mobile=tracker.mobile)
        if len(trackees) == 0:
            bot.send_message(chat_id=update.message.chat_id, text='No items being tracked. Use the Blazada website to track some, if you\'d like')
        else:
            for trackee in trackees:
                bot.send_message(chat_id=update.message.chat_id, text="Target price: " +  str(trackee.target) + "\n  Item: " + trackee.name)
    except Exception as error:
        print(repr(error))

start_handler = CommandHandler('start', start)
check_handler = CommandHandler('check', check)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(check_handler)

updater.start_polling()



def echo(bot, update):
    try:
        if update.message.text=='1':
            bot.send_message(chat_id=update.message.chat_id, text='2, buckle my shoe')
    except Exception as error:
        print(repr(error))

def matchMobile(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id, text="Thanks! Now just sit back and wait for your notification :)")
        chatId = update.message.chat_id
        mobile = update.message.contact.phone_number
        tracker = Tracker.objects.get(mobile = "+"+mobile)
        tracker.chatId = chatId
        tracker.save()
    except Exception as error:
        print(repr(error))

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

contact_handler = MessageHandler(Filters.contact, matchMobile)
dispatcher.add_handler(contact_handler)


#updater.stop()




