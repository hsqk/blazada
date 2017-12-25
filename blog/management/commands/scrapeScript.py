from django.core.management.base import BaseCommand, CommandError
from blog.models import Trackee, Tracker

import requests
import bs4
import os
import sys
appDir = os.getcwd()
librariesPath = appDir + '/blog/libraries'
sys.path.append(librariesPath)
import scrapeLogic


import telegram
#"364600088"


class Command(BaseCommand):
    help = 'Runs through all recorded trackees, scrapes website and checks if the target price has been reached, notifies mobile and deletes table entry if so, otherwise null'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('poll_id', nargs='+', type=int)
    
    def handle(self, *args, **options):
        token = '458733632:AAHzH3NtBMk2fvv4P0zb3Yr0qVUjnawew7k'
        bot = telegram.Bot(token=token)
        allTrackees = Trackee.objects.all()
        for i in range(len(allTrackees)):
            trackee = allTrackees[i]
            try:
                url = trackee.url
                alertPrice = trackee.target
                priceUnder = scrapeLogic.scrape_all(url, alertPrice, False, True)
                if priceUnder:
                    self.stdout.write(trackee.url + " under target")
                    chatId = Tracker.objects.get(mobile=trackee.mobile).chatId
                    #print(chatId)
                    text = "Yo! " + trackee.name + " has reached your target price of $" + str(trackee.target) + "\n \nGet it at " + trackee.url
                    bot.send_message(chat_id=chatId, text=text)
                    trackee.delete()
                else:
                    self.stdout.write(trackee.url + " not under target")
            except Exception as error:
                self.stdout.write(repr(error))
                self.stdout.write(trackee.url + " not valid")
                chatId = Tracker.objects.get(mobile=trackee.mobile).chatId
                #print(chatId)
                text = "Um. The URL for " + trackee.name + " seems to have changed. You'll have to find the new product page and track it with the blazada website again. Sorry about that. (For reference, the URL you entered was " + trackee.url + " )"
                bot.send_message(chat_id=chatId, text=text)
                trackee.delete()

