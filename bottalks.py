token = '458733632:AAHzH3NtBMk2fvv4P0zb3Yr0qVUjnawew7k'
import telegram
bot = telegram.Bot(token=token)

from telegram.ext import Updater
updater = Updater(token=token)
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot, update):
    """
    get chat id
    get mobile number
    update django trackers model, match number to chat id
    """
    bot.send_message(chat_id=update.message.chat_id, text="Hello! You'll receive a notification here when your tracked items have hit the desired prices. To check on your tracked items, enter /check")
    custom_keyboard = [[telegram.KeyboardButton("Send mobile number", request_contact=True)]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True,)
    bot.send_message(chat_id=update.message.chat_id, text="Custom Keyboard Test", reply_markup=reply_markup)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_polling()



from telegram.ext import MessageHandler, Filters

def echo(bot, update):
    if update.message.text=='1':
        bot.send_message(chat_id=update.message.chat_id, text='2, buckle my shoe')
        bot.send_message(chat_id=update.message.chat_id, text='3, oh a contact')
        bot.send_message(chat_id=update.message.chat_id, text='4, something muffin')

def matchMobile(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.contact.phone_number)
    #link chatid to mobile number in trackers model

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

contact_handler = MessageHandler(Filters.contact, matchMobile)
dispatcher.add_handler(contact_handler)


# def check: get chatid, lookup mobile number in django trackee table, get everything, parse and send












updater.stop()


bot.send_message(chat_id="364600088", text="I'm a bot, please talk to me!")




